#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de la hoja de prompts BLINDADOS de BABILONIA (Canal Elara Historiadora).
Autoría de escenas: hecha a mano, específica y variada (regla de calidad del canal).
Este script sólo envuelve cada escena con el ANCLAJE histórico + ESTILO para dejar cada
prompt COMPLETO y listo para copiar/pegar. Ejecuta:  python3 build_babilonia_prompts.py
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

# (kind, bloque, movimiento, escena)
# kind: IMG (imagen Ken Burns) · VID (video 8s) · ELARA (video de Elara, prompt rico en babilonia-elara-clips-flow.md)
SCENES = [
    # B1 — HOOK: cayó en una noche / abrieron la puerta
    ("VID", "B1 Hook", "video 8s", "gran plano general nocturno de las murallas colosales de Babilonia iluminadas por antorchas, todo en calma y silencio bajo la luna, leve niebla al ras del río"),
    ("IMG", "B1 Hook", "zoom-in lento", "una única antorcha ardiendo en un puesto de guardia vacío sobre la muralla, nadie vigilando"),
    ("IMG", "B1 Hook", "zoom-out", "la ciudad dorada dormida vista desde el aire de noche, el gran zigurat recortado contra el cielo estrellado"),
    ("VID", "B1 Hook", "video 8s", "una gran puerta de madera y bronce de la muralla entreabriéndose lentamente desde dentro, sin nadie forzándola, luz de antorcha filtrándose por la rendija"),
    ("IMG", "B1 Hook", "paneo", "detalle de una mano abriendo el cerrojo de una puerta monumental desde el interior, penumbra"),
    ("ELARA", "B1 Hook", "video 8s", "Elara ante la Puerta de Ishtar de noche, presenta el video (hook)"),

    # B2 — La tierra entre ríos / primera visión
    ("IMG", "B2 Mesopotamia", "paneo aéreo", "vista aérea de la llanura fértil entre los ríos Éufrates y Tigris al amanecer, campos de cultivo, canales de riego brillando"),
    ("IMG", "B2 Mesopotamia", "zoom-in", "caravana de viajeros y camellos acercándose por el desierto hacia una ciudad dorada en el horizonte"),
    ("VID", "B2 Mesopotamia", "video 8s", "travelling bajo siguiendo a viajeros polvorientos que se detienen asombrados al ver por primera vez las murallas y torres de Babilonia recortadas contra el cielo"),
    ("IMG", "B2 Mesopotamia", "zoom-out", "reflejo de Babilonia dorada temblando sobre las aguas del Éufrates, como una visión irreal"),

    # B3 — Las murallas / Heródoto
    ("IMG", "B3 Murallas", "zoom-in", "murallas de Babilonia inmensas de ladrillo, con torres almenadas cada pocos pasos, escala monumental frente a personas diminutas"),
    ("VID", "B3 Murallas", "video 8s", "dos carros tirados por caballos circulando en paralelo sobre la anchura de la muralla sin rozarse, vista elevada, ritmo majestuoso"),
    ("IMG", "B3 Murallas", "paneo lateral", "hilera interminable de torres de vigilancia babilónicas sobre la muralla al atardecer dorado"),
    ("IMG", "B3 Murallas", "zoom-in", "un rollo o tablilla con caracteres griegos antiguos junto a un busto de estilo griego, evocando al historiador Heródoto describiendo la ciudad"),
    ("VID", "B3 Murallas", "video 8s", "cámara ascendente en grúa que revela la escala colosal de las murallas y, tras ellas, la ciudad viva y dorada extendiéndose"),

    # B4 — Puerta de Ishtar
    ("IMG", "B4 Ishtar", "zoom-in", "la monumental Puerta de Ishtar cubierta de azulejos azul lapislázuli con relieves dorados de dragones y toros, deslumbrante bajo el sol"),
    ("IMG", "B4 Ishtar", "detalle", "primer plano de un dragón-serpiente mushhushshu en relieve dorado sobre azulejo azul lapislázuli, textura vidriada brillante"),
    ("IMG", "B4 Ishtar", "detalle", "primer plano de un toro en relieve sobre azulejo azul, líneas de oro nítidas"),
    ("VID", "B4 Ishtar", "video 8s", "dolly-in lento cruzando el umbral de la Puerta de Ishtar, los relieves de animales pasando a ambos lados como si caminaran hacia el espectador"),
    ("ELARA", "B4 Ishtar", "video 8s", "Elara cruzando bajo la Puerta de Ishtar, roza el azulejo azul y presenta la ciudad"),

    # B5 — Vía Procesional
    ("IMG", "B5 Via", "paneo", "la Vía Procesional, amplia avenida pavimentada de piedra, flanqueada por muros con leones de azulejo azul y dorado"),
    ("IMG", "B5 Via", "detalle", "primer plano de un león caminante en relieve de azulejo, melena dorada sobre fondo azul lapislázuli"),
    ("VID", "B5 Via", "video 8s", "travelling frontal avanzando por la Vía Procesional entre las filas de leones, gente con túnicas apartándose, estandartes ceremoniales meciéndose"),
    ("IMG", "B5 Via", "zoom-out", "vista de la Vía Procesional que conduce la mirada hasta el gran zigurat al fondo"),

    # B6 — Etemenanki / Torre de Babel
    ("IMG", "B6 Zigurat", "tilt-up", "el gran zigurat Etemenanki de siete pisos escalonados elevándose hacia el cielo, escaleras monumentales, templo en la cima"),
    ("VID", "B6 Zigurat", "video 8s", "órbita aérea lenta alrededor del zigurat colosal, revelando sus siete terrazas y la ciudad extendida a sus pies"),
    ("IMG", "B6 Zigurat", "zoom-in", "peregrinos con túnicas subiendo la gran escalinata del zigurat, escala diminuta frente al monumento"),
    ("IMG", "B6 Zigurat", "paneo", "pintura conceptual del zigurat evocando la Torre de Babel entre nubes bajas, atmósfera mítica"),

    # B7 — Astrónomos en las terrazas
    ("IMG", "B7 Astronomos", "zoom-in", "sacerdotes astrónomos babilónicos de noche en la terraza alta del zigurat observando el cielo estrellado, tablillas de arcilla en las manos"),
    ("VID", "B7 Astronomos", "video 8s", "plano medio de un sacerdote grabando con un punzón símbolos cuneiformes en una tablilla de arcilla húmeda mientras señala una estrella, luz de lámpara de aceite"),
    ("IMG", "B7 Astronomos", "detalle", "tablilla de arcilla cubierta de escritura cuneiforme y diagramas de posiciones planetarias, iluminada por una lámpara"),
    ("IMG", "B7 Astronomos", "zoom-out", "cielo nocturno mesopotámico con constelaciones marcadas sobre la silueta del zigurat"),

    # B8 — Esagila / Marduk / mano del Akitu
    ("IMG", "B8 Esagila", "zoom-in", "interior del templo Esagila, columnas y muros decorados, penumbra dorada, humo de incienso"),
    ("IMG", "B8 Esagila", "zoom-in dramático", "estatua del dios Marduc recubierta de oro en el santuario, resplandor cálido de lámparas, aire solemne"),
    ("VID", "B8 Esagila", "video 8s", "ceremonia del Año Nuevo Akitu: un rey babilonio con manto ceremonial extiende su mano y toca la mano de la estatua dorada de Marduc, sacerdotes alrededor, incienso, ritmo solemne"),
    ("IMG", "B8 Esagila", "detalle", "primer plano de dos manos casi tocándose, la humana y la dorada de la estatua, simbolismo del pacto"),

    # B9 — Jardines Colgantes
    ("IMG", "B9 Jardines", "paneo", "los Jardines Colgantes: terrazas escalonadas rebosantes de árboles, palmeras y flores suspendidas sobre la ciudad seca"),
    ("VID", "B9 Jardines", "video 8s", "travelling ascendente por las terrazas verdes de los jardines colgantes, agua cayendo entre niveles, hojas meciéndose con la brisa"),
    ("IMG", "B9 Jardines", "detalle", "máquina de riego antigua con cangilones subiendo agua desde el río hacia las terrazas de los jardines"),
    ("IMG", "B9 Jardines", "zoom-out", "los jardines verdes como un oasis suspendido en contraste con la llanura árida alrededor"),

    # B10 — Población / cosmopolita
    ("VID", "B10 Ciudad", "video 8s", "travelling por un mercado babilónico abarrotado y colorido, mercaderes de muchos pueblos, telas, ánforas, especias, cambistas"),
    ("IMG", "B10 Ciudad", "zoom-in", "multitud diversa en una plaza de Babilonia, gente de distintos pueblos con vestimentas variadas conviviendo"),
    ("IMG", "B10 Ciudad", "paneo aéreo", "vista aérea de la enorme ciudad de Babilonia, barrios, canales y el río atravesándola, la mayor del mundo"),

    # B11 — indestructible... pero cayó en una noche + CTA
    ("IMG", "B11 Presagio", "zoom-in", "las murallas doradas al atardecer proyectando sombras largas, sensación de fortaleza eterna"),
    ("VID", "B11 Presagio", "video 8s", "atardecer sobre Babilonia que se apaga rápidamente hacia una noche cerrada, nubes moviéndose en time-lapse suave, presagio"),
    ("ELARA", "B11 Presagio", "video 8s", "Elara a cámara: plantea la pregunta 'cómo cayó en una noche' e invita a suscribirse"),

    # B12 — Nabucodonosor II constructor
    ("IMG", "B12 Nabu", "zoom-in", "retrato imponente de Nabucodonosor II, rey babilonio con corona cónica, barba rizada y manto bordado, mirada firme"),
    ("VID", "B12 Nabu", "video 8s", "plano medio del rey Nabucodonosor II en su trono revisando planos de construcción sobre tablillas, gesto de mando, sala palaciega dorada"),
    ("IMG", "B12 Nabu", "paneo", "obras de construcción de Babilonia: andamios de madera, obreros elevando ladrillos, la ciudad creciendo bajo su reinado"),

    # B13 — su nombre en los ladrillos
    ("IMG", "B13 Ladrillos", "detalle", "primer plano de un ladrillo de barro cocido con el nombre del rey grabado en escritura cuneiforme"),
    ("VID", "B13 Ladrillos", "video 8s", "manos de un obrero colocando un ladrillo sellado con inscripción cuneiforme en un muro recién levantado, argamasa de betún"),
    ("IMG", "B13 Ladrillos", "zoom-out", "un muro entero hecho de ladrillos idénticos, todos con la misma inscripción repetida, como una firma infinita"),

    # B14 — conquista de Jerusalén / exilio
    ("IMG", "B14 Exilio", "paneo", "columna de personas cautivas con túnicas caminando por el desierto hacia Babilonia, escoltadas, atmósfera sobria y respetuosa, sin violencia"),
    ("VID", "B14 Exilio", "video 8s", "travelling lateral sobre una larga fila de deportados avanzando cansados hacia las murallas de Babilonia al atardecer, siluetas a contraluz, tono melancólico"),
    ("IMG", "B14 Exilio", "zoom-in", "un templo lejano en llamas al fondo mientras la caravana de cautivos se aleja, humo subiendo, plano sobrio y simbólico"),
    ("IMG", "B14 Exilio", "detalle", "una lira antigua y un fardo de pertenencias en manos de un deportado, símbolo del hogar perdido"),

    # B15 — paradoja cosmopolita / escribas judíos
    ("IMG", "B15 Escribas", "zoom-in", "escribas con túnicas sentados junto a un canal de Babilonia escribiendo en rollos y tablillas bajo palmeras"),
    ("VID", "B15 Escribas", "video 8s", "plano medio de un escriba anciano redactando textos a la orilla del río, reflejo del agua, palmeras meciéndose, ambiente sereno"),
    ("IMG", "B15 Escribas", "detalle", "manos escribiendo caracteres antiguos sobre un rollo, tintero y cálamo, luz cálida"),

    # B16 — su muerte / la trampa (grieta)
    ("IMG", "B16 Grieta", "zoom-in", "un trono babilonio vacío en una sala palaciega en penumbra, un manto real abandonado sobre él"),
    ("VID", "B16 Grieta", "video 8s", "primer plano de una grieta fina abriéndose en un muro dorado de ladrillo, el polvo cayendo, metáfora del imperio agrietándose"),
    ("IMG", "B16 Grieta", "paneo", "sacerdotes y nobles reunidos en penumbra murmurando entre columnas, atmósfera de intriga palaciega"),

    # B17 — caos de sucesión / 4 reyes
    ("IMG", "B17 Sucesion", "zoom-in", "cuatro coronas o tocados reales distintos alineados sobre un paño oscuro, simbolizando cuatro reyes en pocos años"),
    ("VID", "B17 Sucesion", "video 8s", "montaje simbólico: una corona real pasando de unas manos a otras en penumbra palaciega, tensión, cambios de poder"),
    ("IMG", "B17 Sucesion", "detalle", "una daga ceremonial y un sello real sobre una mesa de piedra, penumbra, presagio de conspiración, sobrio y sin violencia"),
    ("IMG", "B17 Sucesion", "zoom-out", "salón del trono vacío y frío, luz gris entrando, sensación de inestabilidad"),

    # B18 — el vacío / entra Nabónido
    ("IMG", "B18 Vacio", "paneo", "mercado y templos de Babilonia funcionando con normalidad al amanecer, pero el palacio al fondo en sombra"),
    ("VID", "B18 Vacio", "video 8s", "plano general del salón del trono con un haz de luz cayendo sobre el asiento vacío, motas de polvo flotando, silencio"),
    ("IMG", "B18 Vacio", "zoom-in", "figura de un aristócrata de provincias, Nabónido, entrando en el salón del trono con paso dudoso"),

    # B19 — Nabónido origen / culto a Sin
    ("IMG", "B19 Nabonido", "zoom-in", "retrato de Nabónido, rey babilonio de mirada introspectiva, señalando con un cetro un símbolo de luna creciente"),
    ("IMG", "B19 Nabonido", "detalle", "símbolo del dios lunar Sin, una luna creciente, tallado en una estela de piedra"),
    ("VID", "B19 Nabonido", "video 8s", "Nabónido rindiendo culto de noche ante un altar con el emblema de la luna creciente, incienso, luz plateada, en vez de ante Marduc"),
    ("IMG", "B19 Nabonido", "paneo", "una sacerdotisa anciana (su madre) ante el santuario lunar de la ciudad de Harrán, atmósfera devota"),

    # B20 — herejía / el pueblo se siente traicionado
    ("IMG", "B20 Herejia", "zoom-in", "sacerdotes de Marduc con gesto de indignación contenida en el templo Esagila, sombras dramáticas"),
    ("VID", "B20 Herejia", "video 8s", "plano medio de sacerdotes de Marduc apartándose del altar principal desatendido, el fuego ritual apagándose, tensión religiosa"),
    ("IMG", "B20 Herejia", "detalle", "altar de Marduc con las ofrendas marchitas y la lámpara apagada, símbolo del culto descuidado"),

    # B21 — abandona la capital / oasis de Tayma
    ("IMG", "B21 Tayma", "paneo", "oasis de Tayma en el desierto de Arabia: palmeras, agua y ruinas antiguas bajo un sol intenso"),
    ("VID", "B21 Tayma", "video 8s", "travelling sobre el oasis de Tayma con la figura del rey Nabónido supervisando la restauración de un templo antiguo, obreros, polvo dorado"),
    ("IMG", "B21 Tayma", "zoom-in", "el rey solitario contemplando el desierto desde una duna, lejos de su ciudad, atmósfera melancólica"),
    ("IMG", "B21 Tayma", "zoom-out", "mapa antiguo estilizado que marca la distancia entre Babilonia y el lejano oasis de Tayma"),

    # B22 — Akitu no se celebra / mano vacía
    ("IMG", "B22 Akitu", "zoom-in", "la Vía Procesional vacía y silenciosa el día del Año Nuevo, sin desfile, estandartes quietos"),
    ("VID", "B22 Akitu", "video 8s", "plano lento del santuario de Marduc en penumbra: la mano de la estatua dorada extendida en el vacío, sin rey que la tome, motas de polvo"),
    ("IMG", "B22 Akitu", "detalle", "primer plano de la mano dorada de la estatua de Marduc sola, sin nadie que la sostenga, luz tenue"),

    # B23 — Belsasar regente / tormenta en el este
    ("IMG", "B23 Belsasar", "zoom-in", "Belsasar, joven regente, en el salón del trono con gesto inseguro, corona parcial, sin la autoridad plena de un rey"),
    ("VID", "B23 Belsasar", "video 8s", "nubes de tormenta acumulándose en el horizonte oriental sobre las montañas, viento levantando polvo, presagio de un poder que se acerca"),
    ("IMG", "B23 Belsasar", "paneo", "vista desde las murallas hacia el este, montañas lejanas bajo un cielo amenazante"),

    # B24 — Ciro el Grande asciende
    ("IMG", "B24 Ciro", "zoom-in", "retrato imponente de Ciro el Grande, rey persa aqueménida con tiara y manto real, mirada serena y poderosa"),
    ("VID", "B24 Ciro", "video 8s", "gran plano del ejército persa aqueménida en marcha ordenada por una llanura, estandartes al viento, escala épica, ritmo imparable"),
    ("IMG", "B24 Ciro", "paneo", "mapa antiguo iluminándose para mostrar la rápida expansión del imperio persa desde el mar Egeo hasta la India"),
    ("IMG", "B24 Ciro", "zoom-in", "tesoro del rey Creso de Lidia, montañas de oro y objetos preciosos, símbolo de la riqueza conquistada"),

    # B25 — política de tolerancia de Ciro
    ("IMG", "B25 Tolerancia", "zoom-in", "Ciro el Grande ante un templo de un pueblo conquistado, respetando a sus sacerdotes locales, gesto magnánimo"),
    ("VID", "B25 Tolerancia", "video 8s", "plano medio de Ciro devolviendo una estatua sagrada a sacerdotes de otro pueblo, ellos inclinándose agradecidos, luz cálida"),
    ("IMG", "B25 Tolerancia", "paneo", "pueblos diversos con sus vestimentas y dioses conviviendo bajo el estandarte persa, mosaico cultural"),

    # B26 — red de Ciro dentro de Babilonia / sacerdotes y comerciantes
    ("IMG", "B26 Red", "zoom-in", "mensajero discreto entregando una tablilla sellada a un sacerdote babilonio en la penumbra de un templo"),
    ("VID", "B26 Red", "video 8s", "plano medio de sacerdotes de Marduc leyendo en secreto un mensaje a la luz de una lámpara, miradas cómplices, intriga"),
    ("IMG", "B26 Red", "paneo", "grandes comerciantes babilónicos reunidos entre ánforas y balanzas, calculando en voz baja, ambiente de conspiración mercantil"),
    ("IMG", "B26 Red", "detalle", "una balanza con plata en un platillo, símbolo del cálculo interesado de los mercaderes"),

    # B27 — batalla de Opis / Sippar / camino abierto
    ("IMG", "B27 Opis", "paneo", "ejércitos enfrentados a lo lejos en la llanura junto al río, polvo y estandartes, plano amplio y sobrio, sin violencia explícita"),
    ("VID", "B27 Opis", "video 8s", "travelling sobre estandartes babilónicos caídos en el polvo tras la derrota de Opis, siluetas alejándose, tono sombrío y respetuoso"),
    ("IMG", "B27 Opis", "zoom-in", "las puertas de la ciudad de Sippar abriéndose sin combate ante el ejército persa, rendición pacífica"),
    ("IMG", "B27 Opis", "zoom-out", "camino despejado que serpentea a través de la llanura directo hacia las murallas de Babilonia"),

    # B28 — tesis de la traición
    ("ELARA", "B28 Traicion", "video 8s", "Elara a cámara con gesto grave: 'A Babilonia no la conquistaron. La entregaron desde dentro'"),
    ("IMG", "B28 Traicion", "zoom-in", "una llave antigua de bronce en una mano en penumbra, símbolo de la ciudad entregada"),
    ("VID", "B28 Traicion", "video 8s", "primer plano lento de una puerta interior de la muralla siendo abierta desde dentro por manos anónimas, luz de antorcha"),

    # B29 — poder económico de los sacerdotes
    ("IMG", "B29 Poder", "paneo", "el templo Esagila como centro económico: graneros llenos, campos de cultivo, sacerdotes administrando registros en tablillas"),
    ("VID", "B29 Poder", "video 8s", "travelling por almacenes del templo repletos de grano, ánforas y tesoros, escribas contando bienes, riqueza abrumadora"),
    ("IMG", "B29 Poder", "detalle", "tablillas de contabilidad del templo apiladas, sellos de arcilla, símbolo del poder de los sacerdotes"),

    # B30 — mensaje de Ciro / lo abrazan
    ("IMG", "B30 Mensaje", "zoom-in", "sacerdote babilonio leyendo con expresión de alivio y esperanza un mensaje que proclama a Ciro elegido de Marduc"),
    ("VID", "B30 Mensaje", "video 8s", "plano medio de sacerdotes asintiendo y elevando las manos en señal de bienvenida ante la idea de Ciro como liberador, luz esperanzadora"),

    # B31 — Cilindro de Ciro
    ("IMG", "B31 Cilindro", "detalle", "primer plano del Cilindro de Ciro, cilindro de arcilla cubierto de escritura cuneiforme, iluminación de museo"),
    ("VID", "B31 Cilindro", "video 8s", "órbita lenta alrededor del Cilindro de Ciro girando sobre un pedestal, la escritura cuneiforme recorriendo su superficie, luz dramática"),
    ("IMG", "B31 Cilindro", "zoom-in", "manos de un escriba babilonio grabando el cilindro de arcilla con el relato de la llegada de Ciro"),

    # B32 — propaganda que funcionó / la entregaron
    ("IMG", "B32 Propaganda", "paneo", "escena idealizada de Ciro entrando como salvador entre una multitud que lo aclama, atmósfera de relato oficial"),
    ("VID", "B32 Propaganda", "video 8s", "transición simbólica: el rostro esperanzado de la multitud que aclama a Ciro se torna pensativo al comprender lo que han entregado"),
    ("IMG", "B32 Propaganda", "zoom-out", "la ciudad dorada vista de lejos con una sombra sutil avanzando sobre ella, presagio"),

    # B33 — la noche / banquete de Belsasar
    ("IMG", "B33 Banquete", "zoom-in", "gran salón del banquete de Belsasar iluminado por antorchas, mesas rebosantes de comida y copas de oro, nobles festejando"),
    ("VID", "B33 Banquete", "video 8s", "travelling entre las mesas del banquete: músicos, risas, copas de oro alzándose, lujo despreocupado, luz cálida y festiva"),
    ("IMG", "B33 Banquete", "detalle", "copas y vasijas sagradas de oro sobre la mesa del banquete, reflejos de las antorchas"),
    ("IMG", "B33 Banquete", "zoom-in", "Belsasar en la cabecera del banquete alzando una copa, seguro y ajeno al peligro"),

    # B34 — escritura en la pared / Daniel
    ("VID", "B34 Escritura", "video 8s", "en el muro del salón, una mano luminosa e incorpórea trazando lentamente signos brillantes en arameo, los comensales paralizándose, silencio sobrecogedor"),
    ("IMG", "B34 Escritura", "zoom-in", "signos luminosos recién escritos resplandeciendo sobre el muro de azulejo, las palabras del veredicto"),
    ("IMG", "B34 Escritura", "detalle", "el rostro descompuesto de Belsasar mirando el muro, copa temblando en su mano"),
    ("VID", "B34 Escritura", "video 8s", "el profeta Daniel, anciano sereno, señalando el muro luminoso e interpretando el mensaje ante la corte muda, luz solemne"),

    # B35 — festejan mientras el mundo termina
    ("IMG", "B35 Ceguera", "zoom-out", "el banquete iluminado y despreocupado dentro del palacio mientras, fuera, la ciudad y el río se hunden en la oscuridad"),
    ("VID", "B35 Ceguera", "video 8s", "plano dividido en profundidad: en primer término el festín brillante, al fondo por una ventana la noche cerrada y silenciosa sobre la ciudad"),

    # B36 — desvío del Éufrates
    ("IMG", "B36 Rio", "paneo", "el río Éufrates atravesando Babilonia de noche bajo las murallas, reflejos de antorchas en el agua"),
    ("VID", "B36 Rio", "video 8s", "obreros persas de noche abriendo un canal lateral con palas para desviar el caudal del Éufrates, el agua empezando a fluir hacia otro cauce, esfuerzo coordinado"),
    ("IMG", "B36 Rio", "zoom-in", "el nivel del agua del río bajando lentamente, dejando al descubierto el lecho fangoso junto a la muralla"),
    ("VID", "B36 Rio", "video 8s", "primer plano del agua retrocediendo sobre el barro a la luz de la luna, revelando el paso bajo la muralla, tensión silenciosa"),

    # B37 — soldados caminan por el lecho / murallas inútiles
    ("VID", "B37 Entrada", "video 8s", "soldados persas avanzando en silencio por el lecho casi seco del río bajo el arco de la muralla, agua hasta los tobillos, sigilo, luz de luna"),
    ("IMG", "B37 Entrada", "zoom-in", "siluetas de soldados cruzando bajo la muralla por el cauce del río, reflejos tenues, atmósfera de sigilo"),
    ("IMG", "B37 Entrada", "zoom-out", "las murallas colosales intactas e inútiles mientras el peligro entra por debajo, ironía visual"),
    ("ELARA", "B37 Entrada", "video 8s", "Elara de pie en el lecho seco del río bajo la muralla, explica cómo entraron"),

    # B38 — caída pacífica / silencio
    ("IMG", "B38 Silencio", "paneo", "puestos de guardia babilónicos vacíos y silenciosos en el interior de la muralla de noche, antorchas ardiendo solas"),
    ("VID", "B38 Silencio", "video 8s", "travelling lento por una calle interior de Babilonia en silencio mientras sombras de soldados avanzan sin encontrar resistencia, puertas abiertas"),
    ("IMG", "B38 Silencio", "zoom-in", "una puerta interior de la ciudad abierta de par en par, sin guardias, penumbra"),

    # B39 — el amanecer extraño
    ("IMG", "B39 Amanecer", "zoom-in", "primer amanecer sobre Babilonia tras la caída, luz gris-dorada, la ciudad en calma pero cambiada"),
    ("VID", "B39 Amanecer", "video 8s", "habitantes babilónicos saliendo a las calles al amanecer y deteniéndose sorprendidos al ver soldados persas patrullando sus avenidas de siempre"),
    ("IMG", "B39 Amanecer", "paneo", "sacerdotes abriendo las puertas del templo de Marduc para recibir a los nuevos amos, ceremonias preparadas"),
    ("IMG", "B39 Amanecer", "detalle", "un comerciante en su puesto observando con cautela a los soldados persas, calculando el nuevo orden"),
    ("IMG", "B39 Amanecer", "zoom-out", "Nabónido capturado sin resistencia siendo conducido lejos, figura pequeña y vencida en el amanecer, plano sobrio"),

    # B40 — Ciro entra en procesión
    ("VID", "B40 Procesion", "video 8s", "Ciro el Grande entrando en Babilonia a pie en procesión por la Vía Procesional de azulejos azules, rodeado de generales, multitud observando, ritmo solemne"),
    ("IMG", "B40 Procesion", "zoom-in", "Ciro caminando con porte sereno entre los muros de leones azules, sin ostentación guerrera, casi como un babilonio más"),
    ("IMG", "B40 Procesion", "paneo", "la multitud babilónica a los lados de la Vía Procesional observando la entrada del nuevo rey, expectación"),

    # B41 — toma la mano de Marduk / legitimidad
    ("VID", "B41 Mano", "video 8s", "dentro del Esagila, Ciro extiende su mano y toma la mano de la estatua dorada de Marduc ante los sacerdotes, gesto que lo hace rey legítimo, incienso y luz cálida"),
    ("IMG", "B41 Mano", "detalle", "primer plano de la mano de Ciro tomando la mano dorada de Marduc, el pacto renovado por un extranjero"),
    ("IMG", "B41 Mano", "zoom-out", "los sacerdotes de Marduc inclinándose ante Ciro reconociéndolo como elegido del dios"),

    # B42 — restaura dioses / libera a los judíos / edicto
    ("IMG", "B42 Edicto", "paneo", "estatuas de dioses de distintos pueblos siendo devueltas a sus templos en carros ceremoniales, gesto de reconciliación"),
    ("VID", "B42 Edicto", "video 8s", "familias del exilio judío partiendo de Babilonia hacia su tierra al amanecer, esperanza en los rostros, camino abierto, tono luminoso"),
    ("IMG", "B42 Edicto", "detalle", "un pergamino y una tablilla con el decreto de Ciro autorizando el regreso de los deportados"),

    # B43 — otra cara: tesoro y archivos a Persia
    ("IMG", "B43 Botin", "zoom-in", "tesoro del templo de Babilonia siendo inventariado por funcionarios persas, oro y objetos sagrados bajo control ajeno"),
    ("VID", "B43 Botin", "video 8s", "travelling por los archivos del templo, miles de tablillas de conocimiento, mientras funcionarios persas las supervisan y trasladan"),
    ("IMG", "B43 Botin", "paneo", "escribas babilónicos trabajando ahora bajo la mirada de administradores persas, el saber fluyendo hacia otro imperio"),

    # B44 — la muerte lenta empieza
    ("IMG", "B44 Declive", "zoom-out", "Babilonia todavía habitada pero con la energía apagándose, calles menos concurridas, luz fría"),
    ("VID", "B44 Declive", "video 8s", "time-lapse suave de la Vía Procesional pasando de bulliciosa a cada vez más vacía, la vida escurriéndose"),

    # B45 — Alejandro entra, fascinado, reconstruye el zigurat
    ("IMG", "B45 Alejandro", "zoom-in", "Alejandro Magno joven con armadura helenística contemplando maravillado el gran zigurat de Babilonia"),
    ("VID", "B45 Alejandro", "video 8s", "Alejandro Magno recorriendo a caballo la Vía Procesional de Babilonia recibido por la ciudad, atmósfera de renacimiento prometido"),
    ("IMG", "B45 Alejandro", "paneo", "obreros comenzando a retirar escombros del zigurat en ruinas por orden de Alejandro, andamios, esperanza de reconstrucción"),

    # B46 — Alejandro muere 323 a.C.
    ("IMG", "B46 Muerte", "zoom-in", "aposento del palacio de Nabucodonosor en penumbra, un lecho con doseles, lámparas tenues, atmósfera solemne"),
    ("VID", "B46 Muerte", "video 8s", "plano lento y respetuoso del salón palaciego en silencio tras la muerte de Alejandro, una corona sobre un cojín, cortinas meciéndose, luto"),
    ("IMG", "B46 Muerte", "detalle", "una lámpara de aceite apagándose lentamente, símbolo sobrio del fin de una promesa, sin cuerpo, sin gore"),

    # B47 — Seleuco funda Seleucia / vacía Babilonia
    ("IMG", "B47 Seleucia", "paneo", "nueva ciudad helenística de Seleucia levantándose junto al río Tigris, arquitectura de columnas griegas, grúas de obra antiguas"),
    ("VID", "B47 Seleucia", "video 8s", "travelling que contrasta la nueva Seleucia en construcción y bulliciosa con la vieja Babilonia quedándose atrás en la distancia"),
    ("IMG", "B47 Seleucia", "zoom-in", "familias babilónicas con sus enseres partiendo de Babilonia hacia la nueva capital, éxodo silencioso"),

    # B48 — ladrillos desmontados / zigurat un montículo
    ("IMG", "B48 Ruina", "zoom-in", "aldeanos retirando ladrillos antiguos de un muro de Babilonia para usarlos en sus casas, la ciudad desmontándose pieza a pieza"),
    ("VID", "B48 Ruina", "video 8s", "time-lapse del gran zigurat desmoronándose lentamente y cubriéndose de polvo y arena hasta parecer una colina natural del desierto"),
    ("IMG", "B48 Ruina", "paneo", "los relieves de azulejo de la Vía Procesional agrietados y desprendidos, colores azules apagándose bajo el sol"),

    # B49 — muere el último escriba cuneiforme
    ("IMG", "B49 Escriba", "zoom-in", "un anciano escriba, el último que sabe leer cuneiforme, a solas a la luz de una lámpara con una tablilla entre las manos"),
    ("VID", "B49 Escriba", "video 8s", "primer plano de la mano temblorosa del anciano escriba soltando el punzón sobre una tablilla inacabada, la lámpara parpadeando, melancolía profunda"),
    ("IMG", "B49 Escriba", "detalle", "una tablilla de arcilla con signos cuneiformes cubriéndose poco a poco de polvo, el conocimiento perdiéndose"),

    # B50 — 2000 años enterrada / Koldewey 1899
    ("IMG", "B50 Olvido", "zoom-out", "solo montículos de tierra y arena en la llanura iraquí, ninguna señal de la ciudad que hubo debajo, siglos de olvido"),
    ("IMG", "B50 Koldewey", "zoom-in", "arqueólogo alemán de fines del siglo XIX con sombrero y libreta observando los montículos del desierto, año 1899"),
    ("VID", "B50 Koldewey", "video 8s", "equipo de excavación de época con picos y cestos retirando tierra bajo el sol, revelando los primeros ladrillos antiguos, expectación"),

    # B51 — excavación / Puerta de Ishtar a Berlín / tablillas
    ("VID", "B51 Excavacion", "video 8s", "travelling sobre la excavación que va descubriendo la Vía Procesional y los relieves azules de la Puerta de Ishtar bajo la tierra"),
    ("IMG", "B51 Museo", "zoom-in", "la Puerta de Ishtar reconstruida en un gran museo moderno, azul lapislázuli deslumbrante, visitantes diminutos ante ella"),
    ("IMG", "B51 Tablillas", "detalle", "decenas de miles de tablillas cuneiformes ordenadas en estantes de excavación, ventana a la vida antigua"),

    # B52 — ladrillos de Saddam / daños de Camp Alpha
    ("IMG", "B52 Reconstruccion", "paneo", "reconstrucción moderna de los muros del palacio de Babilonia con ladrillos nuevos colocados sobre los cimientos antiguos, contraste evidente"),
    ("IMG", "B52 Reconstruccion", "detalle", "un ladrillo moderno con una inscripción reciente junto a un ladrillo antiguo con cuneiforme, eco del pasado"),
    ("VID", "B52 Danos", "video 8s", "plano sobrio del sitio arqueológico con huellas de daños recientes, tierra removida, atmósfera de patrimonio herido, sin elementos militares modernos visibles"),

    # B53 — UNESCO 2019 / desafíos
    ("IMG", "B53 Unesco", "zoom-in", "el sitio arqueológico de Babilonia hoy, ruinas de ladrillo bajo el sol, cuidado y protegido, dignidad"),
    ("VID", "B53 Unesco", "video 8s", "vista aérea con dron del extenso sitio arqueológico de Babilonia actual, montículos y muros parcialmente reconstruidos, río al fondo"),
    ("IMG", "B53 Unesco", "detalle", "costra de sal blanca subiendo por un muro de ladrillo antiguo, amenaza silenciosa para las ruinas"),

    # B54 — legado: 60 min / 360°
    ("ELARA", "B54 Legado", "video 8s", "Elara a cámara junto a un reloj/esfera: 'cada vez que miras el reloj, usas a Babilonia'"),
    ("IMG", "B54 Legado", "detalle", "esfera de reloj marcando las ocho y cuarto, superpuesta sutilmente a símbolos cuneiformes de números babilónicos"),
    ("VID", "B54 Legado", "video 8s", "animación elegante de un círculo dividiéndose en 360 grados y una hora en 60 minutos, con estética de tablilla babilónica"),

    # B55 — zodiaco / horóscopo
    ("IMG", "B55 Zodiaco", "paneo", "rueda del zodiaco con sus doce constelaciones dibujada al estilo de una tablilla babilónica, cielo estrellado detrás"),
    ("VID", "B55 Zodiaco", "video 8s", "el Sol recorriendo lentamente las doce constelaciones del zodiaco sobre la silueta del zigurat, transición del día a la noche"),

    # B56 — Código de Hammurabi
    ("IMG", "B56 Hammurabi", "zoom-in", "la estela de piedra negra del Código de Hammurabi, con el relieve del rey ante el dios y filas de escritura cuneiforme"),
    ("VID", "B56 Hammurabi", "video 8s", "cámara ascendente sobre la estela de Hammurabi revelando de abajo arriba las leyes grabadas y el relieve superior, luz de museo"),
    ("IMG", "B56 Hammurabi", "detalle", "primer plano de las líneas cuneiformes de la ley grabadas en la piedra negra pulida"),

    # B57 — Biblia: Babel, diluvio/Gilgamesh, Salmo 137, mapa del mundo
    ("IMG", "B57 Biblia", "paneo", "pintura evocadora de la Torre de Babel inspirada en el zigurat, entre nubes, estilo clásico"),
    ("IMG", "B57 Gilgamesh", "detalle", "la tablilla del diluvio del poema de Gilgamesh, escritura cuneiforme, junto a la imagen de un arca antigua sobre aguas"),
    ("VID", "B57 Salmo", "video 8s", "deportados sentados junto a un canal de Babilonia con una lira colgada de un árbol, atardecer melancólico, evocando el salmo 'junto a los ríos de Babilonia'"),
    ("IMG", "B57 Mapa", "zoom-in", "el primer mapa del mundo babilónico grabado en una tablilla de arcilla, mundo circular con Babilonia en el centro rodeada de agua"),

    # B58 — ¿murió Babilonia? sigue viva
    ("IMG", "B58 Viva", "zoom-out", "superposición poética de la Babilonia dorada antigua translúcida sobre símbolos actuales (reloj, estrellas), continuidad"),
    ("VID", "B58 Viva", "video 8s", "transición cinematográfica de las ruinas de Babilonia que reviven brevemente en la ciudad dorada y vuelven a las ruinas, ciclo de memoria"),

    # B59 — lección: mueren desde dentro
    ("IMG", "B59 Leccion", "zoom-in", "una puerta monumental entreabierta desde dentro, luz al otro lado, símbolo de la civilización que se entrega a sí misma"),
    ("ELARA", "B59 Leccion", "video 8s", "Elara a cámara, reflexión: las civilizaciones mueren cuando pierden la voluntad de ser lo que son"),

    # B60 — el nombre vive / cierre
    ("IMG", "B60 Nombre", "paneo", "la palabra 'Babilonia' evocada en luz dorada sobre la silueta de las ruinas al atardecer, sin texto legible, atmósfera épica"),
    ("VID", "B60 Nombre", "video 8s", "atardecer dorado sobre las ruinas de Babilonia con la silueta del zigurat, luz cálida bañando los ladrillos milenarios, emoción serena"),

    # B61 — CTA
    ("ELARA", "B61 CTA", "video 8s", "Elara despedida entre las ruinas al atardecer, pregunta a comentarios e invita a suscribirse"),
    ("ELARA", "B61 CTA", "video 8s", "Elara cierre de marca: 'Soy Elara. Nos vemos en la historia'"),
]


def main():
    n_img = sum(1 for s in SCENES if s[0] == "IMG")
    n_vid = sum(1 for s in SCENES if s[0] == "VID")
    n_ela = sum(1 for s in SCENES if s[0] == "ELARA")
    total = len(SCENES)

    out = []
    out.append("# BABILONIA — HOJA DE PROMPTS BLINDADOS (lote)\n")
    out.append(f"**Canal:** Elara Historiadora · **Imágenes:** {n_img} · "
               f"**Clips de video:** {n_vid} · **Clips de Elara:** {n_ela} · "
               f"**Total:** {total} prompts\n")
    out.append("> Anclaje histórico mesopotámico + estilo + negativo aplicados automáticamente. "
               "Imágenes = efecto Ken Burns; Clips = video 8 s. Los clips 🎬 (ELARA) tienen su "
               "prompt de video RICO en `babilonia-elara-clips-flow.md` (subir siempre "
               "`elara-avatar-referencia.jpg` como Ingredient).\n")
    out.append("\n## 🚫 PROMPT NEGATIVO OBLIGATORIO (cópialo en todas las generaciones)\n")
    out.append("```\n" + NEGATIVO + "\n```\n")
    out.append("\n---\n")
    out.append("\n## 📋 PROMPTS EN ORDEN DE MONTAJE\n")
    out.append("> Cada prompt está en su propio bloque, COMPLETO, para copiarlo de un clic. "
               "El número (#) es el orden de montaje. Pega el negativo aparte.\n")

    for i, (kind, bloque, mov, escena) in enumerate(SCENES, start=1):
        if kind == "IMG":
            tag = "🖼️ IMAGEN"
            body = f"{ANCLA} {escena}. {EST_IMG}"
        elif kind == "VID":
            tag = "🎬 VIDEO"
            body = f"{ANCLA} {escena}. {EST_VID}"
        else:  # ELARA
            tag = "🎬 VIDEO (ELARA)"
            body = (f"ELARA (subir imagen base `elara-avatar-referencia.jpg` como Ingredient; "
                    f"vestuario Babilonia: blusa crema, chaqueta rosa palo, pañuelo azul "
                    f"lapislázuli, zapatos de tacón de aguja de punta fina color nude). {ANCLA} "
                    f"{escena}. Ver prompt de video rico y su línea "
                    f"hablada en `babilonia-elara-clips-flow.md`. {EST_VID}")
        out.append(f"\n### #{i} · {tag} · {bloque} · *{mov}*\n")
        out.append("```\n" + body + "\n```\n")

    with open("babilonia-prompts.md", "w", encoding="utf-8") as f:
        f.write("".join(out))
    print(f"OK · total={total} · imagenes={n_img} · videos={n_vid} · elara={n_ela}")


if __name__ == "__main__":
    main()
