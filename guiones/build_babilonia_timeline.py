#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera la HOJA DE TIEMPO (timeline) de Babilonia a partir de la voz en off.
Regla: cada clip dura 8 s -> se divide la narración en tramos de ~8 s (≈19 palabras).
Así los clips SIEMPRE cuadran con la voz. Cada 8 s = un clip (imagen, video o Elara).
Lee `babilonia-voz-en-off-limpio.md` para no desincronizarse del guion.
Ejecuta:  python3 build_babilonia_timeline.py
"""
import re

SEG = 8  # segundos por clip
WORDS_MAX = 20  # tope de palabras por tramo de 8 s
WORDS_MIN_CUT = 15  # a partir de aquí, si termina frase, se corta

# Frases EXACTAS donde se VE la cara de Elara (trozos literales de la voz en off).
ELARA = [
    ("E1", "Soy Elara, y esta noche vamos a vivir, hora a hora, la última noche de Babilonia."),
    ("E2", "Cuando cruzabas esa puerta, no entrabas a una ciudad cualquiera. Entrabas al ombligo del mundo."),
    ("E3", "Si quieres entender la respuesta completa, quédate conmigo hasta el final."),
    ("E4", "A Babilonia no la conquistaron. La entregaron."),
    ("E5", "Y las murallas colosales, esas por las que Babilonia se creía eterna, no sirvieron de nada."),
    ("E6", "Cada vez que miras el reloj y ves que son las ocho y cuarto"),
    ("E7", "Mueren cuando pierden la voluntad de ser lo que son."),
    ("E8", "Dime con sinceridad: ¿crees que las civilizaciones caen por sus enemigos… o por los suyos?"),
    ("E9", "Soy Elara. Nos vemos en la historia."),
]


def load_narration():
    with open("babilonia-voz-en-off-limpio.md", encoding="utf-8") as f:
        raw = f.read()
    # Tomar solo lo que va después del primer separador '---'
    body = raw.split("\n---\n", 1)[1] if "\n---\n" in raw else raw
    # Unir en un solo texto, respetando espacios entre párrafos
    text = re.sub(r"\s+", " ", body).strip()
    return text


def split_sentences(txt):
    # Divide manteniendo el signo de puntuación final
    parts = re.split(r"(?<=[\.\?\!…])\s+", txt)
    return [p.strip() for p in parts if p.strip()]


def pack_prose(txt):
    """Divide prosa en tramos de ~8 s (<= WORDS_MAX palabras), cortando en fin de frase."""
    words = txt.split()
    beats, cur = [], []
    for w in words:
        cur.append(w)
        ends = w.endswith((".", "?", "!", "…"))
        if (len(cur) >= WORDS_MIN_CUT and ends) or len(cur) >= WORDS_MAX:
            beats.append(" ".join(cur))
            cur = []
    if cur:
        beats.append(" ".join(cur))
    return beats


def build_beats(text):
    """Devuelve lista de (tipo, texto, elara_id) en orden."""
    beats = []
    idx = 0
    for eid, phrase in ELARA:
        pos = text.find(phrase, idx)
        if pos == -1:
            raise SystemExit(f"NO ENCONTRÉ la frase de {eid}: {phrase!r}")
        before = text[idx:pos].strip()
        if before:
            for b in pack_prose(before):
                beats.append(("PROSE", b, None))
        beats.append(("ELARA", phrase, eid))
        idx = pos + len(phrase)
    tail = text[idx:].strip()
    if tail:
        for b in pack_prose(tail):
            beats.append(("PROSE", b, None))
    return beats


def mmss(s):
    return f"{s // 60:02d}:{s % 60:02d}"


def main():
    text = load_narration()
    beats = build_beats(text)

    rows = []
    prose_i = 0
    n_img = n_vid = n_ela = 0
    for i, (kind, txt, eid) in enumerate(beats):
        start = i * SEG
        end = (i + 1) * SEG
        if kind == "ELARA":
            tipo = f"👩 ELARA ({eid})"
            n_ela += 1
        else:
            # patrón: 3 imágenes y 1 video
            if prose_i % 4 == 3:
                tipo = "🎬 VIDEO"
                n_vid += 1
            else:
                tipo = "🖼️ IMAGEN"
                n_img += 1
            prose_i += 1
        rows.append((i + 1, mmss(start), mmss(end), tipo, txt))

    total = len(beats)
    dur = mmss(total * SEG)

    out = []
    out.append("# BABILONIA — HOJA DE TIEMPO (TIMELINE) · clip por clip\n")
    out.append(f"**Canal:** Elara Historiadora · **Clips totales:** {total} · "
               f"**Duración:** {dur} · 🖼️ {n_img} imágenes · 🎬 {n_vid} videos · 👩 {n_ela} Elara\n")
    out.append("> ✅ Cada clip dura **8 s**. La tabla está hecha dividiendo la VOZ EN OFF en "
               "tramos de 8 s, así los clips **cuadran exactamente** con lo que se narra.\n")
    out.append("> - **Inicio / Fin** = cuándo entra y sale ese clip en la línea de tiempo.\n"
               "> - **Qué se narra** = las palabras que suenan MIENTRAS se ve ese clip.\n"
               "> - 🖼️ = imagen con movimiento (Ken Burns 8 s) · 🎬 = clip animado (8 s) · "
               "👩 = se ve la cara de Elara diciendo esa frase.\n")
    out.append("> Timecodes aproximados: la voz manda; al grabarla, ajusta el fin de cada clip "
               "al audio real (por eso conviene cortar la voz por frases).\n")
    out.append("> ℹ️ **¿Ya produjiste desde `babilonia-prompts.md` (los 202 clips)?** NO necesitas "
               "esta versión a 8 s: mantén tus 202 clips y deja que cada uno dure lo que dure su "
               "frase (media ~11–12 s). Esta hoja es la alternativa para editar con cortes rígidos "
               "de 8 s. Tu material ya hecho es válido en ambos casos.\n")
    out.append("\n| # | Inicio | Fin | Tipo | Qué se narra en ese clip |\n")
    out.append("|---|--------|-----|------|--------------------------|\n")
    for n, ini, fin, tipo, txt in rows:
        safe = txt.replace("|", "/")
        out.append(f"| {n} | {ini} | {fin} | {tipo} | {safe} |\n")

    with open("babilonia-timeline-montaje.md", "w", encoding="utf-8") as f:
        f.write("".join(out))
    print(f"OK · clips={total} · duracion={dur} · img={n_img} · video={n_vid} · elara={n_ela}")


if __name__ == "__main__":
    main()
