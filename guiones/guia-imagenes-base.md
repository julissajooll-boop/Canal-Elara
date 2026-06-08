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
