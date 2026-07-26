# REGLAS DE PRODUCCIÓN DE GUIONES — Canal Elara Historiadora
*(Aplicar SIEMPRE en todos los proyectos/guiones nuevos.)*

## ⏱️ 1. DURACIÓN DEL GUION: 25 MINUTOS
- Todo guion se diseña para durar **25 minutos**.
- Puede **pasarse hasta ~5 minutos** (25–30 min está bien). Nunca quedarse corto.
- Objetivo de voz en off: **~3.700–4.500 palabras** de narración.
- Desglose de clips que cubra TODA la narración (~185+ clips de 8 s).
- Rellenar con MÁS historias humanas reales y documentadas, nunca con paja.
> Nota: la usuaria indicó "25" como duración objetivo del guion (se interpreta en MINUTOS,
> coherente con el estándar del canal). Confirmar si en algún caso se refiere a otra unidad.

## 🎨 2. FORMATO DE LOS PROMPTS: completos y listos para copiar/pegar
Cada prompt de imagen debe entregarse COMPLETO, con todo incluido en el mismo bloque:
1. **Anclaje histórico** (época, lugar, contexto, vestimenta/arquitectura auténticas).
2. **La escena concreta** del plano.
3. **El estilo** (fotorrealismo cinematográfico, 8K, luz cálida, detalle).
4. **El negativo** (sin anacronismos, sin texto, sin logos, sin marcas de agua, sin
   rostros/manos deformes, sin gore, etc.).
- Para clips animados (🎬): añadir además el **prompt de VIDEO** (movimiento de cámara).
- Presentarlos en bloques de código para copiar y pegar tal cual, sin que la usuaria tenga
  que montar el anclaje/estilo/negativo por su cuenta.

## 🧩 3. NO REHACER lo que ya existe
- Si la usuaria ya tiene material (voz en off, clips de Elara), AÑADIR sobre eso, nunca
  reescribir ni sustituir sin permiso.

## ⭐ 4. CALIDAD (prioridad alta)
- Guiones con narrativa rica, emotiva y con datos reales bien contrastados.
- Prompts visuales específicos y variados (evitar descripciones genéricas o repetidas).
- Coherencia entre voz en off, guion gráfico y montaje.
- Antes de dar por terminado, revisar que todo encaje y tenga el nivel del canal.



## 👩‍🏫 5. ELARA COMO GUÍA INMERSIVA (estilo del canal)
- Elara debe APARECER e INTERACTUAR dentro de las escenas, caminando por las calles, los
  lugares y entre las personas de las que se está hablando, como una TURISTA / GUÍA que lleva
  al espectador de la mano por el pasado (estilo Chloe VS History, pero cinematográfico).
- Puede caminar, señalar, observar de cerca, reaccionar, agacharse a mirar objetos, pasar
  entre los personajes históricos. Su voz narra (voz en off) mientras la vemos recorrer el lugar.
- Sigue siendo la presentadora MODERNA (nunca ropa de época). Vestuario según el guion
  (Egipto: blusa blanca + chaqueta azul). Usar siempre su imagen de referencia para la cara.
- Estos clips de Elara-guía son SIEMPRE video animado (camina/gesticula) e incluyen prompt de
  imagen + prompt de video.

## 🎬 6. FORMATO OBLIGATORIO DE CADA CLIP
Cada clip del guion gráfico se entrega SIEMPRE con:
1. **PROMPT DE IMAGEN** completo (anclaje + escena + estilo + negativo).
2. **PROMPT DE VIDEO** (movimiento de cámara y acción), aunque sea imagen con Ken Burns.
Prompts ricos y variados: definir encuadre, óptica, luz, atmósfera, color y emoción.

### 🚫 6.1 El NEGATIVO va DENTRO del mismo bloque (no aparte)
- El prompt negativo se escribe **DENTRO del mismo bloque de código** del prompt de imagen y,
  otra vez, **DENTRO del mismo bloque** del prompt de video, como última línea con la etiqueta
  `Negativo: ...`. Así cada bloque se copia de UNA sola vez, completo.
- NO poner el negativo en un bloque de código separado debajo del prompt (esa forma antigua queda
  anulada por preferencia de la usuaria). Un clip = 2 bloques copiables (imagen y video), cada uno
  con su negativo incluido al final.


## 🧬 7. IMÁGENES DE REFERENCIA DE PERSONAJES (Ingredient de Flow) — OBLIGATORIO
Todo PERSONAJE que aparezca en MÁS DE UN clip debe tener **una imagen de referencia fija** (un
retrato) para mantener el mismo rostro, peinado, tocado/corona y vestuario en TODO el video.

**Flujo obligatorio (aplicar SIEMPRE):**
1. Generar PRIMERO el retrato de cada personaje recurrente (3-4 versiones, elegir 1).
2. Guardarlo (ej. `ref-<nombre>.jpg`) y subirlo como 🧬 **Ingredient / referencia de personaje**
   en Flow en TODOS los clips donde aparezca ese personaje.
3. El retrato de referencia se genera con: fondo neutro y sencillo, iluminación suave de estudio,
   vista frontal y de 3/4, expresión neutra, rostro nítido y consistente (+ anclaje histórico,
   vestuario de época y negativo, todo dentro del mismo bloque, según la regla 6.1).

**Al entregar el paquete de un guion, incluir SIEMPRE un archivo `*-personajes-referencia.md`** que
liste: qué personajes necesitan referencia, su prompt de retrato y **en qué números de clip** se sube
como Ingredient.

**Quién SÍ necesita referencia:** protagonistas y personajes históricos recurrentes (los que salen en
≥2 clips) y la presentadora Elara (que ya tiene `elara-avatar-referencia.jpg`).

**Quién NO necesita referencia:**
- Extras y multitudes (sirvientes, soldados, mercaderes, peregrinos, dolientes, sacerdotes de fondo…):
  pueden salir distintos en cada clip sin romper la continuidad.
- Figuras sagradas cuyo rostro NO se muestra (p. ej. Jesús): no se genera referencia; se filman de
  espaldas, de perfil lejano o fuera de foco, sin halos ni cruces (anacrónicos según la época).
