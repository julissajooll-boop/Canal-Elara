#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extrae IMG y CLIP del guion visual completo de Pompeya y genera la hoja BLINDADA
   (tabla Markdown + CSV para lote), con anclaje historico romano y prompt negativo."""
import csv
import re

SRC = "/projects/sandbox/Canal-Elara/guiones/pompeya-guion-visual-completo.md"
OUT_MD = "/projects/sandbox/Canal-Elara/guiones/pompeya-prompts.md"
OUT_CSV = "/projects/sandbox/Canal-Elara/guiones/pompeya-prompts.csv"

PREFIX = ("Pompeya romana, año 79 d.C., Imperio Romano, arquitectura romana auténtica "
          "(mármol, frescos pompeyanos, columnas), togas y túnicas de época. ")
IMG_STYLE = (" Imagen fija para efecto Ken Burns. Fotorrealismo histórico, cinematográfico, "
             "8K, iluminación volumétrica, gran detalle.")
VID_STYLE = (" Clip de video de 8 s, movimiento de cámara cinematográfico y continuidad "
             "realista. Fotorrealismo histórico, 8K, iluminación volumétrica, gran detalle.")
NEGATIVE = ("sin elementos modernos, sin ropa occidental contemporánea, sin edificios "
            "modernos, sin texto en inglés, sin logotipos, sin marcas de agua, sin "
            "anacronismos, sin coches, sin rostros ni manos deformes, sin gore explícito.")

# Refuerzo de terminos ambiguos -> anclar a romano
SUBS = [
    (r"\bsoldados\b(?! romanos)", "soldados romanos"),
    (r"\bSoldados\b(?! romanos)", "Soldados romanos"),
]


def strengthen(t):
    for p, r in SUBS:
        t = re.sub(p, r, t)
    return t


def parse_movement(text):
    """Extrae el movimiento entre parentesis al final, si existe (solo IMG)."""
    m = re.search(r"\(([^)]*)\)\s*$", text)
    if m:
        mv = m.group(1).strip()
        base = text[:m.start()].strip()
        return base, mv
    return text.strip(), ""


with open(SRC, encoding="utf-8") as f:
    lines = f.readlines()

block_re = re.compile(r"^### (N\d+)\s*·\s*(.+)$")
img_re = re.compile(r"^- IMG:\s*(.+?)\s*$")
clip_re = re.compile(r"^- CLIP:\s*(.+?)\s*$")
elara_re = re.compile(r"^- \*\*CLIP \(ELARA[^)]*\):\*\*\s*(.+?)\s*$")

rows = []
cur_block = ""
cur_narr = ""
img_n = 0
clip_n = 0

for ln in lines:
    mb = block_re.match(ln)
    if mb:
        cur_block = mb.group(1)
        cur_narr = mb.group(2).strip().strip('"').strip("…")
        continue
    mi = img_re.match(ln)
    if mi:
        img_n += 1
        base, mv = parse_movement(mi.group(1))
        final = PREFIX + strengthen(base) + IMG_STYLE
        rows.append({"tipo": "IMG", "num": img_n, "bloque": cur_block,
                     "narr": cur_narr, "mov": mv, "prompt": final})
        continue
    mc = clip_re.match(ln)
    if mc:
        clip_n += 1
        base, _ = parse_movement(mc.group(1))
        # para clips el parentesis final no es movimiento de camara fijo; conservar texto
        base = mc.group(1).strip()
        final = PREFIX + strengthen(base) + VID_STYLE
        rows.append({"tipo": "CLIP", "num": clip_n, "bloque": cur_block,
                     "narr": cur_narr, "mov": "video 8s", "prompt": final})
        continue
    me = elara_re.match(ln)
    if me:
        clip_n += 1
        base = me.group(1).strip()
        final = ("ELARA (usar imagen base de Elara, ver guia-imagenes-base.md). " + PREFIX
                 + strengthen(base) + VID_STYLE)
        rows.append({"tipo": "CLIP-ELARA", "num": clip_n, "bloque": cur_block,
                     "narr": cur_narr, "mov": "video 8s", "prompt": final})
        continue

imgs = [r for r in rows if r["tipo"] == "IMG"]
clips = [r for r in rows if r["tipo"] != "IMG"]

# CSV
with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Orden", "Tipo", "N_tipo", "Bloque", "Movimiento",
                "Prompt_Final", "Prompt_Negativo", "Narracion"])
    for i, r in enumerate(rows, 1):
        w.writerow([i, r["tipo"], r["num"], r["bloque"], r["mov"],
                    r["prompt"], NEGATIVE, r["narr"]])


def esc(t):
    return t.replace("|", "\\|")


md = []
md.append("# POMPEYA — HOJA DE PROMPTS BLINDADOS (lote)\n")
md.append("**Canal:** Elara Historiadora · **Imágenes:** %d · **Clips de video:** %d · "
          "**Total:** %d prompts\n" % (len(imgs), len(clips), len(rows)))
md.append("> Extraído del guion visual completo. Anclaje histórico romano + estilo + "
          "negativo aplicados automáticamente. Imágenes = efecto Ken Burns; Clips = video 8 s.\n")
md.append("> Elara usa SIEMPRE su imagen base (ver `guia-imagenes-base.md`).\n")
md.append("")
md.append("## 🚫 PROMPT NEGATIVO OBLIGATORIO (cópialo en todas las generaciones)\n")
md.append("```")
md.append(NEGATIVE)
md.append("```")
md.append("")
md.append("---\n")
md.append("## Tabla completa (orden de montaje)\n")
md.append("| # | Tipo | Bloque | Mov. | Prompt (blindado) |")
md.append("|---|------|--------|------|-------------------|")
for i, r in enumerate(rows, 1):
    md.append("| %d | %s | %s | %s | %s |" % (
        i, r["tipo"], r["bloque"], esc(r["mov"]), esc(r["prompt"])))

md.append("")
md.append("---\n")
md.append("## Solo prompts de IMAGEN (%d, uno por línea)\n" % len(imgs))
md.append("```")
for r in imgs:
    md.append("[%s] %s" % (r["bloque"], r["prompt"]))
md.append("```")
md.append("")
md.append("## Solo prompts de VIDEO (%d, uno por línea)\n" % len(clips))
md.append("```")
for r in clips:
    tag = " (ELARA)" if r["tipo"] == "CLIP-ELARA" else ""
    md.append("[%s]%s %s" % (r["bloque"], tag, r["prompt"]))
md.append("```")

with open(OUT_MD, "w", encoding="utf-8") as f:
    f.write("\n".join(md) + "\n")

print("Filas totales:", len(rows))
print("Imagenes:", len(imgs))
print("Clips (incl. Elara):", len(clips))
print("Clips de Elara:", sum(1 for r in rows if r["tipo"] == "CLIP-ELARA"))
print("MD ->", OUT_MD)
print("CSV ->", OUT_CSV)
print("\n--- Ejemplo IMG N1 ---")
print(imgs[0]["prompt"][:160])
