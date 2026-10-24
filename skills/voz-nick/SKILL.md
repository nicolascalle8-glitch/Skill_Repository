---
name: voz-nick
description: >-
  Escribe, reescribe o revisa textos que Nick va a presentar como suyos para que suenen a él
  (español simple y directo, primera persona, preguntas que ordenan la idea) y no a una IA,
  sin cambiar datos ni conclusiones técnicas. Úsala cuando Nick diga "que suene a mí",
  "escríbelo como yo", "esto suena a ChatGPT", "pásalo a mi voz", o cuando escribas notas
  para exponer, textos de slides, informes, artículos, reflexiones, comentarios o mensajes
  que él va a firmar, decir o entregar, aunque no nombre la skill. Las otras skills
  (presentaciones-universidad, panel-asesores) la usan para eso. No sirve para las
  respuestas normales de Claude a Nick ni para textos de clientes o marcas con su propia voz.
---

# Voz de Nick

Nick entrega textos con su nombre: notas para exponer, slides, informes, reflexiones,
comentarios. Si suenan a IA, se nota y le resta. Esta skill hace que suenen a él, usando un
perfil sacado de textos reales suyos, y aprende de cada corrección que él hace.

El perfil está en `references/perfil.md`. Léelo completo antes de escribir. Es la fuente
única de su estilo: si otra skill o el contrato dicen algo distinto, manda el perfil y
avisas la diferencia en una línea.

## Antes de empezar

Mira qué tipo de texto es (slide, notas para exponer, documento, notas técnicas, mensaje)
y busca su fila en la tabla de calibración del perfil. Si no está claro y cambia el
resultado, pregunta solo eso.

## Qué te pueden pedir

**A. Escribir desde cero en su voz.** Escribe directo como él, con los rasgos del perfil.
Los datos salen de la fuente o de lo que Nick dio; nunca inventes para que suene mejor.

**B. Pasar un texto a su voz** (uno de IA, de otra persona o un borrador suyo).
1. Separa lo que no se toca: números, unidades, ecuaciones, nombres, citas, referencias,
   términos técnicos y conclusiones. Eso queda igual, palabra por palabra si hace falta.
2. Reescribe el resto con el perfil: quita lo de "Lo que NO es Nick", pon primera persona
   donde haya opinión, ordena con preguntas si el texto lo pide, parte las frases largas.
3. Si un párrafo existe solo para repetir o vender, se va. Más corto casi siempre es mejor.

**C. Revisar si suena a él.** Marca qué no suena a él y por qué (con la regla del perfil),
y da la versión corregida solo de esas partes.

## Revisión automática

Antes de entregar, guarda el texto en un archivo y corre:

```bash
python3 <ruta-de-esta-skill>/scripts/revisar_voz.py texto.md
```

Marca muletillas, lenguaje inflado, guiones largos, cierres tipo eslogan, tríos de
adjetivos, negritas en frases enteras y frases muy largas. Corrige lo que marque, salvo que
sea una cita textual o un término técnico (dilo). Luego haz la prueba humana: ¿esto lo
diría Nick frente al salón? Si suena a folleto o a ChatGPT, otra pasada.

No metas errores de ortografía a propósito para que "suene humano".

## Salida

- El texto, listo para copiar.
- Si reescribiste (modo B), debajo y en máximo 5 líneas: qué cambiaste y qué dejaste igual
  a propósito (datos, términos). Si el texto era largo, solo los cambios grandes.
- Nada más: sin ofrecer otras versiones salvo que las pida.

## Cuando Nick corrige un texto

Sus correcciones valen más que el perfil. Cuando cambie algo que escribiste:

1. Fíjate qué cambió y si es una regla general (por ejemplo, "no uso 'por consiguiente'")
   o algo de ese texto.
2. Si es general, proponle en una línea agregarlo a "Correcciones de Nick" del perfil.
3. Si dice que sí, agrégalo en `skills/voz-nick/references/perfil.md` del repo
   `nicolascalle8-glitch/Skill_Repository` con fecha y ejemplo, sube la versión del perfil,
   haz commit (`voz-nick: corrección de Nick — <tema>`) y entrégale el `.skill` para
   reinstalar. Deja la entrada HECHO en `proyectos/skills/BITACORA.md` (y en Drive, como dice
   `shared/BITACORA-DRIVE.md`).

Lo mismo con los puntos de "Por confirmar con Nick": si él responde uno, actualiza el perfil.

## Verificación

- Todos los números, unidades, ecuaciones, nombres y referencias del original siguen iguales.
- `revisar_voz.py` sin hallazgos, o cada hallazgo que quedó tiene su razón.
- No quedó nada de "Lo que NO es Nick".
- El texto no es más largo que el original sin una razón.

## Límites

- No cambia el sentido técnico ni las conclusiones. Si el original tiene un error técnico,
  lo dice aparte; no lo arregla callado.
- No inventa experiencias, opiniones ni datos de Nick para que el texto suene personal.
- No es para las respuestas de Claude en el chat ni para textos de marca de clientes (Arde
  La Selva, Artequino, etc.), que tienen su propia voz.
- No arma la presentación (`presentaciones-universidad`) ni evalúa la entrega
  (`panel-asesores`): solo pone la voz.
