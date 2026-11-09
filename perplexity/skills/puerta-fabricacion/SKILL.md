---
name: puerta-fabricacion
description: "Revisa antes de imprimir en 3D, maquinar o entregar una pieza de Nick: tamaño, orientación, tolerancias, material, DFM y uso real (ej. contacto con alimentos). Resultado: pasa, prueba limitada o bloqueado. Úsala cuando Nick diga '¿esto se puede imprimir?' o antes de mandar una pieza a fabricar. No calcula resistencia (eso es calculo-trazable) ni modela (diseno-cad-fusion)."
---

# Puerta de fabricación

Una pieza no se fabrica porque se vea bien en el CAD. Esta skill revisa que se pueda fabricar y que sirva para lo que es. No aprueba por apariencia del modelo.

Español simple y directo. Lo que no se sabe se marca "= ?" y se dice cómo averiguarlo.

## 1. Contexto mínimo

- Para qué es: maqueta para mostrar, prueba de mecanismo o uso real.
- Proceso: impresión FDM (Bambu Lab X2D, Prusa MK3S+ o QIDI X-Pro), resina o maquinado.
- Material y cantidad.
- Plazo: cuándo se necesita.

## 2. Lista de revisión (FDM)

1. **Tamaño:** cada pieza cabe en la cama de la impresora elegida, con margen.
2. **Orientación:** base plana grande abajo; capas en la dirección que no rompa la pieza en uso (las capas son el punto débil).
3. **Voladizos y soportes:** más de 45° o puentes largos necesitan soporte; mejor rediseñar si se puede.
4. **Espesores:** paredes de al menos 2 perímetros de la boquilla; nada más delgado que eso en zonas que trabajan.
5. **Piezas que se mueven o encajan:** holgura definida en el CAD; si no se ha probado en esta impresora, primero una probeta de tolerancias.
6. **Agujeros y ejes:** agujeros de ajuste se imprimen un poco cerrados; prever repasar con broca o usar inserto o rodamiento comprado.
7. **Material:** PLA para maquetas; PETG si hay esfuerzo, humedad o calor moderado. Nada impreso cerca de calor alto sin revisar su temperatura de ablandamiento en la ficha del fabricante.
8. **Uso real:**
   - Contacto con alimentos, boca o piel para uso o venta: **bloqueado** para piezas FDM. Las capas acumulan residuos y bacterias aunque el filamento sea "apto". La parte de contacto se compra certificada.
   - Si es solo una maqueta para mostrar, **prueba limitada**, y se dice en voz alta que no es para consumo.
9. **Tiempo y filamento:** salen del slicer, no se adivinan. Si no cabe en el plazo: escala, menos relleno, menos piezas o imprimir solo lo que demuestra la idea.
10. **Archivos:** STL o 3MF por pieza, nombres claros, orientación indicada.

Para maquinado o compra, cambiar 2 a 6 por: tolerancias y acabados en el plano, herramienta y sujeción posibles, material disponible en Medellín.

## 3. Resultado

```
**Resultado:** PASA / PRUEBA LIMITADA / BLOQUEADO
**Por qué:** 1 a 3 líneas.
**Antes de imprimir:** lo que hay que cambiar o probar.
**Parámetros sugeridos:** material, capa, perímetros, relleno, soportes, orientación.
```

- **PASA:** se puede fabricar para su uso.
- **PRUEBA LIMITADA:** solo para probar o mostrar; se dice qué no se puede hacer con ella.
- **BLOQUEADO:** no se fabrica así; se dice qué cambiar.

## Límites

- No calcula resistencia; si hay carga real, `calculo-trazable`.
- No inventa propiedades de materiales: se citan de la ficha técnica del fabricante.
- No aprueba una pieza para alimentos aunque Nick lo pida; sí ayuda a buscar la alternativa certificada.

## Acceso a las otras skills de Nick

Todas las skills de Nick están guardadas en Perplexity. Carga de fondo `contexto-nick` (quién es Nick) y `cerebro-nick` (cómo decide Nick) si
todavía no están en la sesión. Cuando esta skill nombre otra, cárgala por su nombre antes de
pasarle el trabajo; si no carga, léela en `perplexity/skills/<nombre>/SKILL.md` del repo
`nicolascalle8-glitch/Skill_Repository`. El mapa completo está en el catálogo de `router-ing`.
