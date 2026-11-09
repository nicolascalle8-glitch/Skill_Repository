# Bitácora en Drive con `gws`

El qué y el porqué están en `shared/BITACORA-DRIVE.md` del repo (léelo). Ese archivo nombra
los conectores de Claude (`read_doc`, `update_doc`, `create_file`, `read_file_content`); aquí
está lo mismo con el CLI `gws`. Carga la skill `gws-best-practices` antes del primer comando.
Los ids salen de `registry/DRIVE.yml`; no busques por nombre salvo que falte el id.

**Excepción:** `horno-vertical` no tiene copia en Drive (CONTRATO.md, sección 7). Ahí no se
escribe nada en Drive; solo `proyectos/horno-vertical/BITACORA.md` en GitHub.

## Proyecto nuevo (punto 1)

```bash
# Carpeta dentro de "Proyectos IA" (antes revisa en DRIVE.yml que no exista)
gws drive files create --json '{"name":"<proyecto>","mimeType":"application/vnd.google-apps.folder","parents":["<raiz.folder_id>"]}'
# Doc desde Markdown (contenido mínimo de BITACORA-DRIVE.md, punto 1); Drive lo convierte a Google Doc
gws drive files create --json '{"name":"Bitácora — <proyecto>","mimeType":"application/vnd.google-apps.document","parents":["<folder_id>"]}' \
  --upload /tmp/bitacora.md --upload-content-type text/markdown
```

Registra `folder_id`, `bitacora_doc_id`, `bitacora_url` (`https://docs.google.com/document/d/<id>/edit`)
y `estado: activo` en `registry/DRIVE.yml`, en el mismo commit que crea `BITACORA.md`.

## Agregar una entrada arriba (punto 2)

```bash
gws docs documents get --params '{"documentId":"<bitacora_doc_id>"}' > /tmp/doc.json
# /tmp/entrada.json: {"titulo":"AAAA-MM-DD HH:MM — Perplexity Computer (<modelo>) — <TIPO>","campos":[["Qué","…"],["Archivos","…"],["Fuentes","…"],["Verificado","…"],["Para Nick","…"],["Para la siguiente IA","…"]]}
python3 <clon>/shared/scripts/entrada_drive.py /tmp/doc.json /tmp/entrada.json > /tmp/r.json
gws docs documents batchUpdate --params '{"documentId":"<bitacora_doc_id>"}' --json "$(python3 -c "import json;r=json.load(open('/tmp/r.json'));print(json.dumps({'requests':r['requests'],'writeControl':{'requiredRevisionId':r['requiredRevisionId']}}))")"
```

- Si lo rechaza por revisión, alguien escribió en el medio: vuelve a `documents get`. Nunca
  quites `writeControl`.
- Verifica leyendo el texto: `gws drive files export --params '{"fileId":"<id>","mimeType":"text/plain"}' --output /tmp/bitacora.txt`.
- El texto debe ser idéntico al de `BITACORA.md` en GitHub.

## "En curso", "Propuestas sin respuesta" y aprobaciones (puntos 3 y 4)

Mismo `documents.batchUpdate` con `writeControl.requiredRevisionId` (sácalo de un
`documents get` fresco):

- Líneas de lista: `{"replaceAllText":{"containsText":{"text":"<línea exacta>","matchCase":true},"replaceText":"<nueva>"}}`,
  con las reglas de `shared/BITACORA-DRIVE.md`, punto 3.
- Aprobación o rechazo: `insertText` en el `endIndex - 1` del párrafo "Para la siguiente IA: …"
  de esa PROPUESTA, con `"\n✅ Aprobado por Nick — AAAA-MM-DD HH:MM"` (o `❌ Rechazado …`).
  Nunca edites el texto de la propuesta.

## Sincronizar al empezar (punto 5) y sin Drive (punto 6)

- Compara las líneas "fecha — IA — tipo" del export de texto con las de `BITACORA.md`. Lo que
  falte en GitHub se copia tal cual (commit `perplexity(<proyecto>): sincroniza bitácora desde Drive`);
  lo que falte en Drive se agrega con el paso de arriba. Nunca borres una entrada.
- Si `gws` falla o Drive no responde: trabaja solo con GitHub y anota `Drive: pendiente de copiar`.
