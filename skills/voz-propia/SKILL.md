---
name: voz-propia
description: Escribe, reescribe o revisa textos que la estudiante de Física de la EIA (novia de Nick) va a presentar como suyos (informes de laboratorio, notas para exponer, ensayos, comentarios, mensajes a profesores) para que suenen a ella y no a una IA, sin cambiar datos, ecuaciones ni conclusiones. Úsala cuando ella diga "que suene a mí", "esto suena a ChatGPT", "pásalo a mi voz", o cuando otra skill de física redacte algo que ella va a firmar o decir, aunque no nombre la skill. No es para textos de Nick (voz-nick) ni para las respuestas normales de Claude.
---

# Voz propia

Los textos que ella entrega tienen que sonar a ella. El perfil está en
`references/perfil.md`; léelo completo antes de escribir.

## Primera vez: armar el perfil

Si el perfil dice "Versión 0", todavía no hay muestras. Antes de prometer que algo
"suena a ella":
1. Pídele 3–5 textos escritos por ella sin IA (un informe viejo, un ensayo, un correo
   largo, mensajes). Nada generado por IA.
2. Saca los rasgos: persona gramatical (yo/nosotros/impersonal), largo de frase,
   conectores que repite, cómo abre y cierra, qué tanto usa términos técnicos, cómo
   escribe ecuaciones y unidades, signos (punto y coma, paréntesis, comillas).
3. Llena el perfil con ejemplos cortos de sus textos, sube a "Versión 1" con fecha y
   muéstraselo para que lo confirme.

Mientras no haya perfil: español claro, frases medianas, sin las marcas de IA de la lista
"Lo que NO es ella", y avísale que todavía no está calibrado.

## Qué te pueden pedir

**A. Escribir en su voz.** Directo como ella. Los datos salen de la fuente; nunca se
inventan experiencias ni opiniones suyas.

**B. Pasar un texto a su voz.**
1. Lo que no se toca: números, unidades, incertidumbres, ecuaciones, nombres, referencias,
   términos técnicos y conclusiones.
2. Reescribe el resto con el perfil. Si un párrafo solo repite o vende, se va.

**C. Revisar si suena a ella.** Marca qué no y por qué; corrige solo eso.

## Revisión automática

```bash
python3 <ruta-de-esta-skill>/scripts/revisar_voz.py texto.md
```

Corrige lo que marque salvo citas o términos técnicos (dilo). Después la prueba humana:
¿esto lo diría ella frente al profesor?

## Cuando ella corrige un texto

Sus correcciones valen más que el perfil. Si el cambio es una regla general, propónle
agregarlo a "Correcciones" del perfil; si dice que sí, se anota con fecha y ejemplo.

## Verificación

- Datos, ecuaciones, unidades y referencias iguales al original.
- `revisar_voz.py` sin hallazgos o cada uno justificado.
- No más largo que el original sin razón.

## Límites

- No arregla errores técnicos callado: los dice aparte.
- No es la voz de Nick: no mezclar con `voz-nick`.
