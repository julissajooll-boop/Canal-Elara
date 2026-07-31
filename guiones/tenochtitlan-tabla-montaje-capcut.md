# TENOCHTITLÁN — TABLA DE MONTAJE (CapCut)
## Elara Historiadora · video ~25–26 min

> Cómo armar TODO el video, capa por capa. **La voz en off manda**: primero pones la narración,
> luego encajas cada clip a su tramo. La lista completa de tramos (198, con texto exacto y tiempos)
> está en **`tenochtitlan-timeline-montaje.md`**. Aquí va la guía de montaje y las reglas.

---

## 🗂️ LOS 3 ARCHIVOS Y PARA QUÉ SIRVEN
| Archivo | Qué es |
|---------|--------|
| `tenochtitlan-voz-en-off.md` | El guion para grabar la narración (la voz manda). |
| `tenochtitlan-desglose-clips.md` | **Biblioteca visual**: los 188 prompts (imagen+video con negativos) + fichas de personaje + 5 mapas. Es *qué generar*. |
| `tenochtitlan-timeline-montaje.md` | **Timeline**: los 198 tramos de 8 s con el texto exacto y los tiempos. Es *cuándo va cada clip y cuánto dura*. |

**Flujo:** genera las imágenes/videos de la biblioteca → graba la voz → coloca la voz en CapCut →
ve bajando por la timeline y arrastra a cada tramo el clip que corresponde a ese texto.

---

## 🎚️ ESTRUCTURA DE PISTAS EN CAPCUT (de arriba a abajo)
| Pista | Contenido |
|-------|-----------|
| Texto 2 | Títulos, rótulos (año, lugar), "Suscríbete", **subtítulos** (suben retención) |
| Texto 1 | Logo ELARA (esquina, todo el video, opacidad ~70%) |
| Video 2 | Clips de **Elara a cámara** (lip-sync) cuando aparecen |
| Video 1 | Clips de la reconstrucción (imágenes Ken Burns + videos Flow + mapas), en orden |
| Audio 1 | 🎙️ **Voz en off de Elara** (MANDA sobre todo) |
| Audio 2 | 🎵 Música de fondo (−18 a −25 dB, con ducking cuando habla Elara) |
| Audio 3 | 🔊 Efectos de sonido (ambiente de lago, mercado, tambores, boom) |

---

## ⏱️ CÓMO CUADRAR LA DURACIÓN (importante)
- Voz en off: **~25:33** · Timeline: **198 tramos × 8 s = 26:24** → cuadra (±1 min). ✅
- **Perilla de ajuste = las imágenes.** Los videos de Flow y los clips de Elara duran 8 s fijos,
  pero las imágenes con Ken Burns puedes dejarlas el tiempo que quieras. Si al montar el video te
  queda algo más largo o corto que la voz, ajusta la duración de las imágenes (entre ~7 y ~9 s)
  hasta que el último clip termine junto con la última palabra.
- Alternativa: bajar el **Speed** de la voz en ElevenLabs a 0.92–0.95 para estirar la narración.

---

## 🗣️ LOS 11 CLIPS DE ELARA A CÁMARA (lip-sync)
Elara aparece en cámara solo en momentos clave (hook, algunos remates y cierre + CTA). Son los tramos
marcados **🗣️ Elara** en la timeline (tramos 1–6 del hook, y los del cierre y la CTA). Genera esos
clips con su **imagen base de Tenochtitlán** (terracota + turquesa) y voz latina, y colócalos en la
pista Video 2. El resto del video es voz en off sobre la reconstrucción.

> Regla: lo que Elara dice a cámara es EXACTAMENTE el texto del tramo (no una versión parecida).

---

## 🎬 GUÍA DE MONTAJE POR BLOQUES (mapa rápido)
| Bloque | Tramos aprox. | Qué mostrar (de la biblioteca visual) | Música | SFX |
|--------|---------------|----------------------------------------|--------|-----|
| **HOOK** | 1–6 | Elara a cámara + calle CDMX + cimientos + ciudad-lago revelada | Tensión que sube | **BOOM** al título, rumble |
| **CONTEXTO** | 7–20 | Valle y 5 lagos (MAPA 153), volcanes, ciudad aérea, españoles asombrados, comparación de tamaño | Épica suave entra | Viento, agua, whoosh en la revelación |
| **ACTO 1 · ORIGEN** | 21–55 | MAPA peregrinación (154), Aztlán, expulsión, el águila sobre el nopal, chinampas, canoas, tributo | Misteriosa → esperanzadora | Ambiente, aleteo del águila |
| **ACTO 2 · GRANDEZA** | 56–120 | MAPA calzadas (155), calzadas y canoas, acueducto, dique, mercado de Tlatelolco, Templo Mayor, escuelas, palacio de Moctezuma, arte/estrellas/poesía | Majestuosa/cálida | Mercado bullicioso, tambor huehuetl, aves |
| **ACTO 3 · CAÍDA** | 121–175 | MAPA ruta de Cortés (156), llegada, caballos, tlaxcaltecas, la Malinche, encuentro, Noche Triste, viruela, MAPA cerco (157), bergantines, Cuauhtémoc, caída | Tensión → tragedia | Silencio tenso, agua nocturna, tambores de guerra |
| **CIERRE + CTA** | 176–198 | Ruinas dormidas, hallazgo 1978, Templo Mayor hoy, transición pasado-presente, Elara despedida | Emotiva → cierre que sube | Bocinas leves (contraste), whoosh final |

> Para el detalle tramo por tramo (texto exacto + tiempos), usa `tenochtitlan-timeline-montaje.md`.

---

## 📐 REGLAS DE ORO DEL MONTAJE
1. **La voz manda:** monta primero la narración y ajusta los clips a cada frase.
2. **Ritmo dinámico:** ~3 imágenes (Ken Burns) + 1 video de Flow por escena, para que no se sienta estático.
3. **Música siempre por debajo** (−18 a −25 dB) + ducking cuando Elara habla.
4. **Elara en pantalla solo en los 11 tramos marcados**; el resto, voz sobre reconstrucción.
5. **Transiciones:** corte seco o fundido suave por defecto; whoosh/zoom solo en momentos clave
   (revelación de la ciudad, el águila, la Noche Triste, el hallazgo de 1978, el cierre).
6. **BOOM** en 3-4 puntos fuertes: entrada del título, la aparición del águila, la palabra
   "desapareció"/Noche Triste, y el remate final.
7. **Mapas:** anímalos en CapCut con keyframes (ver `guia-mapas-animados`), no con IA de video.
8. **Logo ELARA** en esquina todo el video; **subtítulos** activados palabra por palabra.
9. **Filtro/LUT cinematográfico** parejo y cálido en todos los clips para unificar el color
   (paleta verde lago / turquesa / oro / rojo teja).

---

## 🎵 SONIDO SUGERIDO
- **Música:** ambient cinematográfico con percusión y flautas prehispánicas; sube en la grandeza,
  se vuelve tensa en la caída, y cierra emotiva. Mantener siempre bajo la voz.
- **SFX por bloque:** agua y aves (lago), multitud y regateo (mercado), tambor grave (templo),
  cañas y remos (canoas), silencio tenso + agua nocturna (Noche Triste), bocinas de ciudad muy
  leves (contraste en el cierre actual).

## 📤 EXPORTAR
- 1920×1080 (o 4K) · 24–30 fps · MP4 · calidad alta · audio −14 LUFS aprox.

## ✅ CHECKLIST FINAL ANTES DE SUBIR
- [ ] La última imagen termina junto con la última palabra de la voz.
- [ ] Ningún tramo quedó sin clip (revisar contra la timeline).
- [ ] Subtítulos en todo el video.
- [ ] Miniatura + título listos (ver `tenochtitlan-titulo-miniatura.md`).
- [ ] 2–3 Shorts ya cortados para publicar alrededor del estreno (ver `tenochtitlan-shorts.md`).
