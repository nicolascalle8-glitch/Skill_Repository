# Plantilla para una skill nueva

Copiar en `skills/<nombre>/SKILL.md` y llenar. Mantener el `SKILL.md` corto; lo largo
(tablas, ejemplos, listas de chequeo) va en `skills/<nombre>/references/`.

```markdown
---
name: nombre-en-kebab-case
description: >-
  Qué hace en una frase. Úsala cuando <disparadores concretos, con las palabras que yo
  usaría>. No sirve para <exclusiones>.
---

# Título

Para qué existe y qué resultado deja (una o dos frases).

## Antes de empezar

Qué datos necesita, qué decisión debe ayudar a tomar y qué pedir si falta algo.

## Cómo se hace

Pasos en orden. Cada paso dice qué produce.

## Salida

Qué se entrega exactamente (formato, secciones, archivos) y con qué etiquetas del contrato.

## Verificación

Cómo se comprueba que está bien antes de entregarlo.

## Límites

Qué no hace y a qué skill le pasa el trabajo cuando se sale de su alcance.
```

## Antes de marcarla activa

- [ ] Probada con un caso real (ejercicio, pieza, informe) y el resultado revisado por mí.
- [ ] Agregada a `registry/CAPACIDADES.yml` con estado `activa` y fecha.
- [ ] Agregada al catálogo del router (`skills/router-ing/references/catalogo.md`).
- [ ] No contradice `shared/CONTRATO-OPERATIVO.md` ni `CONTRATO.md`.
- [ ] Empaquetada como `.skill` e instalada en Claude.
