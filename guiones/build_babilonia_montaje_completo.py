#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MONTAJE COMPLETO de Babilonia: fusiona los 202 clips base + los 95 de relleno en UNA sola lista
en orden, a 8 s cada uno (~293 clips ≈ 39 min = la voz en off completa). Cada fila trae: nº de
montaje, id original (#N base o R# relleno), minuto (inicio-fin), tipo, estado, la voz en off que
suena en ese momento y el prompt. Sale en .md y .csv.
Lee: babilonia-voz-en-off-limpio.md, babilonia-prompts.md, babilonia-relleno-prompts.md
Ejecuta:  python3 build_babilonia_montaje_completo.py
"""
import re
import csv

SEG = 8  # segundos por clip
CLIPS_HECHOS_BASE = 131  # clips base #1..#131 ya generados

ELARA_PHRASES = [
    "Soy Elara, y esta noche vamos a vivir, hora a hora, la última noche de Babilonia.",
    "Cuando cruzabas esa puerta, no entrabas a una ciudad cualquiera. Entrabas al ombligo del mundo.",
    "Si quieres entender la respuesta completa, quédate conmigo hasta el final.",
    "A Babilonia no la conquistaron. La entregaron.",
    "Y las murallas colosales, esas por las que Babilonia se creía eterna, no sirvieron de nada.",
    "Cada vez que miras el reloj y ves que son las ocho y cuarto",
    "Mueren cuando pierden la voluntad de ser lo que son.",
    "Dime con sinceridad: ¿crees que las civilizaciones caen por sus enemigos… o por los suyos?",
    "Soy Elara. Nos vemos en la historia.",
]


def load_narration():
    with open("babilonia-voz-en-off-limpio.md", encoding="utf-8") as f:
        raw = f.read()
    body = raw.split("\n---\n", 1)[1] if "\n---\n" in raw else raw
    return re.sub(r"\s+", " ", body).strip()


def blocknum(s):
    m = re.search(r"B(\d+)", s)
    return int(m.group(1)) if m else None


def parse_base():
    with open("babilonia-prompts.md", encoding="utf-8") as f:
        content = f.read()
    clips = []
    pat = re.compile(r"### #(\d+) · (.+?) · (.+?) · \*(.+?)\*\s*\n```\n(.*?)\n```", re.DOTALL)
    for m in pat.finditer(content):
        n = int(m.group(1)); tag = m.group(2); bloque = m.group(3)
        elara = "(ELARA)" in tag
        tipo = "Elara" if elara else ("Imagen" if "IMAGEN" in tag else "Video")
        clips.append({"id": f"#{n}", "orden": n, "bnum": blocknum(bloque),
                      "bloque": bloque, "tipo": tipo, "elara": elara,
                      "prompt": m.group(5).strip(),
                      "estado": "HECHO" if n <= CLIPS_HECHOS_BASE else "FALTA"})
    clips.sort(key=lambda c: c["orden"])
    return clips


def parse_relleno():
    with open("babilonia-relleno-prompts.md", encoding="utf-8") as f:
        content = f.read()
    rell, trans = [], []
    pat = re.compile(r"### R(\d+) · (.+?)\n```\n(.*?)\n```", re.DOTALL)
    for m in pat.finditer(content):
        rid = int(m.group(1))
        header_rest = m.group(2)
        parts = [p.strip() for p in header_rest.split("·")]
        tag = parts[0]
        ubic = parts[1] if len(parts) > 1 else ""
        tipo = "Imagen" if "IMAGEN" in tag else "Video"
        item = {"id": f"R{rid}", "tipo": tipo, "elara": False,
                "prompt": m.group(3).strip(), "estado": "FALTA"}
        bn = blocknum(ubic)
        if bn is None:  # transición
            item["bloque"] = "TRANSICIÓN"; item["bnum"] = None
            trans.append(item)
        else:
            item["bloque"] = ubic; item["bnum"] = bn
            rell.append(item)
    return rell, trans


def split_even(text, k):
    words = text.split()
    if k <= 0:
        return []
    if not words:
        return [""] * k
    per = len(words) / k
    out, start = [], 0
    for i in range(k):
        end = len(words) if i == k - 1 else round((i + 1) * per)
        out.append(" ".join(words[start:end]).strip()); start = end
    return out


def mmss(s):
    s = int(round(s)); return f"{s//60:02d}:{s%60:02d}"


def main():
    base = parse_base()
    rell, trans = parse_relleno()

    # relleno agrupado por nº de bloque
    rell_by_b = {}
    for r in rell:
        rell_by_b.setdefault(r["bnum"], []).append(r)

    # fusionar: tras el último clip base de cada bloque, insertar su relleno
    merged = []
    for i, c in enumerate(base):
        merged.append(c)
        next_bnum = base[i + 1]["bnum"] if i + 1 < len(base) else None
        if c["bnum"] != next_bnum and c["bnum"] in rell_by_b:
            merged.extend(rell_by_b[c["bnum"]])

    # repartir la voz en off por las frases de Elara (anclas) sobre la lista fusionada
    text = load_narration()
    elara_idx = [i for i, c in enumerate(merged) if c["elara"]]
    chunks = []
    idx = 0
    for ph in ELARA_PHRASES:
        pos = text.find(ph, idx)
        chunks.append(text[idx:pos].strip()); idx = pos + len(ph)
        chunks.append(ph)  # marca de Elara
    chunks.append(text[idx:].strip())

    # segmentos de merged entre clips de Elara
    narr = {}
    seg_bounds = [-1] + elara_idx + [len(merged)]
    # chunks: [prosa0, E1, prosa1, E2, ..., E9, prosaN]
    ci = 0
    prev = -1
    carry = ""
    for k, ei in enumerate(elara_idx):
        seg = merged[prev + 1:ei]          # clips antes de esta Elara
        prose = chunks[2 * k]              # prosa correspondiente
        parts = split_even(prose, len(seg))
        if carry and parts:
            parts[0] = (carry + " " + parts[0]).strip(); carry = ""
        elif carry and not seg:
            pass
        for c, p in zip(seg, parts):
            narr[id(c)] = p
        if not seg:
            carry = (carry + " " + prose).strip()
        narr[id(merged[ei])] = chunks[2 * k + 1]  # frase de Elara
        prev = ei
    # cola tras la última Elara
    seg = merged[prev + 1:]
    prose = chunks[-1]
    parts = split_even(prose, len(seg))
    for c, p in zip(seg, parts):
        narr[id(c)] = p

    # timecodes 8s
    t = 0.0
    for c in merged:
        c["ini"], c["fin"] = t, t + SEG; t += SEG
    total = mmss(t)

    n_img = sum(1 for c in merged if c["tipo"] == "Imagen")
    n_vid = sum(1 for c in merged if c["tipo"] == "Video")
    n_ela = sum(1 for c in merged if c["tipo"] == "Elara")

    # ---- MD ----
    out = []
    out.append("# BABILONIA — MONTAJE COMPLETO (base + relleno, en orden)\n")
    out.append(f"**Canal:** Elara Historiadora · **Clips en total:** {len(merged)} · "
               f"**Duración a 8 s:** ~{total} · 🖼️ {n_img} · 🎬 {n_vid} · 👩 {n_ela}\n")
    out.append("> ✅ ESTA es tu lista para montar de principio a fin. Son tus 202 clips base + los "
               "95 de relleno YA intercalados en orden. A 8 s cada uno cubren TODA la voz en off.\n")
    out.append("> - **id** = el nombre de tu archivo generado: `#N` = clip base "
               "(`babilonia-prompts.md`) · `R#` = relleno (`babilonia-relleno-prompts.md`).\n")
    out.append(f"> - ✅ HECHO = ya generado (base #1–#{CLIPS_HECHOS_BASE}) · ⏳ FALTA = por generar "
               "(incluye TODO el relleno).\n")
    out.append("> - Los 47 de relleno EXTRA y los prompts POR FRASE son REPUESTOS: úsalos solo si "
               "quieres cambiar o enriquecer algún plano. NO hacen falta para completar la voz.\n")
    out.append("\n---\n")
    bactual = None
    rows = []
    for i, c in enumerate(merged, 1):
        if c["bloque"] != bactual and c["tipo"] != "Elara":
            # cabecera por bloque (usa el nombre del bloque base)
            pass
        estado = "✅ HECHO" if c["estado"] == "HECHO" else "⏳ FALTA"
        ntxt = narr.get(id(c), "").strip()
        out.append(f"\n### {i}. [{c['id']}] · {mmss(c['ini'])}–{mmss(c['fin'])} · "
                   f"{c['tipo']} · {estado}\n")
        out.append(f"🎙️ **Voz en off:** {ntxt}\n\n")
        out.append("🎬 **Prompt:**\n```\n" + c["prompt"] + "\n```\n")
        rows.append({"montaje": i, "id": c["id"], "inicio": mmss(c["ini"]),
                     "fin": mmss(c["fin"]), "tipo": c["tipo"], "estado": c["estado"],
                     "narracion": ntxt, "prompt": c["prompt"]})

    if trans:
        out.append("\n---\n## 🔀 TRANSICIONES (opcionales, entre secciones)\n")
        for tr in trans:
            out.append(f"\n### [{tr['id']}] · {tr['tipo']} · transición\n")
            out.append("```\n" + tr["prompt"] + "\n```\n")

    with open("babilonia-MONTAJE-COMPLETO.md", "w", encoding="utf-8") as f:
        f.write("".join(out))

    with open("babilonia-MONTAJE-COMPLETO.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["montaje", "id", "inicio", "fin", "tipo",
                                          "estado", "narracion", "prompt"])
        w.writeheader(); w.writerows(rows)

    print(f"OK · total={len(merged)} (base={len(base)} + relleno={len(rell)}) · "
          f"dur=~{total} · transiciones={len(trans)}")


if __name__ == "__main__":
    main()
