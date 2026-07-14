#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HOJA DE MONTAJE DEFINITIVA de Babilonia, alineada con los 202 clips de `babilonia-prompts.md`
(la numeración que la usuaria YA está produciendo). Reparte la voz en off entre los 202 clips
EN ORDEN, usando los 9 clips de Elara como puntos de anclaje exactos. Así cada clip #N muestra
qué se narra mientras está en pantalla, y TODO coincide con el material ya generado.
Ejecuta:  python3 build_babilonia_montaje.py
"""
import re

CLIPS_HECHOS = 131  # nº de clips ya producidos por la usuaria (#1..#131)

# Frases EXACTAS de Elara (trozos literales de la voz en off), en orden.
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
    """Lee babilonia-prompts.md y devuelve lista de dicts {n, tipo, bloque, elara}."""
    clips = []
    with open("babilonia-prompts.md", encoding="utf-8") as f:
        for line in f:
            m = re.match(r"^### #(\d+) · (.+?) · (.+?) · ", line.strip())
            if not m:
                continue
            n = int(m.group(1))
            tipo_raw = m.group(2)
            bloque = m.group(3)
            elara = "(ELARA)" in tipo_raw
            if elara:
                tipo = "👩 ELARA"
            elif "IMAGEN" in tipo_raw:
                tipo = "🖼️ IMAGEN"
            else:
                tipo = "🎬 VIDEO"
            clips.append({"n": n, "tipo": tipo, "bloque": bloque, "elara": elara})
    clips.sort(key=lambda c: c["n"])
    return clips


def split_words_even(text, k):
    """Divide 'text' en k trozos contiguos con nº de palabras lo más parejo posible."""
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


def main():
    text = load_narration()
    clips = parse_clips()
    elara_nums = [c["n"] for c in clips if c["elara"]]
    assert len(elara_nums) == len(ELARA_PHRASES), \
        f"Elara en prompts={len(elara_nums)} vs frases={len(ELARA_PHRASES)}"

    # Trocear la voz en off en: prosa0, E1, prosa1, E2, ... , E9, prosa_final
    chunks = []  # lista de ("PROSE"/"ELARA", texto)
    idx = 0
    for ph in ELARA_PHRASES:
        pos = text.find(ph, idx)
        if pos == -1:
            raise SystemExit(f"No encontré la frase de Elara: {ph!r}")
        chunks.append(("PROSE", text[idx:pos].strip()))
        chunks.append(("ELARA", ph))
        idx = pos + len(ph)
    chunks.append(("PROSE", text[idx:].strip()))

    # Segmentos de clips entre puntos de Elara
    # orden real: [clips antes de E1][E1][clips entre E1-E2][E2]...[E9][clips tras E9]
    segments = []  # cada uno: ("PROSE", [clips]) o ("ELARA", clip)
    prev = 0
    for en in elara_nums:
        seg_clips = [c for c in clips if prev < c["n"] < en]
        segments.append(("PROSE", seg_clips))
        segments.append(("ELARA", next(c for c in clips if c["n"] == en)))
        prev = en
    seg_clips = [c for c in clips if c["n"] > prev]
    segments.append(("PROSE", seg_clips))

    # Emparejar chunks <-> segments (mismo patrón: PROSE,ELARA,...,PROSE)
    rows = []  # (clip, narracion)
    carry = ""  # prosa sobrante de segmentos sin clips
    for (ckind, ctext), (skind, sdata) in zip(chunks, segments):
        assert ckind == skind
        if skind == "ELARA":
            narr = (carry + " " if carry else "") + f"«{ctext}»  (Elara a cámara)"
            carry = ""
            rows.append((sdata, narr))
        else:
            seg_clips = sdata
            if not seg_clips:
                carry = (carry + " " if carry else "") + ctext  # prosa que se dirá sin clip propio
                continue
            parts = split_words_even(ctext, len(seg_clips))
            if carry:
                parts[0] = (carry + " " + parts[0]).strip()
                carry = ""
            for c, p in zip(seg_clips, parts):
                rows.append((c, p))
    rows.sort(key=lambda r: r[0]["n"])

    # Construir markdown
    total = len(rows)
    out = []
    out.append("# BABILONIA — HOJA DE MONTAJE DEFINITIVA (alineada con tus 202 clips)\n")
    out.append(f"**Canal:** Elara Historiadora · **Clips:** {total} (numeración de "
               f"`babilonia-prompts.md`) · ✅ hechos: #1–#{CLIPS_HECHOS} · ⏳ faltan: "
               f"#{CLIPS_HECHOS+1}–#{total}\n")
    out.append("> ✅ Esta es la hoja para que TODO coincida con lo que ya produjiste.\n"
               "> - **#** = el mismo número de clip de `babilonia-prompts.md` (tu archivo generado).\n"
               "> - **Narración** = las palabras de la voz en off que suenan MIENTRAS se ve ese clip.\n"
               "> - Móntalo EN ORDEN (#1, #2, #3…). La voz manda: cada clip dura lo que dure su "
               "frase (de media ~11–12 s). Las 🖼️ imágenes con Ken Burns; los 🎬 videos animados; "
               "los 👩 son Elara a cámara diciendo esa frase.\n")
    out.append("\n| # | Estado | Tipo | Narración que suena durante el clip |\n")
    out.append("|---|--------|------|--------------------------------------|\n")
    for c, narr in rows:
        estado = "✅" if c["n"] <= CLIPS_HECHOS else "⏳"
        safe = narr.replace("|", "/").strip()
        tipo = c["tipo"] + (f" ({elara_label(c['n'], elara_nums)})" if c["elara"] else "")
        out.append(f"| {c['n']} | {estado} | {tipo} | {safe} |\n")

    with open("babilonia-hoja-montaje.md", "w", encoding="utf-8") as f:
        f.write("".join(out))
    print(f"OK · clips={total} · hechos<= {CLIPS_HECHOS} · elara={len(elara_nums)}")


def elara_label(n, elara_nums):
    return "E" + str(elara_nums.index(n) + 1)


if __name__ == "__main__":
    main()
