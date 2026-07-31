#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera la timeline de montaje de Tenochtitlan DESDE la voz en off.
Regla del canal: la voz manda. Se divide la narracion en tramos de 8 s
(velocidad medida de la voz de Elara en ElevenLabs: ~164 palabras/min).
Salida: tabla markdown con # clip, inicio, fin, tipo, bloque y TEXTO EXACTO.
"""
import re
import math

VOZ = "guiones/tenochtitlan-voz-en-off.md"
OUT = "guiones/tenochtitlan-timeline-montaje.md"

WPM = 164.0                     # velocidad real de la voz de Elara (medida)
SEG_POR_CLIP = 8                # cada tramo/clip = 8 s
WORDS_MIN = 18                  # corta al llegar a ~18 palabras en fin de frase
WORDS_MAX = 22                  # corte forzado si no hay puntuacion (media ~8 s a 164 wpm)

def hhmmss(seg):
    m, s = divmod(int(round(seg)), 60)
    return f"{m:02d}:{s:02d}"

# --- 1) Extraer SOLO la narracion hablada, con etiqueta de bloque y si es Elara ---
segments = []          # lista de (texto_palabra, bloque, es_elara)
current_block = "INTRO"
elara_section = False
elara_marker = False   # marcador standalone dentro de una seccion (p.ej. Cierre)

BLOCK_MAP = [
    ("HOOK", "HOOK"), ("CONTEXTO", "CONTEXTO"), ("ACTO 1", "ACTO 1 · ORIGEN"),
    ("ACTO 2", "ACTO 2 · GRANDEZA"), ("ACTO 3", "ACTO 3 · CAIDA"),
    ("CIERRE", "CIERRE"), ("CTA FINAL", "CTA FINAL"),
]

with open(VOZ, encoding="utf-8") as f:
    lines = f.readlines()

for raw in lines:
    line = raw.rstrip("\n")
    stripped = line.strip()
    # Fin del contenido narrado
    if stripped.startswith("## ") and "DATOS" in stripped.upper():
        break
    # Cabecera de seccion principal -> define bloque y si es Elara
    if stripped.startswith("## "):
        up = stripped.upper()
        current_block = "OTRO"
        for key, name in BLOCK_MAP:
            if key in up:
                current_block = name
                break
        elara_section = ("HOOK" in up) or ("CTA FINAL" in up)
        elara_marker = False
        continue
    # Marcador standalone de Elara (p.ej. dentro del Cierre)
    if stripped.replace("*", "").strip() == "[ELARA A CÁMARA]":
        elara_marker = True
        continue
    # Saltar subtitulos ###, citas >, tablas |, separadores, vacios, y linea de titulo #
    if (not stripped or stripped.startswith("#") or stripped.startswith(">")
            or stripped.startswith("|") or stripped.startswith("---")
            or stripped.startswith("- ")):
        continue
    # Es una linea de narracion real
    es_elara = elara_section or elara_marker
    for w in stripped.split():
        segments.append((w, current_block, es_elara))

# --- 2) Agrupar palabras en tramos (~8 s) respetando fin de frase ---
clips = []
buf = []
buf_block = None
buf_elara = None
END_PUNCT = tuple(".!?…")

def flush():
    global buf, buf_block, buf_elara
    if buf:
        clips.append((" ".join(buf), buf_block, buf_elara))
        buf = []

for w, block, es_elara in segments:
    if not buf:
        buf_block, buf_elara = block, es_elara
    # Si cambia el modo Elara/normal, cerrar el tramo actual
    if buf and es_elara != buf_elara:
        flush()
        buf_block, buf_elara = block, es_elara
    buf.append(w)
    n = len(buf)
    ends_sentence = w.endswith(END_PUNCT) or w.endswith(('.”', '."', '.\u201d'))
    if (n >= WORDS_MIN and ends_sentence) or n >= WORDS_MAX:
        flush()
flush()

# --- 3) Tipo (rimo): Elara donde toca; resto 3 imagenes + 1 video ---
rows = []
img_counter = 0
t = 0
for i, (texto, block, es_elara) in enumerate(clips, start=1):
    if es_elara:
        tipo = "🗣️ Elara (lip-sync)"
    else:
        img_counter += 1
        tipo = "🎬 Video (Flow)" if img_counter % 4 == 0 else "🖼️ Imagen (Ken Burns)"
    inicio = hhmmss(t)
    fin = hhmmss(t + SEG_POR_CLIP)
    rows.append((i, inicio, fin, tipo, block, texto))
    t += SEG_POR_CLIP

# --- 4) Metricas ---
total_words = len(segments)
dur_voz_seg = total_words / WPM * 60.0
dur_clips_seg = len(clips) * SEG_POR_CLIP
n_elara = sum(1 for c in clips if c[2])

# --- 5) Escribir markdown ---
with open(OUT, "w", encoding="utf-8") as f:
    f.write("# TENOCHTITLÁN — TIMELINE DE MONTAJE (generada desde la voz en off)\n")
    f.write("## Elara Historiadora · tramos de 8 s · la voz manda\n\n")
    f.write("> Generada automáticamente con `build_tenochtitlan_timeline.py` a partir de\n")
    f.write("> `tenochtitlan-voz-en-off.md`. Cada fila = un tramo de 8 s con el TEXTO EXACTO\n")
    f.write("> que se narra. Empata cada fila con un clip de la biblioteca visual\n")
    f.write("> (`tenochtitlan-desglose-clips.md` / `tenochtitlan-shorts.md`).\n\n")
    f.write("### 📊 Verificación de cuadre\n")
    f.write(f"- Palabras narradas: **{total_words}**\n")
    f.write(f"- Velocidad de la voz de Elara: **{WPM:.0f} palabras/min** (medida)\n")
    f.write(f"- Duración estimada de la voz en off: **{hhmmss(dur_voz_seg)}**\n")
    f.write(f"- Nº de tramos/clips (8 s): **{len(clips)}**  →  {hhmmss(dur_clips_seg)} de video\n")
    f.write(f"- De ellos, clips de **Elara a cámara**: {n_elara}\n")
    diff = abs(dur_voz_seg - dur_clips_seg)
    ok = "✅ CUADRA (±1 min)" if diff <= 60 else "⚠️ AJUSTAR"
    f.write(f"- Diferencia voz vs. clips: {int(diff)} s  →  {ok}\n\n")
    f.write("> 🔧 Perilla de ajuste: las IMÁGENES (Ken Burns) no tienen duración fija; si el\n")
    f.write("> video queda algo más corto que la voz, alárgalas de 8 s a ~8–9 s (o baja el\n")
    f.write("> Speed de ElevenLabs a 0.92–0.95). Los videos de Flow y los clips de Elara van a 8 s.\n\n")
    f.write("---\n\n")
    f.write("| # | Inicio | Fin | Tipo | Bloque | Texto EXACTO narrado (8 s) |\n")
    f.write("|---|--------|-----|------|--------|-----------------------------|\n")
    for i, inicio, fin, tipo, block, texto in rows:
        texto_md = texto.replace("|", "\\|")
        f.write(f"| {i} | {inicio} | {fin} | {tipo} | {block} | {texto_md} |\n")

print(f"Palabras: {total_words}")
print(f"Duracion voz estimada: {hhmmss(dur_voz_seg)}")
print(f"Clips (8s): {len(clips)}  -> {hhmmss(dur_clips_seg)}")
print(f"Clips Elara: {n_elara}")
print(f"Diferencia: {int(abs(dur_voz_seg - dur_clips_seg))} s")
print(f"Escrito: {OUT}")
