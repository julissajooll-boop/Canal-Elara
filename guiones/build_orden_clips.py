#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera un mapa CLIP -> FRAGMENTO DE NARRACION donde empieza cada clip.
Divide la narracion de cada escena entre sus clips (por frases), de modo que
cada clip queda anclado al texto exacto del guion donde arranca."""
import re

SRC = "/projects/sandbox/Canal-Elara/guiones/la-gran-muralla-guion-escenas.md"
OUT = "/projects/sandbox/Canal-Elara/guiones/la-gran-muralla-orden-prompts.md"
CLIP_SECS = 8

with open(SRC, encoding="utf-8") as f:
    lines = f.readlines()

acto_re = re.compile(r"^## (ACTO .+|CIERRE.*)")
escena_re = re.compile(r"^### ESCENA (\d+)(?:\s*[—-]\s*(.+))?")
narr_re = re.compile(r"^\*\*Narración:\*\*\s*(.+)$")
clip_re = re.compile(r"^- \*\*Clip (\d+)\*\*\s*·\s*(.+?)\s*·\s*(.+?)\s*·\s*\*(.+?)\*")

escenas = []
current_acto = ""
cur = None
for ln in lines:
    ma = acto_re.match(ln)
    if ma:
        current_acto = ma.group(1).strip()
        continue
    me = escena_re.match(ln)
    if me:
        cur = {"num": me.group(1), "titulo": (me.group(2) or "").strip(),
               "acto": current_acto, "narr": "", "clips": []}
        escenas.append(cur)
        continue
    mn = narr_re.match(ln)
    if mn and cur is not None:
        cur["narr"] = mn.group(1).strip().strip('"')
        continue
    mc = clip_re.match(ln)
    if mc and cur is not None:
        cur["clips"].append({"num": mc.group(1), "plano": mc.group(2).strip(),
                             "recurso": mc.group(3).strip(),
                             "emocion": mc.group(4).strip()})


def split_sentences(text):
    text = text.replace("…", "… ")
    parts = re.split(r"(?<=[\.\?\!])\s+", text)
    return [p.strip() for p in parts if p.strip()]


def distribute(narr, n):
    sents = split_sentences(narr)
    if n <= 0:
        return []
    if not sents:
        return ["(sin narración / clip visual)" for _ in range(n)]
    if len(sents) <= n:
        out = []
        for i in range(n):
            if i < len(sents):
                out.append(sents[i])
            else:
                out.append("(continúa) " + sents[-1])
        return out
    out = []
    per = len(sents) / n
    for i in range(n):
        start = round(i * per)
        end = round((i + 1) * per)
        end = max(end, start + 1)
        chunk = " ".join(sents[start:end])
        out.append(chunk)
    return out


def fmt(secs):
    return "%d:%02d" % (secs // 60, secs % 60)


md = []
md.append("# LA GRAN MURALLA — MAPA DE ORDEN DE LOS PROMPTS\n")
md.append("**Canal:** Elara Historiadora · Cada clip dura 8 s.\n")
md.append("> Este mapa indica, para cada clip, el **fragmento exacto del guion (voz en off) "
          "donde empieza**, además de su acto, escena, plano y código de tiempo (acumulado a "
          "8 s por clip). Lee de arriba hacia abajo = orden de montaje.\n")

total_clips = sum(len(e["clips"]) for e in escenas)
md.append("**Total de clips:** %d · **Duración de material:** ~%s\n"
          % (total_clips, fmt(total_clips * CLIP_SECS)))
md.append("\n---\n")

md.append("## Línea de tiempo: dónde empieza cada clip en el guion\n")
md.append("| Tiempo | Clip | Esc | Plano | 🎙️ Texto del guion donde empieza el clip |")
md.append("|--------|------|-----|-------|-------------------------------------------|")

clip_count = 0
for e in escenas:
    frags = distribute(e["narr"], len(e["clips"]))
    for c, frag in zip(e["clips"], frags):
        start = clip_count * CLIP_SECS
        clip_count += 1
        frag_md = frag.replace("|", "\\|")
        md.append("| %s | %s | %s | %s | %s |" % (
            fmt(start), c["num"], e["num"], c["plano"], frag_md))

md.append("\n---\n")

md.append("## Detalle por escena (narración completa + reparto por clip)\n")
clip_count = 0
last_acto = ""
for e in escenas:
    if e["acto"] != last_acto:
        last_acto = e["acto"]
        md.append("\n### 🎬 %s\n" % last_acto)
    md.append("\n**ESCENA %s%s**" % (
        e["num"], (" — " + e["titulo"]) if e["titulo"] else ""))
    if e["narr"]:
        md.append("\n> 🎙️ *\"%s\"*\n" % e["narr"])
    md.append("\n| Tiempo | Clip | Plano | Recurso | Emoción | 🎙️ Empieza en el texto |")
    md.append("|--------|------|-------|---------|---------|------------------------|")
    frags = distribute(e["narr"], len(e["clips"]))
    for c, frag in zip(e["clips"], frags):
        start = clip_count * CLIP_SECS
        clip_count += 1
        frag_md = frag.replace("|", "\\|")
        md.append("| %s | Clip %s | %s | %s | %s | %s |" % (
            fmt(start), c["num"], c["plano"], c["recurso"], c["emocion"], frag_md))

md.append("\n---\n")

md.append("""## 🎬 PROMPTS ESPECIALES "SIN TEXTO" — ubicación exacta

Estos prompts viven en `la-gran-muralla-intro-cinematografica.md`:

### 1) INTRO CINEMATOGRÁFICA (Cold Open) — va AL PRINCIPIO DE TODO
- **Posición:** antes del Clip 1 (0:00), como apertura.
- **Duración:** 16 s (2 clips). Cubre la narración de la ESCENA 1 y 2 (el gancho).
- **Opción A (recomendada):** reemplaza los Clips 1-4. **Opción B:** va como teaser antes del Clip 1.

### 2) "LA AMENAZA DEL NORTE" (sin texto) — empieza en la frase:
- 🎙️ *"...una amenaza que no venía de sus vecinos, sino de las estepas heladas..."* (fin ESCENA 4)
  y *"Eran los pueblos nómadas del norte."* (inicio ESCENA 5).
- **Reemplaza los Clips 15 y 16** (1:52-2:08). El Clip 17 (jinetes al galope) continúa la idea.

> 💡 Al usar un prompt "sin texto", elimina del montaje el/los clip(s) que reemplaza.

---

## Cómo usar este mapa
1. Genera cada clip con su prompt blindado de `la-gran-muralla-prompts.md` (mismo número).
2. Móntalos en el orden de la línea de tiempo (de arriba a abajo).
3. La columna "Texto del guion donde empieza el clip" te dice qué parte de la voz en off
   debe estar sonando cuando entra ese clip: úsala para sincronizar imagen y narración.
4. La intro cold open va al inicio; "la amenaza del norte" entra en los Clips 15-16.
""")

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(md) + "\n")

print("OK ->", OUT)
print("Clips mapeados:", total_clips)
print("Duracion total:", fmt(total_clips * CLIP_SECS))
e1 = escenas[2]
print("\nEjemplo Escena", e1["num"], "->", len(e1["clips"]), "clips")
for c, fr in zip(e1["clips"], distribute(e1["narr"], len(e1["clips"]))):
    print("  Clip", c["num"], "=>", fr[:70])
