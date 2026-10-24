# Bitácora en Google Drive

Cada proyecto tiene su bitácora en **dos lugares con las mismas entradas**:

- GitHub: `proyectos/<proyecto>/BITACORA.md` → guarda el historial de versiones (commits).
- Google Drive: `Proyectos IA / <proyecto> / Bitácora — <proyecto>` (Google Doc) → para leerla
  fácil desde cualquier lado, y para que Gemini (que vive en Google) la lea y escriba directo.

Los ids de carpetas y documentos están en `registry/DRIVE.yml`. Úsalos; no busques por nombre
salvo que falte el id.

Herramientas: conectores de Google Drive y Google Docs. Antes de la primera escritura en un
Doc, carga la skill `google-workspace` (reglas de posiciones y revisiones).

## 1. Proyecto nuevo

1. Crea la carpeta `<proyecto>` dentro de la raíz (`create_file`, mimeType de carpeta,
   `parentId` = `raiz.folder_id`). Antes, revisa en DRIVE.yml que no exista ya.
2. Crea el documento `Bitácora — <proyecto>` dentro de esa carpeta subiendo Markdown
   (`contentMimeType: text/markdown`), con este contenido mínimo:

   ```
   # BITÁCORA — <Nombre del proyecto>

   Reglas: CONTRATO.md del repo Skill_Repository. Entradas nuevas arriba. Nada se borra. Esta bitácora es la misma que proyectos/<proyecto>/BITACORA.md en GitHub.

   ## En curso

   - (nada)

   ## Propuestas sin respuesta

   - (ninguna)

   ## Entradas
   ```
   Drive lo convierte a Google Doc con títulos reales.
3. Agrega el proyecto a `registry/DRIVE.yml` con `folder_id`, `bitacora_doc_id`, `bitacora_url`
   y `estado: activo`, en el mismo commit que crea `proyectos/<proyecto>/BITACORA.md`.

## 2. Agregar una entrada (arriba, debajo de "Entradas")

1. `read_doc` del documento y guarda el resultado a un archivo (si la app ya lo guardó, usa esa ruta).
2. Escribe la entrada en un JSON:
   `{"titulo": "AAAA-MM-DD HH:MM — <IA> — <TIPO>", "campos": [["Qué","…"],["Archivos","…"],["Fuentes","…"],["Verificado","…"],["Para Nick","…"],["Para la siguiente IA","…"]]}`
3. `python3 shared/scripts/entrada_drive.py <read_doc.json> <entrada.json>` → imprime
   `requiredRevisionId` y `requests`.
4. `update_doc` con esos `requests` y `writeControl.requiredRevisionId`. Si lo rechaza por
   revisión, vuelve al paso 1 (alguien escribió en el medio); nunca quites el control.
5. Verifica con `read_file_content` que la entrada quedó arriba y completa.

El texto de la entrada debe ser **idéntico** al de `BITACORA.md` en GitHub.

## 3. "En curso" y "Propuestas sin respuesta"

Son líneas de lista cortas. Para cambiarlas usa `replaceAllText` con la línea exacta:
- Agregar cuando dice "(nada)" / "(ninguna)": reemplaza ese texto por la línea nueva.
- Agregar cuando ya hay líneas: reemplaza la última línea por `<última línea>\n<línea nueva>`
  (queda en la misma lista).
- Quitar: reemplaza la línea por "(nada)" si era la única; si no, por texto vacío y luego
  revisa que no quede una viñeta vacía.

## 4. Aprobación o rechazo de Nick

Debajo del último campo de la PROPUESTA ("Para la siguiente IA: …"), inserta un párrafo
`✅ Aprobado por Nick — AAAA-MM-DD HH:MM` o `❌ Rechazado por Nick — AAAA-MM-DD HH:MM — <razón>`.
Busca la posición con `read_doc` (el `endIndex` del párrafo de ese campo) y usa el control de
revisión. Nunca edites el texto de la propuesta.

## 5. Sincronizar al empezar

Antes de trabajar en un proyecto, compara los títulos de entrada (las líneas
"fecha — IA — tipo") de Drive (`read_file_content`) con los de `BITACORA.md`:

- Una entrada que está en Drive y no en GitHub (por ejemplo, la escribió Gemini directo en el
  Doc): cópiala tal cual a `BITACORA.md`, en su lugar por fecha, y haz commit
  `claude(<proyecto>): sincroniza bitácora desde Drive`.
- Una que está en GitHub y no en Drive: agrégala a Drive con el paso 2.
- Nunca borres una entrada de ninguno de los dos lados.

## 6. Si Drive no está disponible

Trabaja solo con GitHub y anota en la entrada: `Drive: pendiente de copiar`. La próxima vez que
haya conexión, la sincronización del punto 5 la copia.
