#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el MAPA DE ORDEN con timecodes de Pompeya: secuencia exacta de imagenes y
clips por bloque de narracion, con tiempo acumulado (IMG=3s, CLIP=8s)."""
import re

SRC = "/projects/sandbox/Canal-Elara/guiones/pompeya-guion-visual-completo.md"
OUT = "/projects/sandbox/Canal-Elara/guiones/pompeya-orden-prompts.md"

IMG_SECS = 3
CLIP_SECS = 8

with open(SRC, encoding="utf-8") as f:
    lines = f.readlines()

acto_re = re.compile(r"^# (ACTO .+|CIERRE.*|FRASE FINAL.*)")
block_re = re.compile(r"^### (N\d+)\s*·\s*(.+)$")
img_re = re.compile(r"^- IMG:\s*(.+?)\s*$")
clip_re = re.compile(r"^- CLIP:\s*(.+?)\s*$")
elara_re = re.compile(r"^- \*\*CLIP \(ELARA[^)]*\):\*\*\s*(.+?)\s*$")

items = []
cur_acto = ""
cur_block = None

for ln in lines:
    ma = acto_re.match(ln)
    if ma:
        cur_acto = ma.group(1).strip()
        items.append(("acto", cur_acto))
        continue
    mb = block_re.match(ln)
    if mb:
        cur_block = {"id": mb.group(1), "narr": mb.group(2).strip().strip('"')}
        items.append(("block", cur_block))
        continue
    mi = img_re.match(ln)
    if mi:
        items.append(("img", mi.group(1).strip()))
        continue
    me = elara_re.match(ln)
    if me:
        items.append(("elara", me.group(1).strip()))
        continue
    mc = clip_re.match(ln)
    if mc:
        items.append(("clip", mc.group(1).strip()))
        continue


def fmt(s):
    return "%d:%02d" % (s // 60, s % 60)


def short(t, n=70):
    t = t.strip()
    return (t[:n] + "…") if len(t) > n else t


md = []
md.append("# POMPEYA — MAPA DE ORDEN CON TIMECODES\n")
md.append("**Canal:** Elara Historiadora · IMG = 3 s (Ken Burns) · CLIP = 8 s.\n")
md.append("> Secuencia exacta de montaje (de arriba a abajo). El tiempo es acumulado. "
          "Cada bloque N# muestra la frase de narracion que debe sonar mientras pasan sus piezas.\n")

n_img = sum(1 for t, _ in items if t == "img")
n_clip = sum(1 for t, _ in items if t in ("clip", "elara"))
total = n_img * IMG_SECS + n_clip * CLIP_SECS
md.append("**Imagenes:** %d · **Clips:** %d · **Duracion total:** ~%s\n"
          % (n_img, n_clip, fmt(total)))
md.append("\n---\n")

t = 0
img_i = 0
clip_i = 0
for kind, data in items:
    if kind == "acto":
        md.append("\n## 🎬 %s\n" % data)
    elif kind == "block":
        md.append("\n**%s** — 🎙️ *\"%s\"*\n" % (data["id"], data["narr"]))
        md.append("| Tiempo | Pieza | Descripcion |")
        md.append("|--------|-------|-------------|")
    elif kind == "img":
        img_i += 1
        md.append("| %s | IMG %d | %s |" % (fmt(t), img_i, short(data).replace("|", "\\|")))
        t += IMG_SECS
    elif kind == "clip":
        clip_i += 1
        md.append("| %s | CLIP %d | %s |" % (fmt(t), clip_i, short(data).replace("|", "\\|")))
        t += CLIP_SECS
    elif kind == "elara":
        clip_i += 1
        md.append("| %s | CLIP %d (ELARA) | %s |" % (fmt(t), clip_i, short(data).replace("|", "\\|")))
        t += CLIP_SECS

md.append("\n---\n")
md.append("## Apariciones de ELARA (clips clave)\n")
md.append("- **N2** (apertura) · **N23** (la revelacion) · **N48** (cierre + CTA)\n")
md.append("## Montaje\n")
md.append("1. Genera cada pieza con su prompt blindado de `pompeya-prompts.md`.\n")
md.append("2. Monta en este orden exacto (arriba a abajo).\n")
md.append("3. La voz en off de `pompeya-ultimas-24-horas-narracion.docx` corre continua; "
          "cada bloque N# indica que frase suena en esas piezas.\n")
md.append("4. Ritmo: acorta imagenes (1.5-2 s) en la erupcion/oleada; alargalas (3-4 s) "
          "en los moldes y el cierre.\n")

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(md) + "\n")

print("OK ->", OUT)
print("Imagenes:", n_img, "| Clips:", n_clip, "| Total:", fmt(total))
