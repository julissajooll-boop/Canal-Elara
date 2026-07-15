#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera los CLIPS/IMÁGENES DE RELLENO (b-roll) de Babilonia para completar la duración.
Tus 202 clips a 8 s ≈ 27 min; la voz en off dura ~39 min. Faltan ~93 clips de 8 s.
Estos rellenos se INSERTAN entre tus clips existentes (misma numeración de babilonia-prompts.md)
para que los visuales cubran TODA la voz en off. Cada uno viene blindado y listo para copiar.
Ejecuta:  python3 build_babilonia_relleno.py
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

# (tipo, ubicación[bloque + junto a qué clips], escena) — b-roll variado, sin repetir
FILLERS = [
    # === GRANDEZA (junto a tus clips #7–#46) ===
    ("VID", "Bloque B2 · junto a #7–#10", "caravana de mercaderes con camellos cargados acercándose por el desierto al amanecer, polvo dorado"),
    ("IMG", "Bloque B2 · junto a #7–#10", "detalle de pies con sandalias y bastones de viajeros polvorientos sobre el camino del desierto"),
    ("IMG", "Bloque B3 · junto a #11–#15", "primer plano de la textura del ladrillo de barro y betún de la muralla, juntas de brea oscura"),
    ("VID", "Bloque B3 · junto a #11–#15", "guardias babilonios con lanzas y escudos patrullando lo alto de la muralla al atardecer"),
    ("IMG", "Bloque B4 · junto a #16–#20", "detalle de un león dorado en relieve sobre azulejo azul lapislázuli, brillo vidriado"),
    ("VID", "Bloque B4 · junto a #16–#20", "manos de un artesano puliendo y colocando un azulejo vidriado azul en la puerta"),
    ("IMG", "Bloque B5 · junto a #21–#24", "pies descalzos y sandalias caminando sobre las losas pulidas de la Vía Procesional"),
    ("IMG", "Bloque B5 · junto a #21–#24", "estandartes y pendones ceremoniales de colores meciéndose sobre la avenida"),
    ("IMG", "Bloque B6 · junto a #25–#28", "detalle de los escalones gastados del zigurat con una figura humana diminuta al pie"),
    ("VID", "Bloque B6 · junto a #25–#28", "vista panorámica desde lo alto del zigurat sobre la ciudad dorada al amanecer, leve movimiento"),
    ("IMG", "Bloque B7 · junto a #29–#32", "detalle de una tablilla con números y diagramas cuneiformes junto a un cielo estrellado"),
    ("IMG", "Bloque B7 · junto a #29–#32", "lámpara de aceite iluminando el rostro concentrado de un sacerdote astrónomo de noche"),
    ("VID", "Bloque B8 · junto a #33–#36", "humo de incienso subiendo entre columnas del templo, haces de luz cálida atravesando"),
    ("IMG", "Bloque B8 · junto a #33–#36", "ofrendas de grano, dátiles y objetos de oro a los pies de la estatua de Marduc"),
    ("VID", "Bloque B9 · junto a #37–#40", "agua cayendo entre las terrazas de los jardines colgantes, plantas colgando y meciéndose"),
    ("IMG", "Bloque B9 · junto a #37–#40", "pájaros y flores entre la vegetación exuberante de los jardines colgantes"),
    ("IMG", "Bloque B10 · junto a #41–#43", "puestos del mercado con especias de colores, telas teñidas y ánforas apiladas"),
    ("IMG", "Bloque B10 · junto a #41–#43", "plano coral de rostros diversos de la multitud babilónica conversando en la plaza"),
    ("IMG", "Bloque B11 · junto a #44–#46", "sombras largas de las torres de la muralla al atardecer sobre la llanura"),
    ("VID", "Bloque B11 · junto a #44–#46", "la ciudad dorada apagándose hacia la noche mientras se encienden las primeras antorchas"),

    # === NABUCODONOSOR / LA GRIETA / NABÓNIDO (junto a #47–#86) ===
    ("IMG", "Bloque B12 · junto a #47–#49", "corona real cónica y cetro sobre un cojín de lino en el salón del trono"),
    ("IMG", "Bloque B12 · junto a #47–#49", "planos y maquetas de arcilla de construcciones sobre una mesa palaciega"),
    ("VID", "Bloque B13 · junto a #50–#52", "hileras de ladrillos con inscripción cuneiforme secándose al sol, obrero pasando"),
    ("IMG", "Bloque B14 · junto a #53–#56", "sandalias, bastones y fardos de una caravana dejados en el polvo del camino, tono sobrio"),
    ("IMG", "Bloque B14 · junto a #53–#56", "una lira antigua apoyada junto a un muro, luz melancólica de atardecer"),
    ("IMG", "Bloque B15 · junto a #57–#59", "rollos y tablillas junto al río bajo palmeras, cálamos y tinteros de escriba"),
    ("VID", "Bloque B16 · junto a #60–#62", "una grieta fina recorriendo lentamente un muro dorado, polvo desprendiéndose"),
    ("IMG", "Bloque B17 · junto a #63–#66", "pasillos de palacio en penumbra con cortinas movidas por la corriente de aire"),
    ("IMG", "Bloque B17 · junto a #63–#66", "sellos cilíndricos y tablillas de decretos sobre una mesa de piedra en penumbra"),
    ("IMG", "Bloque B18 · junto a #67–#69", "haz de luz cayendo sobre un trono vacío, motas de polvo flotando en el aire"),
    ("IMG", "Bloque B19 · junto a #70–#73", "emblema de la luna creciente del dios Sin tallado en una estela, luz plateada"),
    ("VID", "Bloque B19 · junto a #70–#73", "altar del dios lunar con humo de incienso en la noche, resplandor plateado"),
    ("IMG", "Bloque B20 · junto a #74–#76", "altar de Marduc con la lámpara apagada y las ofrendas marchitas, penumbra"),
    ("IMG", "Bloque B21 · junto a #77–#80", "dunas del desierto de Arabia bajo un sol intenso, huellas de caravana"),
    ("VID", "Bloque B21 · junto a #77–#80", "ruinas antiguas del oasis de Tayma en restauración, andamios de madera y polvo"),
    ("IMG", "Bloque B22 · junto a #81–#83", "la Vía Procesional vacía y silenciosa en día de fiesta, estandartes inmóviles"),
    ("IMG", "Bloque B22 · junto a #81–#83", "la mano dorada de la estatua de Marduc extendida sola en la penumbra del templo"),
    ("VID", "Bloque B23 · junto a #84–#86", "nubes de tormenta acumulándose en time-lapse suave sobre las montañas del este"),
    ("IMG", "Bloque B23 · junto a #84–#86", "Belsasar joven mirando por una ventana del palacio con gesto inseguro"),

    # === CIRO / LA TRAICIÓN / EL CILINDRO (junto a #87–#115) ===
    ("VID", "Bloque B24 · junto a #87–#90", "estandartes persas aqueménidas ondeando al viento sobre una llanura amplia"),
    ("IMG", "Bloque B24 · junto a #87–#90", "cascos, lanzas y escudos del ejército persa alineados, disciplina y orden"),
    ("VID", "Bloque B25 · junto a #91–#93", "Ciro devolviendo una estatua sagrada a sacerdotes de otro pueblo que se inclinan"),
    ("IMG", "Bloque B26 · junto a #94–#97", "mensajero embozado entregando una tablilla sellada en la penumbra de un templo"),
    ("IMG", "Bloque B26 · junto a #94–#97", "sacerdotes murmurando entre columnas a la luz de una única lámpara"),
    ("IMG", "Bloque B26 · junto a #94–#97", "balanza con plata y granos sobre una mesa, símbolo del cálculo mercantil"),
    ("IMG", "Bloque B27 · junto a #98–#101", "estandartes caídos en el polvo tras la batalla, siluetas a lo lejos, sin violencia explícita"),
    ("VID", "Bloque B27 · junto a #98–#101", "las puertas de una ciudad abriéndose lentamente en señal de rendición pacífica"),
    ("IMG", "Bloque B28 · junto a #102–#104", "una llave de bronce antigua en una mano en penumbra, símbolo de la ciudad entregada"),
    ("IMG", "Bloque B29 · junto a #105–#107", "almacenes del templo repletos de grano, ánforas y tesoros bajo luz cálida"),
    ("IMG", "Bloque B29 · junto a #105–#107", "tablillas de contabilidad apiladas con sellos de arcilla, archivo del templo"),
    ("IMG", "Bloque B30 · junto a #108–#109", "un sacerdote leyendo una tablilla con expresión de alivio y esperanza"),
    ("VID", "Bloque B31 · junto a #110–#112", "el Cilindro de Ciro girando lentamente sobre un pedestal, luz dramática de museo"),
    ("IMG", "Bloque B31 · junto a #110–#112", "manos de un escriba grabando un cilindro de arcilla con un punzón"),
    ("IMG", "Bloque B32 · junto a #113–#115", "multitud idealizada aclamando a un rey que entra, atmósfera de relato oficial"),

    # === LA NOCHE (junto a #116–#141) ===
    ("IMG", "Bloque B33 · junto a #116–#119", "copas y vasijas de oro sobre la mesa del banquete, reflejos de antorcha"),
    ("VID", "Bloque B33 · junto a #116–#119", "músicos y bailarinas amenizando el salón del banquete, ambiente festivo y despreocupado"),
    ("VID", "Bloque B34 · junto a #120–#123", "signos luminosos apareciendo y resplandeciendo sobre el muro del salón"),
    ("IMG", "Bloque B34 · junto a #120–#123", "rostros de comensales petrificados mirando la pared del salón"),
    ("IMG", "Bloque B35 · junto a #124–#125", "ventana del palacio con el banquete iluminado y la noche negra afuera, contraste"),
    ("VID", "Bloque B36 · junto a #126–#129", "palas y cestos de obreros junto al canal del río de noche, esfuerzo coordinado"),
    ("IMG", "Bloque B36 · junto a #126–#129", "el nivel del agua del río bajando, barro húmedo revelándose bajo la luna"),
    ("VID", "Bloque B37 · junto a #130–#133", "pisadas sigilosas en el barro del lecho del río bajo el arco de la muralla"),
    ("IMG", "Bloque B37 · junto a #130–#133", "antorchas reflejadas en el agua baja bajo el arco de la muralla, sigilo"),
    ("IMG", "Bloque B38 · junto a #134–#136", "antorchas ardiendo solas en puestos de guardia vacíos de noche"),
    ("IMG", "Bloque B38 · junto a #134–#136", "una puerta interior de la ciudad abierta de par en par, penumbra, silencio"),
    ("VID", "Bloque B39 · junto a #137–#141", "las primeras luces del amanecer extendiéndose sobre la ciudad en calma"),
    ("IMG", "Bloque B39 · junto a #137–#141", "un manto real abandonado sobre unos escalones, símbolo sobrio de Nabónido capturado"),

    # === CIRO HEREDA / LA MUERTE LENTA (junto a #142–#170) ===
    ("VID", "Bloque B40 · junto a #142–#144", "pies de la procesión de Ciro avanzando sobre los azulejos azules de la Vía Procesional"),
    ("IMG", "Bloque B40 · junto a #142–#144", "multitud a ambos lados de la Vía Procesional observando la entrada del nuevo rey"),
    ("IMG", "Bloque B41 · junto a #145–#147", "detalle de dos manos casi tocándose: la de Ciro y la mano dorada de Marduc"),
    ("VID", "Bloque B42 · junto a #148–#150", "carros ceremoniales devolviendo estatuas de dioses a sus templos"),
    ("IMG", "Bloque B42 · junto a #148–#150", "familias del exilio partiendo al amanecer con sus enseres, esperanza serena"),
    ("IMG", "Bloque B43 · junto a #151–#153", "tesoro del templo siendo inventariado por funcionarios persas, oro y objetos sagrados"),
    ("IMG", "Bloque B43 · junto a #151–#153", "estanterías de tablillas de archivo bajo la vigilancia de administradores"),
    ("VID", "Bloque B44 · junto a #154–#155", "la Vía Procesional pasando de concurrida a cada vez más vacía, time-lapse suave"),
    ("IMG", "Bloque B45 · junto a #156–#158", "Alejandro Magno contemplando el gran zigurat en ruinas con admiración"),
    ("VID", "Bloque B45 · junto a #156–#158", "obreros retirando escombros del zigurat, andamios y polvo, esperanza de reconstrucción"),
    ("VID", "Bloque B46 · junto a #159–#161", "una lámpara de aceite apagándose lentamente en un aposento en penumbra"),
    ("VID", "Bloque B47 · junto a #162–#164", "la ciudad de Seleucia en construcción junto al Tigris, columnas helenísticas"),
    ("IMG", "Bloque B48 · junto a #165–#167", "aldeanos retirando ladrillos antiguos de un muro de Babilonia para sus casas"),
    ("IMG", "Bloque B48 · junto a #165–#167", "relieves de azulejo azul agrietados y desprendidos, colores apagándose al sol"),
    ("IMG", "Bloque B49 · junto a #168–#170", "un anciano escriba solo con una tablilla entre las manos a la luz de una lámpara"),

    # === REDESCUBRIMIENTO / LEGADO / CIERRE (junto a #171–#202) ===
    ("IMG", "Bloque B50 · junto a #171–#173", "montículos de arena y tierra en el desierto iraquí bajo viento y polvo"),
    ("IMG", "Bloque B50 · junto a #171–#173", "arqueólogo de fines del siglo XIX con libreta y sombrero ante los montículos"),
    ("VID", "Bloque B51 · junto a #174–#176", "cestos y picos de excavación descubriendo poco a poco azulejos azules bajo la tierra"),
    ("IMG", "Bloque B51 · junto a #174–#176", "la Puerta de Ishtar reconstruida en un gran museo, visitantes diminutos ante ella"),
    ("IMG", "Bloque B51 · junto a #174–#176", "estanterías con miles de tablillas cuneiformes catalogadas"),
    ("IMG", "Bloque B52 · junto a #177–#179", "ladrillos modernos colocados sobre cimientos antiguos, contraste evidente"),
    ("VID", "Bloque B53 · junto a #180–#182", "vista aérea con dron del extenso sitio arqueológico de Babilonia al atardecer"),
    ("IMG", "Bloque B54 · junto a #183–#185", "esfera de reloj y engranajes con símbolos cuneiformes sutiles superpuestos"),
    ("IMG", "Bloque B55 · junto a #186–#187", "rueda del zodiaco al estilo de una tablilla babilónica sobre un cielo estrellado"),
    ("IMG", "Bloque B56 · junto a #188–#190", "detalle de las líneas de ley grabadas en la estela negra de Hammurabi"),
    ("IMG", "Bloque B57 · junto a #191–#194", "la tablilla del primer mapa del mundo babilónico, mundo circular rodeado de agua"),
    ("VID", "Bloque B58 · junto a #195–#196", "transición de las ruinas que reviven brevemente en la ciudad dorada y vuelven a ruinas"),
    ("IMG", "Bloque B60 · junto a #199–#200", "atardecer dorado sobre las ruinas de Babilonia con la silueta del zigurat"),
]


def main():
    n_img = sum(1 for f in FILLERS if f[0] == "IMG")
    n_vid = sum(1 for f in FILLERS if f[0] == "VID")
    total = len(FILLERS)

    out = []
    out.append("# BABILONIA — CLIPS E IMÁGENES DE RELLENO (b-roll)\n")
    out.append(f"**Canal:** Elara Historiadora · **Rellenos:** {total} "
               f"(🖼️ {n_img} imágenes · 🎬 {n_vid} videos)\n")
    out.append("> 🎯 Para qué: tus 202 clips a 8 s ≈ 27 min, pero la voz en off dura ~39 min. "
               "Estos rellenos completan la diferencia. Con tus 202 + estos ~93 rellenos llegas a "
               "~295 visuales de 8 s = **cubres toda la voz en off**.\n")
    out.append("> Cómo usarlos: cada relleno indica **en qué bloque va y junto a qué clips tuyos** "
               "se inserta. Son b-roll (planos de apoyo) que enriquecen y alargan cada sección "
               "sin repetir. Intercálalos entre tus clips de ese bloque.\n")
    out.append("> ⚠️ Si prefieres NO añadir relleno, la alternativa es dejar cada uno de tus 202 "
               "clips en pantalla ~11–12 s (también cuadra). El relleno da un ritmo más dinámico.\n")
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
        out.append(f"\n### R{i} · {tag} · {ubic}\n")
        out.append("```\n" + body + "\n```\n")

    with open("babilonia-relleno-prompts.md", "w", encoding="utf-8") as f:
        f.write("".join(out))
    print(f"OK · relleno total={total} · imagenes={n_img} · videos={n_vid}")


if __name__ == "__main__":
    main()
