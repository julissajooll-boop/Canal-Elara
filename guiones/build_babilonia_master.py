#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GUION MAESTRO DE MONTAJE de Babilonia: TODO en un solo archivo, en orden.
Para cada clip (#1..#202 de babilonia-prompts.md): nº, minuto (inicio-fin), tipo, estado
(hecho/falta), el TEXTO de la voz en off que suena en ese momento, y el PROMPT para generarlo.
Así la usuaria no tiene que saltar entre archivos.
Lee: babilonia-voz-en-off-limpio.md (narración) y babilonia-prompts.md (prompts).
Ejecuta:  python3 build_babilonia_master.py
"""
import re
import csv

CLIPS_HECHOS = 131
WPS = 2.5  # palabras por segundo (~150 wpm) para calcular la duración de cada clip

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


def parse_clips():
    with open("babilonia-prompts.md", encoding="utf-8") as f:
        content = f.read()
    clips = []
    # Cada bloque: ### #N · TAG · BLOQUE · *mov*  \n ``` \n prompt \n ```
    pattern = re.compile(
        r"### #(\d+) · (.+?) · (.+?) · \*(.+?)\*\s*\n```\n(.*?)\n```",
        re.DOTALL,
    )
    for m in pattern.finditer(content):
        n = int(m.group(1))
        tag = m.group(2).strip()
        bloque = m.group(3).strip()
        mov = m.group(4).strip()
        prompt = m.group(5).strip()
        elara = "(ELARA)" in tag
        if elara:
            tipo = "👩 ELARA"
        elif "IMAGEN" in tag:
            tipo = "🖼️ IMAGEN"
        else:
            tipo = "🎬 VIDEO"
        clips.append({"n": n, "tipo": tipo, "bloque": bloque, "mov": mov,
                       "prompt": prompt, "elara": elara})
    clips.sort(key=lambda c: c["n"])
    return clips


def split_words_even(text, k):
    words = text.split()
    if k <= 0:
        return []
    if not words:
        return [""] * k
    per = len(words) / k
    out, start = [], 0
    for i in range(k):
        end = len(words) if i == k - 1 else round((i + 1) * per)
        out.append(" ".join(words[start:end]).strip())
        start = end
    return out


def assign_narration(clips, text):
    elara_nums = [c["n"] for c in clips if c["elara"]]
    # trocear narración por las frases de Elara
    chunks = []
    idx = 0
    for ph in ELARA_PHRASES:
        pos = text.find(ph, idx)
        if pos == -1:
            raise SystemExit(f"No encontré: {ph!r}")
        chunks.append(("PROSE", text[idx:pos].strip()))
        chunks.append(("ELARA", ph))
        idx = pos + len(ph)
    chunks.append(("PROSE", text[idx:].strip()))
    # segmentos de clips
    segments = []
    prev = 0
    for en in elara_nums:
        segs = [c for c in clips if prev < c["n"] < en]
        segments.append(("PROSE", segs))
        segments.append(("ELARA", next(c for c in clips if c["n"] == en)))
        prev = en
    segments.append(("PROSE", [c for c in clips if c["n"] > prev]))

    narr = {}
    carry = ""
    for (ck, ctext), (sk, sdata) in zip(chunks, segments):
        if sk == "ELARA":
            narr[sdata["n"]] = (carry + " " if carry else "") + ctext
            carry = ""
        else:
            if not sdata:
                carry = (carry + " " if carry else "") + ctext
                continue
            parts = split_words_even(ctext, len(sdata))
            if carry:
                parts[0] = (carry + " " + parts[0]).strip()
                carry = ""
            for c, p in zip(sdata, parts):
                narr[c["n"]] = p
    return narr


def mmss(s):
    s = int(round(s))
    return f"{s // 60:02d}:{s % 60:02d}"


def main():
    text = load_narration()
    clips = parse_clips()
    narr = assign_narration(clips, text)

    # duración de cada clip proporcional a sus palabras narradas
    t = 0.0
    for c in clips:
        words = len(narr.get(c["n"], "").split())
        dur = max(3.0, words / WPS)  # mínimo 3 s por clip
        c["ini"], c["fin"] = t, t + dur
        t += dur
    total = mmss(t)

    out = []
    out.append("# BABILONIA — GUION MAESTRO DE MONTAJE (TODO EN UNO)\n")
    out.append(f"**Canal:** Elara Historiadora · **Clips:** {len(clips)} · **Duración total:** ~{total}\n")
    out.append("> 📖 Este es el ÚNICO archivo que necesitas para montar. De arriba a abajo, en orden.\n"
               "> Para CADA clip tienes: nº · minuto (inicio–fin) · tipo · estado · lo que se NARRA "
               "en ese momento · y el PROMPT para generarlo.\n")
    out.append("> - ✅ = ya lo tienes hecho (#1–#%d) · ⏳ = falta.\n" % CLIPS_HECHOS)
    out.append("> - 🖼️ imagen (Ken Burns) · 🎬 video (8 s animado) · 👩 Elara a cámara.\n")
    out.append("> - La VOZ manda: cada clip dura lo que dura su frase (por eso el minuto varía).\n")
    out.append("> - 👩/personajes recurrentes (Ciro, Nabucodonosor, Nabónido, Belsasar, Elara): "
               "sube su imagen de referencia (Ingredient) para que no cambien de cara.\n")
    out.append("> - Prompt negativo general (pégalo en todas):\n")
    out.append("```\nsin elementos modernos, sin ropa occidental contemporánea, sin militares "
               "modernos ni soldados occidentales, sin edificios modernos, sin banderas modernas, "
               "sin texto en inglés, sin logotipos, sin marcas de agua, sin anacronismos, sin "
               "rostros ni manos deformes, sin gore.\n```\n")
    out.append("\n---\n")

    elara_order = [x["n"] for x in clips if x["elara"]]
    bloque_actual = None
    rows_csv = []
    for c in clips:
        # cabecera de bloque cuando cambia
        if c["bloque"] != bloque_actual:
            bloque_actual = c["bloque"]
            out.append(f"\n## ▬▬ {bloque_actual} ▬▬\n")
        estado = "✅ HECHO" if c["n"] <= CLIPS_HECHOS else "⏳ FALTA"
        etiqueta = c["tipo"]
        eid = ""
        if c["elara"]:
            eid = "E" + str(elara_order.index(c["n"]) + 1)
            etiqueta += f" ({eid})"
        out.append(f"\n### #{c['n']} · {mmss(c['ini'])}–{mmss(c['fin'])} · {etiqueta} · {estado}\n")
        narr_txt = narr.get(c["n"], "").strip()
        out.append(f"🎙️ **Voz en off (suena aquí):** {narr_txt}\n\n")
        out.append("🎬 **Prompt:**\n```\n" + c["prompt"] + "\n```\n")
        # fila CSV
        tipo_txt = ("Elara" if c["elara"] else ("Imagen" if "IMAGEN" in c["tipo"] else "Video"))
        rows_csv.append({
            "clip": c["n"],
            "inicio": mmss(c["ini"]),
            "fin": mmss(c["fin"]),
            "tipo": tipo_txt,
            "elara_id": eid,
            "estado": "HECHO" if c["n"] <= CLIPS_HECHOS else "FALTA",
            "bloque": c["bloque"],
            "narracion": narr_txt,
            "prompt": c["prompt"],
        })

    with open("babilonia-GUION-MAESTRO.md", "w", encoding="utf-8") as f:
        f.write("".join(out))

    # CSV para Excel / Google Sheets
    campos = ["clip", "inicio", "fin", "tipo", "elara_id", "estado", "bloque",
              "narracion", "prompt"]
    with open("babilonia-GUION-MAESTRO.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(rows_csv)

    n_done = sum(1 for c in clips if c["n"] <= CLIPS_HECHOS)
    print(f"OK · clips={len(clips)} · duracion=~{total} · hechos<= {CLIPS_HECHOS} ({n_done}) · CSV ok")


if __name__ == "__main__":
    main()
