#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RELLENO EXTRA (segundo lote) de Babilonia: b-roll de DETALLE/MACRO y TRANSICIONES.
Distinto al primer lote (build_babilonia_relleno.py); pensado para dar dinamismo, cubrir huecos
y sustituir clips flojos. Cada prompt viene blindado y con su sitio sugerido.
Ejecuta:  python3 build_babilonia_relleno_extra.py
"""

ANCLA = ("Babilonia neobabilónica, siglo VI a.C., Mesopotamia histórica (entre los ríos "
         "Éufrates y Tigris), arquitectura mesopotámica auténtica (muros de ladrillo de barro "
         "y betún, azulejos vidriados azul lapislázuli con relieves dorados de leones, toros y "
         "dragones, zigurat escalonado de siete pisos), túnicas y mantos mesopotámicos, barbas "
         "rizadas babilónicas.")
EST_IMG = ("Imagen fija para efecto Ken Burns. Fotorrealismo histórico cinematográfico, 8K, "
           "iluminación volumétrica cálida, gran detalle.")
EST_VID = ("Clip de video de 8 s, movimiento de cámara cinematográfico y continuidad realista. "
           "Fotorrealismo histórico, 8K, iluminación volumétrica, gran detalle.")
NEGATIVO = ("sin elementos modernos, sin ropa occidental contemporánea, sin militares modernos "
            "ni soldados occidentales, sin uniformes ni armas de fuego modernos, sin vehículos "
            "motorizados, sin edificios modernos ni rascacielos, sin banderas modernas, sin "
            "texto en inglés, sin logotipos, sin marcas de agua, sin anacronismos, sin rostros "
            "ni manos deformes, sin gore explícito.")

# (tipo, ubicación, escena) — detalle/macro y transiciones, sin repetir el primer lote
FILLERS = [
    # GRANDEZA
    ("IMG", "Bloque B3 · junto a #11–#15", "primerísimo plano de una tronera estrecha de la muralla, el viento silbando, la llanura desenfocada al fondo"),
    ("IMG", "Bloque B4 · junto a #16–#20", "macro de un azulejo azul lapislázuli con una gota de agua resbalando sobre el esmalte brillante"),
    ("VID", "Bloque B5 · junto a #21–#24", "motas de polvo flotando lentamente en un haz de luz sobre las losas de la Vía Procesional"),
    ("IMG", "Bloque B6 · junto a #25–#28", "macro del betún oscuro rezumando entre los ladrillos del zigurat, huellas de manos de obreros"),
    ("IMG", "Bloque B7 · junto a #29–#32", "PRIMER PLANO de una tablilla de arcilla con constelaciones y escritura cuneiforme, iluminada por una lámpara de aceite"),
    ("VID", "Bloque B7 · junto a #29–#32", "macro de un punzón presionando marcas en forma de cuña sobre arcilla húmeda, luz cálida"),
    ("IMG", "Bloque B8 · junto a #33–#36", "primerísimo plano del rostro dorado de la estatua de Marduc reflejando las llamas de las lámparas"),
    ("VID", "Bloque B9 · junto a #37–#40", "macro de gotas de agua sobre hojas verdes de los jardines colgantes a contraluz"),
    ("IMG", "Bloque B10 · junto a #41–#43", "manos pesando plata y granos en una balanza del mercado, macro"),

    # NABUCODONOSOR / GRIETA / NABÓNIDO
    ("IMG", "Bloque B12 · junto a #47–#49", "macro del sello real presionado sobre arcilla fresca, marca en relieve"),
    ("VID", "Bloque B13 · junto a #50–#52", "macro de un sello cuneiforme presionándose sobre un ladrillo de barro húmedo"),
    ("IMG", "Bloque B14 · junto a #53–#56", "una sola sandalia abandonada en el polvo y huellas que se alejan, tono sobrio y melancólico"),
    ("VID", "Bloque B16 · junto a #60–#62", "extreme close-up de polvo cayendo de una grieta que se ensancha lentamente en un muro"),
    ("VID", "Bloque B19 · junto a #70–#73", "un amuleto con la luna creciente del dios Sin balanceándose, destellos plateados"),
    ("VID", "Bloque B21 · junto a #77–#80", "arena barrida por el viento sobre piedras antiguas talladas del oasis de Tayma"),
    ("VID", "Bloque B22 · junto a #81–#83", "una lámpara ritual apagada con una fina voluta de humo subiendo en la penumbra"),
    ("VID", "Bloque B23 · junto a #84–#86", "primeras gotas de lluvia golpeando la tierra seca y agrietada, tormenta acercándose"),

    # CIRO / TRAICIÓN / LA NOCHE
    ("VID", "Bloque B24 · junto a #87–#90", "estandarte persa aqueménida ondeando en cámara lenta, primer plano"),
    ("VID", "Bloque B26 · junto a #94–#97", "macro de un sello de arcilla rompiéndose al abrir un mensaje secreto, manos en penumbra"),
    ("VID", "Bloque B28 · junto a #102–#104", "primer plano de una llave de bronce girando en una cerradura antigua, símbolo de la entrega"),
    ("VID", "Bloque B31 · junto a #110–#112", "paneo macro sobre las líneas de escritura cuneiforme del Cilindro de Ciro"),
    ("VID", "Bloque B33 · junto a #116–#119", "vino vertiéndose en una copa de oro en el banquete, reflejos de antorcha, cámara lenta"),
    ("VID", "Bloque B34 · junto a #120–#123", "extreme close-up de las letras luminosas formándose en el muro, leves chispas"),
    ("VID", "Bloque B36 · junto a #126–#129", "macro del agua del río retrocediendo sobre el barro y revelando piedras bajo la luna"),
    ("VID", "Bloque B37 · junto a #130–#133", "primer plano de un pie entrando en el agua hasta el tobillo bajo la muralla, ondas"),
    ("VID", "Bloque B38 · junto a #134–#136", "una puerta abierta crujiendo, la llama de una antorcha doblándose por la corriente"),

    # CIRO HEREDA / MUERTE LENTA
    ("VID", "Bloque B40 · junto a #142–#144", "pies con sandalias de Ciro pisando los azulejos azules durante la procesión, seguimiento bajo"),
    ("IMG", "Bloque B41 · junto a #145–#147", "macro de una mano cerrándose sobre la mano dorada de la estatua de Marduc"),
    ("VID", "Bloque B45 · junto a #156–#158", "la mano de Alejandro Magno rozando un ladrillo desmoronado del zigurat"),
    ("VID", "Bloque B46 · junto a #159–#161", "una corona sobre un cojín y una única vela consumiéndose, luto sobrio"),
    ("VID", "Bloque B47 · junto a #162–#164", "capitel de columna griega siendo izado con cuerdas en la construcción de Seleucia"),
    ("VID", "Bloque B48 · junto a #165–#167", "manos de un aldeano arrancando un ladrillo con inscripción de un muro, polvo cayendo"),
    ("VID", "Bloque B49 · junto a #168–#170", "un punzón rodando de la mano quieta de un anciano escriba junto a una tablilla inacabada"),

    # REDESCUBRIMIENTO / LEGADO / CIERRE
    ("VID", "Bloque B50 · junto a #171–#173", "el viento borrando huellas sobre un montículo del desierto, time-lapse suave"),
    ("VID", "Bloque B51 · junto a #174–#176", "un pincel de arqueólogo retirando el polvo de un relieve de león azul recién descubierto"),
    ("VID", "Bloque B51 · junto a #174–#176", "un foco de museo revelando lentamente el azul lapislázuli de la Puerta de Ishtar"),
    ("VID", "Bloque B54 · junto a #183–#185", "una esfera de reloj disolviéndose en símbolos de números cuneiformes"),
    ("VID", "Bloque B55 · junto a #186–#187", "la rueda del zodiaco girando lentamente sobre la silueta del zigurat"),
    ("IMG", "Bloque B56 · junto a #188–#190", "una yema de dedo recorriendo los surcos de la ley grabada en la estela negra de Hammurabi"),
    ("VID", "Bloque B57 · junto a #191–#194", "una lira colgada de un árbol junto al río al atardecer, cuerdas vibrando con el viento (salmo de Babilonia)"),
    ("VID", "Bloque B57 · junto a #191–#194", "la tablilla circular del primer mapa del mundo babilónico girando lentamente, macro"),
    ("VID", "Bloque B58 · junto a #195–#196", "el reflejo dorado de Babilonia temblando sobre el Éufrates y apagándose lentamente"),
    ("IMG", "Bloque B60 · junto a #199–#200", "polvo y arena cubriendo poco a poco un ladrillo vidriado azul caído, al atardecer"),

    # TRANSICIONES (úsalas entre secciones o para saltos de tiempo)
    ("VID", "TRANSICIÓN · entre bloques", "una tormenta de arena que barre el encuadre de lado a lado, transición entre secciones"),
    ("VID", "TRANSICIÓN · entre bloques", "la llama de una antorcha apagándose hasta el negro, corte entre bloques"),
    ("VID", "TRANSICIÓN · saltos de tiempo", "barrido de estrellas girando en time-lapse sobre la silueta del zigurat, salto temporal"),
    ("VID", "TRANSICIÓN · entre bloques", "polvo dorado flotando atravesado por un haz de luz, transición suave y cálida"),
]


def main():
    n_img = sum(1 for f in FILLERS if f[0] == "IMG")
    n_vid = sum(1 for f in FILLERS if f[0] == "VID")
    total = len(FILLERS)

    out = []
    out.append("# BABILONIA — RELLENO EXTRA (b-roll de detalle y transiciones)\n")
    out.append(f"**Canal:** Elara Historiadora · **Rellenos extra:** {total} "
               f"(🖼️ {n_img} imágenes · 🎬 {n_vid} videos)\n")
    out.append("> 🎯 Segundo lote, DISTINTO al primero (`babilonia-relleno-prompts.md`). Son planos "
               "de **detalle/macro** y **transiciones** para dar más dinamismo, cubrir huecos o "
               "sustituir clips flojos. Cada uno indica su bloque y junto a qué clips va.\n")
    out.append("> Las TRANSICIONES sirven para pasar de una sección a otra o marcar saltos de tiempo.\n")
    out.append("\n## 🚫 PROMPT NEGATIVO OBLIGATORIO (cópialo en todas las generaciones)\n")
    out.append("```\n" + NEGATIVO + "\n```\n")
    out.append("\n---\n")

    for i, (kind, ubic, escena) in enumerate(FILLERS, start=1):
        if kind == "IMG":
            tag = "🖼️ IMAGEN"
            body = f"{ANCLA} {escena}. {EST_IMG}"
        else:
            tag = "🎬 VIDEO"
            body = f"{ANCLA} {escena}. {EST_VID}"
        out.append(f"\n### RX{i} · {tag} · {ubic}\n")
        out.append("```\n" + body + "\n```\n")

    with open("babilonia-relleno-extra-prompts.md", "w", encoding="utf-8") as f:
        f.write("".join(out))
    print(f"OK · relleno extra total={total} · imagenes={n_img} · videos={n_vid}")


if __name__ == "__main__":
    main()
