#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extrae los prompts de imagen y video del guion por escenas y genera:
   1) una hoja limpia en Markdown (tabla) con prompts BLINDADOS
   2) un CSV listo para procesamiento en lote.

   BLINDAJE para evitar que la IA genere militares modernos/estadounidenses:
   - Prefijo de anclaje historico chino en cada prompt.
   - Sufijo de estilo con arquitectura fiel de la Gran Muralla.
   - Prompt NEGATIVO obligatorio (columna propia + bloque aparte).
   - Refuerzo de terminos ambiguos (soldados -> soldados chinos, etc.).
"""
import csv
import re

SRC = "/projects/sandbox/Canal-Elara/guiones/la-gran-muralla-guion-escenas.md"
OUT_MD = "/projects/sandbox/Canal-Elara/guiones/la-gran-muralla-prompts.md"
OUT_CSV = "/projects/sandbox/Canal-Elara/guiones/la-gran-muralla-prompts.csv"

# --- Anclajes de estilo (se aplican a TODOS los clips) ---
PREFIX = ("Gran Muralla China, antigua China imperial historica. ")

IMG_STYLE = (
    " Estilo: fotorrealismo historico chino, iluminacion cinematografica, 8K, "
    "gran detalle. Arquitectura fiel: muralla china de piedra y ladrillo gris con "
    "parapeto almenado dentado, troneras y torres de vigilancia chinas (dilou) de "
    "tejado curvo; paisaje de montanias del norte de China."
)

VID_STYLE = (
    " Estilo: fotorrealismo historico chino, movimiento de camara cinematografico, "
    "continuidad realista. Ambientacion: Gran Muralla China autentica (piedra y "
    "ladrillo gris, almenas dentadas, torres dilou de tejado curvo) en montanias "
    "del norte de China."
)

# Prompt negativo obligatorio (clave para eliminar los militares americanos)
NEGATIVE = (
    "sin militares modernos, sin soldados estadounidenses ni occidentales, "
    "sin uniformes contemporaneos ni camuflaje, sin bandera de Estados Unidos ni "
    "banderas modernas, sin cascos militares modernos, sin armas de fuego modernas "
    "(fusiles, ametralladoras, tanques, helicopteros, aviones), sin vehiculos "
    "motorizados, sin edificios modernos ni rascacielos, sin ropa occidental, "
    "sin elementos anacronicos, sin texto en ingles, sin logotipos, "
    "sin marcas de agua."
)

# --- Refuerzo de terminos ambiguos (insurance extra) ---
SUBS = [
    (r"\bSoldados\b(?! chinos)", "Soldados chinos"),
    (r"\bsoldados\b(?! chinos)", "soldados chinos"),
    (r"\bSoldado\b(?! chino)", "Soldado chino"),
    (r"\bsoldado\b(?! chino)", "soldado chino"),
    (r"\bGeneral\b(?! chino)", "General chino"),
    (r"\bgeneral\b(?! chino)", "general chino"),
    (r"\bTropas\b(?! chinas)", "Tropas chinas"),
    (r"\btropas\b(?! chinas)", "tropas chinas"),
    (r"\bCañones\b", "Cañones de bronce chinos antiguos"),
    (r"\bcañones\b", "cañones de bronce chinos antiguos"),
    (r"\bCañón\b", "Cañón de bronce chino antiguo"),
    (r"\bcañón\b", "cañón de bronce chino antiguo"),
    (r"\bEjército\b(?! chino| mongol| manch| rebelde| nómada| Qin| Han| Ming| Yuan)",
     "Ejército chino imperial"),
    (r"\bejército\b(?! chino| mongol| manch| rebelde| nómada| Qin| Han| Ming| Yuan)",
     "ejército chino imperial"),
    (r"\bArqueros\b(?! chinos| nómadas)", "Arqueros chinos"),
    (r"\barqueros\b(?! chinos| nómadas)", "arqueros chinos"),
    (r"\bArmadura\b(?! china| lamelar)", "Armadura china lamelar"),
    (r"\barmadura\b(?! china| lamelar)", "armadura china lamelar"),
]


def strengthen(text):
    for pat, rep in SUBS:
        text = re.sub(pat, rep, text)
    return text


def build_img(raw):
    return PREFIX + strengthen(raw) + IMG_STYLE


def build_vid(raw):
    return PREFIX + strengthen(raw) + VID_STYLE


with open(SRC, encoding="utf-8") as f:
    lines = f.readlines()

clip_re = re.compile(r"^- \*\*Clip (\d+)\*\*\s*·\s*(.+?)\s*·\s*(.+?)\s*·\s*\*(.+?)\*")
img_re = re.compile(r"^\s*-\s*🎨\s*Imagen:\s*(.+?)\s*$")
vid_re = re.compile(r"^\s*-\s*🎬\s*Video:\s*(.+?)\s*$")
escena_re = re.compile(r"^### ESCENA (\d+)")

rows = []
current_escena = ""
current = None

for ln in lines:
    me = escena_re.match(ln)
    if me:
        current_escena = me.group(1)
        continue
    mc = clip_re.match(ln)
    if mc:
        if current:
            rows.append(current)
        current = {
            "clip": mc.group(1),
            "escena": current_escena,
            "plano": mc.group(2).strip(),
            "recurso": mc.group(3).strip(),
            "emocion": mc.group(4).strip(),
            "imagen": "",
            "video": "",
        }
        continue
    mi = img_re.match(ln)
    if mi and current:
        current["imagen"] = mi.group(1).strip()
        continue
    mv = vid_re.match(ln)
    if mv and current:
        current["video"] = mv.group(1).strip()
        continue

if current:
    rows.append(current)

# Construir versiones blindadas
for r in rows:
    r["img_final"] = build_img(r["imagen"])
    r["vid_final"] = build_vid(r["video"])

# --- CSV ---
with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Clip", "Escena", "Duracion_s", "Plano", "Recurso", "Emocion",
                "Prompt_Imagen_Final", "Prompt_Video_Final", "Prompt_Negativo"])
    for r in rows:
        w.writerow([r["clip"], r["escena"], 8, r["plano"], r["recurso"],
                    r["emocion"], r["img_final"], r["vid_final"], NEGATIVE])

# --- Markdown ---
def esc_md(t):
    return t.replace("|", "\\|")

md = []
md.append("# LA GRAN MURALLA — Hoja de prompts BLINDADOS (lote)\n")
md.append("**Canal:** Elara Historiadora · **Clips:** %d · **Duración por clip:** 8 s\n"
          % len(rows))
md.append("> ⚠️ **IMPORTANTE — Cómo evitar que la IA genere militares modernos/estadounidenses:**\n"
          ">\n"
          "> 1. Cada prompt ya incluye el **anclaje histórico chino** y la **descripción de la arquitectura** de la muralla.\n"
          "> 2. **Pega SIEMPRE el PROMPT NEGATIVO** (ver abajo) en el campo *Negative prompt* de tu herramienta.\n"
          "> 3. Si la herramienta no tiene campo negativo, el negativo ya viene en la columna *Prompt negativo* del CSV; añádelo al final del prompt.\n")
md.append("")
md.append("## 🚫 PROMPT NEGATIVO OBLIGATORIO (cópialo en todas las generaciones)\n")
md.append("```")
md.append(NEGATIVE)
md.append("```")
md.append("")
md.append("---\n")
md.append("## Tabla de prompts\n")
md.append("| # | Esc | Plano | Recurso | Emoción | Prompt de imagen (blindado) | Prompt de video (blindado) |")
md.append("|---|-----|-------|---------|---------|------------------------------|-----------------------------|")
for r in rows:
    md.append("| %s | %s | %s | %s | %s | %s | %s |" % (
        r["clip"], r["escena"], esc_md(r["plano"]), esc_md(r["recurso"]),
        esc_md(r["emocion"]), esc_md(r["img_final"]), esc_md(r["vid_final"])))

md.append("")
md.append("---\n")
md.append("## Solo prompts de IMAGEN (uno por línea, ya blindados)\n")
md.append("```")
for r in rows:
    md.append("Clip %s: %s" % (r["clip"], r["img_final"]))
md.append("```")
md.append("")
md.append("## Solo prompts de VIDEO (uno por línea, ya blindados)\n")
md.append("```")
for r in rows:
    md.append("Clip %s: %s" % (r["clip"], r["vid_final"]))
md.append("```")

with open(OUT_MD, "w", encoding="utf-8") as f:
    f.write("\n".join(md) + "\n")

print("Clips extraidos:", len(rows))
print("MD ->", OUT_MD)
print("CSV ->", OUT_CSV)
faltan_img = [r["clip"] for r in rows if not r["imagen"]]
faltan_vid = [r["clip"] for r in rows if not r["video"]]
print("Clips sin prompt de imagen:", faltan_img or "ninguno")
print("Clips sin prompt de video:", faltan_vid or "ninguno")
# muestra de control
print("\n--- EJEMPLO Clip 1 (imagen) ---")
print(rows[0]["img_final"])
