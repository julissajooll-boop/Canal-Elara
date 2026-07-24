#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera babilonia-PENDIENTES.md: TODO el material que falta por generar (clips #132–#202 con
su prompt completo, sacados de babilonia-prompts.md) + la lista de clips de Elara que faltan.
Así la usuaria tiene en UN solo archivo lo que le queda para terminar el video.
Ejecuta:  python3 build_babilonia_pendientes.py
"""
import re

CLIPS_HECHOS = 131

NEGATIVO = ("sin elementos modernos, sin ropa occidental contemporánea, sin militares modernos "
            "ni soldados occidentales, sin uniformes ni armas de fuego modernos, sin vehículos "
            "motorizados, sin edificios modernos ni rascacielos, sin banderas modernas, sin "
            "texto en inglés, sin logotipos, sin marcas de agua, sin anacronismos, sin rostros "
            "ni manos deformes, sin gore explícito.")

ELARA_PEND = [
    ("E5", "#133", "En el lecho del río (la noche)", "Y las murallas colosales, esas por las que Babilonia se creía eterna, no sirvieron de nada."),
    ("E6", "#183", "El legado (con un reloj)", "Cada vez que miras el reloj y ves que son las ocho y cuarto…"),
    ("E7", "#198", "La lección", "Mueren cuando pierden la voluntad de ser lo que son."),
    ("E8", "#201", "Pregunta a comentarios", "Dime con sinceridad: ¿crees que las civilizaciones caen por sus enemigos… o por los suyos?"),
    ("E9", "#202", "Despedida", "Soy Elara. Nos vemos en la historia."),
]


def main():
    with open("babilonia-prompts.md", encoding="utf-8") as f:
        content = f.read()
    pat = re.compile(r"### #(\d+) · (.+?) · (.+?) · \*(.+?)\*\s*\n```\n(.*?)\n```", re.DOTALL)
    pend = []
    for m in pat.finditer(content):
        n = int(m.group(1))
        if n <= CLIPS_HECHOS:
            continue
        pend.append((n, m.group(2).strip(), m.group(3).strip(), m.group(4).strip(),
                     m.group(5).strip()))
    pend.sort(key=lambda x: x[0])

    n_img = sum(1 for p in pend if "IMAGEN" in p[1])
    n_vid = sum(1 for p in pend if "VIDEO" in p[1] and "ELARA" not in p[1])
    n_ela = sum(1 for p in pend if "ELARA" in p[1])

    out = []
    out.append("# BABILONIA — LO QUE FALTA POR GENERAR (pendientes)\n")
    out.append(f"**Canal:** Elara Historiadora · **Ya hechos:** #1–#{CLIPS_HECHOS} · "
               f"**Faltan:** #{CLIPS_HECHOS+1}–#{pend[-1][0]} ({len(pend)} clips: "
               f"🖼️ {n_img} · 🎬 {n_vid} · 👩 {n_ela})\n")
    out.append("> ✅ Esta es tu lista de PENDIENTES: genera estos y el video queda completo.\n"
               "> Cada uno trae su prompt listo para copiar. Pega el negativo aparte (abajo).\n"
               "> Recuerda: personajes recurrentes (Ciro, Nabucodonosor, Nabónido, Belsasar, "
               "Alejandro, Elara) → sube su imagen de referencia (Ingredient).\n")
    out.append("\n## 🚫 PROMPT NEGATIVO (pégalo en todas)\n```\n" + NEGATIVO + "\n```\n")
    out.append("\n---\n")

    for n, tag, bloque, mov, prompt in pend:
        out.append(f"\n### #{n} · {tag} · {bloque} · *{mov}*\n")
        out.append("```\n" + prompt + "\n```\n")

    out.append("\n---\n\n## 👩 CLIPS DE ELARA QUE FALTAN (prompts ricos en `babilonia-elara-clips-flow.md`)\n")
    out.append("| Clip | Nº | Momento | Frase que dice |\n|------|----|---------|----------------|\n")
    for eid, num, mom, line in ELARA_PEND:
        out.append(f"| {eid} | {num} | {mom} | {line} |\n")

    with open("babilonia-PENDIENTES.md", "w", encoding="utf-8") as f:
        f.write("".join(out))
    print(f"OK · pendientes={len(pend)} (img={n_img}, video={n_vid}, elara={n_ela}) + Elara E5-E9")


if __name__ == "__main__":
    main()
