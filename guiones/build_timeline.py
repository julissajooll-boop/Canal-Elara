#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador GENERICO de timeline de montaje DESDE la voz en off (canal Elara Historiadora).
Uso:  python3 guiones/build_timeline.py <voz_en_off.md> <timeline_salida.md> "<TITULO>"
Regla: la voz manda. Divide la narracion en tramos de 8 s (voz de Elara ~164 wpm).
Salida: tabla markdown con # clip, inicio, fin, tipo, bloque y TEXTO EXACTO.
"""
import sys, re

WPM = 164.0
SEG = 8
WMIN, WMAX = 18, 22
END = tuple(".!?…")

def hhmmss(s):
    m, s = divmod(int(round(s)), 60)
    return f"{m:02d}:{s:02d}"

BLOCKS = [("COLD OPEN","COLD OPEN"),("HOOK","HOOK"),("CONTEXTO","CONTEXTO"),
          ("ACTO 1","ACTO 1"),("ACTO 2","ACTO 2"),("ACTO 3","ACTO 3"),
          ("CIERRE","CIERRE"),("CTA","CTA FINAL")]

def main():
    voz, out = sys.argv[1], sys.argv[2]
    titulo = sys.argv[3] if len(sys.argv) > 3 else "GUION"
    words = []  # (palabra, bloque, es_elara)
    block, elara_sec, elara_mark = "INTRO", False, False
    for raw in open(voz, encoding="utf-8"):
        s = raw.strip()
        if s.startswith("## ") and "DATOS" in s.upper():
            break
        if s.startswith("## "):
            up = s.upper(); block = "OTRO"
            for k, n in BLOCKS:
                if k in up: block = n; break
            elara_sec = ("COLD OPEN" in up) or ("HOOK" in up) or ("CTA FINAL" in up)
            elara_mark = False; continue
        if s.replace("*","").strip() == "[ELARA A CÁMARA]":
            elara_mark = True; continue
        if (not s or s.startswith("#") or s.startswith(">") or s.startswith("|")
                or s.startswith("---") or s.startswith("- ")):
            continue
        es = elara_sec or elara_mark
        for w in s.split():
            words.append((w, block, es))
    # agrupar en tramos ~8s
    clips, buf, bb, be = [], [], None, None
    def flush():
        nonlocal buf, bb, be
        if buf: clips.append((" ".join(buf), bb, be)); buf = []
    for w, b, es in words:
        if not buf: bb, be = b, es
        if buf and es != be:
            flush(); bb, be = b, es
        buf.append(w); n = len(buf)
        if (n >= WMIN and w.endswith(END)) or n >= WMAX: flush()
    flush()
    # filas
    rows, ic, t = [], 0, 0
    for i, (tx, b, es) in enumerate(clips, 1):
        if es: tipo = "🗣️ Elara (lip-sync)"
        else:
            ic += 1; tipo = "🎬 Video (Flow)" if ic % 4 == 0 else "🖼️ Imagen (Ken Burns)"
        rows.append((i, hhmmss(t), hhmmss(t+SEG), tipo, b, tx)); t += SEG
    tw = len(words); dv = tw/WPM*60; dc = len(clips)*SEG; ne = sum(1 for c in clips if c[2])
    with open(out, "w", encoding="utf-8") as f:
        f.write(f"# {titulo} — TIMELINE DE MONTAJE (generada desde la voz en off)\n")
        f.write("## Elara Historiadora · tramos de 8 s · la voz manda\n\n")
        f.write("> Generada con `build_timeline.py`. Cada fila = un tramo de 8 s con el TEXTO EXACTO.\n")
        f.write("> Empata cada fila con un clip de la biblioteca visual (`*-desglose-clips.md`).\n\n")
        f.write("### 📊 Verificación de cuadre\n")
        f.write(f"- Palabras narradas: **{tw}**\n- Voz de Elara: **{WPM:.0f} wpm**\n")
        f.write(f"- Duración estimada de la voz: **{hhmmss(dv)}**\n")
        f.write(f"- Nº de tramos/clips (8 s): **{len(clips)}** → {hhmmss(dc)} de video\n")
        f.write(f"- Clips de Elara a cámara: {ne}\n")
        d = abs(dv-dc); f.write(f"- Diferencia voz vs. clips: {int(d)} s → {'✅ CUADRA (±1 min)' if d<=60 else '⚠️ AJUSTAR'}\n\n")
        f.write("> 🔧 Perilla de ajuste: las imágenes (Ken Burns) no tienen duración fija; ajústalas\n")
        f.write("> entre ~7 y ~9 s para cuadrar con la voz. Los videos de Flow y los clips de Elara van a 8 s.\n\n---\n\n")
        f.write("| # | Inicio | Fin | Tipo | Bloque | Texto EXACTO narrado (8 s) |\n")
        f.write("|---|--------|-----|------|--------|-----------------------------|\n")
        for i, a, b_, tp, bl, tx in rows:
            tx_md = tx.replace("|", "\\|")
            f.write(f"| {i} | {a} | {b_} | {tp} | {bl} | {tx_md} |\n")
    print(f"{titulo}: palabras={tw}  voz={hhmmss(dv)}  clips={len(clips)} ({hhmmss(dc)})  elara={ne}  diff={int(abs(dv-dc))}s")

if __name__ == "__main__":
    main()
