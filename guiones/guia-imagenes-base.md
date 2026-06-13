# GUÍA — Cómo trabajar con IMÁGENES BASE (image-to-video)
**Canal:** Elara Historiadora · **Herramienta:** Omni (y similares: Veo, Seedance, Kling)

> Resuelve la duda: *"¿las imágenes son base? No sé cómo trabajar con ellas."*
> Sí: para personajes o lugares que se repiten, conviene generar primero una IMAGEN FIJA
> y usarla como punto de partida del video. Así el personaje se ve IGUAL en todos los clips.

---

## 1. Las dos formas de generar un clip

| Modo | Cómo funciona | Cuándo usarlo |
|------|----------------|---------------|
| **Texto → Video** | Solo el prompt escrito genera el video | Paisajes, tomas aéreas, multitudes, clips sin personaje recurrente |
| **Imagen base → Video** (image-to-video) | Generas/subes una **imagen fija** y la IA la anima siguiendo el prompt de video | **Personajes recurrentes** (Meng Jiang, un general), o cuando quieres controlar EXACTAMENTE la composición |

**Regla simple:**
- ¿El sujeto aparece en **un solo clip**? → Texto → Video directo.
- ¿El mismo sujeto aparece en **varios clips**? → Genera una **imagen base** y reutilízala.

---

## 2. Flujo de trabajo con imagen base (paso a paso)

1. **Genera la imagen base** con el *prompt de imagen* (en un generador de imágenes o en el
   modo imagen de tu herramienta). Hazla en alta calidad y en el encuadre que servirá de
   referencia (idealmente el rostro y vestuario bien visibles).
2. **Guarda esa imagen** (es tu "ancla" del personaje).
3. Para cada clip, en el modo **image-to-video**:
   - Sube la imagen base.
   - Escribe el *prompt de video* (el movimiento de cámara y la acción).
   - Genera. La IA animará a ESE personaje, manteniendo su rostro y ropa.
4. Si un clip necesita otro ángulo (p. ej. primer plano del llanto), genera una **segunda
   imagen base** partiendo de la primera (mismo personaje, nuevo encuadre) y úsala.

> 💡 En Omni: busca la opción "imagen de referencia" / "frame inicial" / "image to video".
> Subes la imagen ahí y el prompt de video describe solo el movimiento.

---

## 3. Continuidad entre clips (encadenar tomas)
- Para que el Clip B continúe al Clip A: usa el **último fotograma del Clip A** como imagen
  base del Clip B. Así la luz y el personaje no "saltan".
- Mantén SIEMPRE las mismas palabras de estilo (época, paleta, "fotorrealismo histórico").

---

## 4. FICHA DE PERSONAJE — Meng Jiang (para la leyenda, Clips 49–56)
Genera UNA imagen base con este prompt y reutilízala en todos sus clips:

### Prompt de IMAGEN BASE (Meng Jiang)
```
Retrato de cuerpo entero de Meng Jiang, joven mujer china de la dinastía Qin (siglo III a.C.),
unos 20 años, rostro delicado, ovalado y melancólico, piel clara, ojos oscuros tristes,
cabello negro liso recogido en un moño sencillo con una horquilla de madera. Viste una túnica
hanfu sencilla de color ocre con un manto grueso de lino para el invierno. Expresión de
tristeza serena. Fondo neutro de estudio, iluminación suave y cinematográfica, fotorrealismo
histórico, 8K, gran detalle.
[NEGATIVO: sin ropa moderna ni occidental, sin maquillaje moderno, sin rasgos no asiáticos,
sin elementos anacrónicos, sin texto, sin marcas de agua, sin manos deformes.]
```

### Cómo usarla en cada clip de la leyenda
- **Clip 49 (boda):** imagen base + "junto a su esposo bajo faroles rojos, sonriendo, plano medio".
- **Clip 50 (ruptura):** imagen base + "extendiendo la mano mientras se llevan a su esposo".
- **Clip 51 (espera):** imagen base + "asomada a la puerta mirando un camino vacío, hojas cayendo".
- **Clip 52 (travesía):** imagen base + "caminando sola por la nieve con un fardo, plano general".
- **Clip 53 (llegada):** imagen base + "diminuta al pie de la Gran Muralla, contrapicado".
- **Clip 54 (dolor):** imagen base + "de rodillas llorando frente al muro, primer plano".

> Para los planos generales (52, 53) la cara se ve pequeña, pero usar la imagen base mantiene
> el vestuario y la silueta coherentes con los primeros planos (51, 54).

---

## 5. Checklist rápido
- [ ] ¿El sujeto se repite? → usa imagen base.
- [ ] ¿Generaste la ficha de personaje una vez? → reutilízala.
- [ ] ¿Mismo estilo y época en todos los prompts? → sí.
- [ ] ¿Pegaste el prompt negativo? → siempre.
- [ ] ¿Continuidad entre clips? → usa el último fotograma como base del siguiente.



---

## 🎙️ FICHA DE PERSONAJE — ELARA (presentadora del canal)

> Elara es la anfitriona recurrente del canal. Su imagen debe ser SIEMPRE la misma en todos
> los videos. Genera UNA imagen base con la ficha y reutilízala (image-to-video) cada vez
> que aparezca. Aparece en la ESCENA 2 (Clip 7): *"Soy Elara, y hoy vamos a recorrerla de
> principio a fin. Quédate hasta el final…"*

### Concepto de look (por qué engancha)
- **Exploradora-historiadora elegante**, estilo documental cinematográfico premium.
- Mezcla de **aventurera culta** (tipo expedición arqueológica) con sofisticación.
- Presente en el lugar: aparece **sobre la Gran Muralla**, lo que conecta visualmente
  con el tema y da sensación de autoridad y cercanía.

### Vestuario y accesorios (especificación fija)
- **Abrigo / gabardina larga** color camel o tierra, elegante, ligeramente movida por el viento.
- Debajo, **suéter de punto fino** color crema o marfil.
- **Bufanda de seda** sutil en tonos cálidos (ocre/borgoña).
- **Pantalón sastre** y **botas de cuero** marrón (estética exploradora chic).
- Accesorios: **reloj clásico** de cuero, un **cuaderno de cuero** o mapa enrollado en la mano
  (opcional), pendientes discretos. Nada moderno llamativo, sin logos.
- **Cabello** suelto o semirrecogido, movido levemente por la brisa.
- Maquillaje natural, mirada cálida e inteligente, sonrisa segura.

### Prompt de IMAGEN BASE (Elara)
```
Retrato de cuerpo entero de Elara, presentadora documental: mujer latina de unos 30 años,
rostro expresivo y cálido, piel trigueña, ojos marrones inteligentes, cabello castaño ondulado
suelto movido por la brisa, sonrisa segura y cercana. Viste una gabardina larga elegante color
camel ondeando ligeramente al viento, suéter de punto fino color marfil debajo, bufanda de seda
en tonos ocre, pantalón sastre y botas de cuero marrón. Accesorios: reloj clásico de cuero,
pendientes discretos. Está de pie sobre la Gran Muralla China, con la muralla serpenteando entre
montañas brumosas al fondo, luz dorada del atardecer. Estilo: fotorrealismo cinematográfico, look
documental premium, 8K, profundidad de campo, iluminación cálida y favorecedora, gran detalle.
[NEGATIVO: sin ropa anacrónica llamativa, sin logotipos ni marcas, sin texto, sin gafas de sol,
sin elementos modernos fuera de lugar (autos, móviles), sin rasgos deformes, sin manos deformes,
sin marcas de agua.]
```

### 🎥 PROMPT DE VIDEO — Presentación de Elara (Clip 7, ~8 s)
**Narración (lo que dice):** *"Soy Elara, y hoy vamos a recorrerla de principio a fin.
Quédate hasta el final…"*
```
Usar la imagen base de Elara. Elara de pie sobre la Gran Muralla China al atardecer dorado, la
muralla serpenteando entre montañas brumosas detrás de ella. Mira directamente a cámara con una
sonrisa cálida y segura mientras habla al espectador; su gabardina camel y su cabello se mueven
suavemente con la brisa. Travelling lento de acercamiento (push-in) desde plano general a plano
medio, con ligero movimiento orbital que revela la inmensidad de la muralla a su espalda. Luz
dorada cinematográfica, partículas de polvo flotando, profundidad de campo. Atmósfera elegante,
intrigante y envolvente que invita a quedarse.

Estilo: fotorrealismo cinematográfico, look documental premium, 8K, color grading cálido,
movimiento de cámara suave y continuo, realismo absoluto.
```
- **Tipo de recurso:** reconstrucción IA con presentadora (image-to-video)
- **Plano:** plano general -> plano medio (push-in con leve órbita)
- **Objetivo emocional:** cercanía + autoridad + enganche (promesa de viaje)
- **Continuidad:** usar SIEMPRE la misma imagen base de Elara en todos sus clips.

> Aplicar el PROMPT NEGATIVO. Si el lip-sync lo hace tu herramienta de voz (no Flow), genera
> el clip con la boca hablando de forma natural y sincroniza la voz en off en edición.
> Tip de enganche: que Elara aparezca DESPUÉS del cold open (la puerta abriéndose), para que
> su entrada se sienta como "tu guía aparece para llevarte adentro de la historia".



---

## 👑 FICHA DE PERSONAJE — QIN SHI HUANG (el Primer Emperador)

> Aparece en la ESCENA 9 (Clips 33–34), ESCENA 10 (Clip 35–37) y ESCENA 17 (Clip 60, anciano
> con los elíxires). Genera UNA imagen base y reutilízala. Para el Clip 60 (vejez), genera una
> variante "anciano" partiendo de la misma cara.

### Concepto
- Primer emperador de China (dinastía Qin, 221 a.C.). **Brillante, paranoico y despiadado.**
- Imagen de **poder absoluto**: severo, imponente, mirada calculadora.

### Vestuario y accesorios (fijos)
- **Túnica imperial Qin negra con bordados dorados** de dragones (los Qin adoptaron el negro).
- **Corona imperial china (mianguan)**: tocado plano con hileras de cuentas colgantes
  (cortinas de jade) al frente.
- Cinturón de jade, mangas anchas, posible cetro o espada ceremonial.
- Barba y bigote finos y cuidados, cabello recogido bajo la corona.

### Prompt de IMAGEN BASE (Qin Shi Huang)
```
Retrato de Qin Shi Huang, primer emperador de China (dinastía Qin, siglo III a.C.), hombre de
unos 45 años, rostro severo y anguloso, mirada intensa y calculadora, barba y bigote finos
cuidados. Viste una majestuosa túnica imperial negra con bordados dorados de dragones y mangas
anchas, cinturón de jade, y una corona imperial china mianguan (tocado plano con hileras de
cuentas de jade colgando al frente). Sentado erguido en un trono imperial de madera lacada en
un salón sombrío iluminado por antorchas, estandartes negros del estado Qin al fondo. Estilo:
fotorrealismo histórico chino, 8K, iluminación de claroscuro dramático, gran detalle, poder
absoluto.
[NEGATIVO: sin militares modernos, sin ropa occidental, sin elementos anacrónicos, sin rasgos
no asiáticos, sin texto, sin logotipos, sin marcas de agua, sin manos deformes.]
```

### Variante para Clip 60 (anciano, obsesión por la inmortalidad)
```
…misma cara de Qin Shi Huang pero más anciano y demacrado, cabello y barba grises, ojos febriles
y obsesivos, observando a la luz de las velas frascos de elíxires alquímicos en una cámara
sombría. Resto igual (túnica negra y dorada). Fotorrealismo histórico chino, claroscuro, 8K.
```

### Clips donde usar la imagen base
- **Clip 33:** base + "levantándose del trono, contrapicado, antorchas, estandartes negros".
- **Clip 34:** base + "primer plano del rostro, ojos calculadores, push-in lento".
- **Clip 35:** base + "de pie en una terraza mirando las montañas del norte al amanecer".
- **Clip 37:** base + "entregando un pergamino imperial al general Meng Tian" (2 personajes).
- **Clip 60:** usar la variante anciano con los elíxires.

---

## ⚔️ FICHA DE PERSONAJE — GENERAL WU SANGUI

> Aparece en la ESCENA 39 (Clips 146–147), ESCENA 40 (Clips 150–151), ESCENA 41 (Clips 152–155)
> y ESCENA 50 (Clip 190, en la pregunta del CTA). Es el personaje del CLÍMAX (la traición).
> Genera UNA imagen base y reutilízala en todos sus clips.

### Concepto
- General Ming del siglo XVII, guardián del paso de Shanhaiguan. **Atrapado en un dilema imposible.**
- Imagen de **autoridad atormentada**: fuerte pero con conflicto interior visible.

### Vestuario y accesorios (fijos)
- **Armadura de general Ming**: armadura lamelar/de placas con escamas metálicas, hombreras
  decoradas, sobreveste (tabardo) en tonos rojo oscuro y dorado.
- **Casco de general Ming** con penacho rojo de crin y adornos metálicos.
- Capa o manto que ondea al viento, espada china (jian/dao) al cinto.
- Rostro firme, barba corta, mirada intensa y conflictuada.

### Prompt de IMAGEN BASE (Wu Sangui)
```
Retrato de cuerpo entero del general chino Wu Sangui (dinastía Ming, siglo XVII), hombre de unos
40 años, rostro firme y curtido, barba corta, mirada intensa y atormentada. Viste una imponente
armadura de general Ming: armadura lamelar de placas con escamas metálicas, hombreras decoradas,
sobreveste rojo oscuro con bordados dorados, y un casco de general Ming con penacho de crin roja
y adornos metálicos. Una capa ondea al viento; lleva una espada china al cinto. Está de pie en lo
alto de la fortaleza de Shanhaiguan, la Gran Muralla descendiendo hacia el mar al fondo, cielo
tormentoso. Estilo: fotorrealismo histórico chino, 8K, iluminación cinematográfica dramática,
gran detalle en el metal y la tela, atmósfera tensa.
[NEGATIVO: sin militares modernos, sin uniformes occidentales, sin armas de fuego modernas, sin
elementos anacrónicos, sin rasgos no asiáticos, sin texto, sin logotipos, sin marcas de agua,
sin manos deformes.]
```

### Clips donde usar la imagen base
- **Clip 146:** base + "de pie en lo alto de la fortaleza mirando el horizonte, capa al viento".
- **Clip 147:** base + "primer plano del rostro firme pero atormentado, push-in lento".
- **Clip 150:** base + "vista cenital, solo en la muralla entre dos ejércitos" (plano amplio).
- **Clip 152:** base + "rostro debatiéndose, mirando al norte y al sur, tomando su decisión".
- **Clip 153:** base + "frente a un comandante manchú sellando un pacto" (2 personajes).
- **Clip 190 (CTA):** base + "silueta dividida entre luz y sombra, simbolizando la duda moral".

> 💡 Para los clips con 2 personajes (37, 153), genera primero las dos imágenes base por separado
> y, si tu herramienta lo permite, combínalas; o genera una imagen nueva con ambos descritos juntos.
