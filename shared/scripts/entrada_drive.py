#!/usr/bin/env python3
"""Arma el batch de Google Docs para agregar una entrada de bitácora arriba.

Uso:
  python3 entrada_drive.py <read_doc.json> <entrada.json>  > requests.json

<read_doc.json>  resultado completo de read_doc del documento de bitácora (guardado a archivo).
<entrada.json>   {"titulo": "2026-10-24 18:10 — Claude Opus 5.5 — HECHO",
                  "campos": [["Qué", "..."], ["Archivos", "..."], ...]}

Imprime {"requiredRevisionId": ..., "requests": [...]}. La entrada queda justo debajo del
título "Entradas" (la más nueva arriba): el título como Heading 3 y cada etiqueta en negrita.
"""
import json
import sys


def utf16_len(s):
    return len(s.encode("utf-16-le")) // 2


def cargar_doc(path):
    data = json.load(open(path, encoding="utf-8"))
    doc = data.get("content", data)
    tab = doc["tabs"][0]["documentTab"] if "tabs" in doc else doc
    return doc.get("revisionId"), tab["body"]["content"]


def indice_entradas(body):
    for el in body:
        p = el.get("paragraph")
        if not p:
            continue
        texto = "".join(e.get("textRun", {}).get("content", "") for e in p["elements"]).strip()
        if texto == "Entradas" and p["paragraphStyle"].get("namedStyleType", "").startswith("HEADING"):
            return el["endIndex"]
    sys.exit("No encontré el título 'Entradas' en el documento.")


def construir(revision, inicio, entrada):
    lineas = [entrada["titulo"]] + [f"{k}: {v}" for k, v in entrada["campos"]]
    texto = "\n".join(lineas) + "\n"
    req = [{"insertText": {"location": {"index": inicio}, "text": texto}}]

    pos = inicio
    fin_titulo = pos + utf16_len(lineas[0]) + 1
    req.append({"updateParagraphStyle": {
        "range": {"startIndex": pos, "endIndex": fin_titulo},
        "paragraphStyle": {"namedStyleType": "HEADING_3"},
        "fields": "namedStyleType"}})
    cuerpo_ini = fin_titulo
    cuerpo_fin = inicio + utf16_len(texto)
    # El texto insertado hereda el estilo del título "Entradas": el cuerpo vuelve a Normal y sin negrita.
    req.append({"updateParagraphStyle": {
        "range": {"startIndex": cuerpo_ini, "endIndex": cuerpo_fin},
        "paragraphStyle": {"namedStyleType": "NORMAL_TEXT"},
        "fields": "namedStyleType"}})
    req.append({"updateTextStyle": {
        "range": {"startIndex": pos, "endIndex": cuerpo_fin},
        "textStyle": {"bold": False}, "fields": "bold"}})
    pos = cuerpo_ini
    for k, v in entrada["campos"]:
        etiqueta = f"{k}:"
        req.append({"updateTextStyle": {
            "range": {"startIndex": pos, "endIndex": pos + utf16_len(etiqueta)},
            "textStyle": {"bold": True}, "fields": "bold"}})
        pos += utf16_len(f"{k}: {v}") + 1
    return {"requiredRevisionId": revision, "requests": req}


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    revision, body = cargar_doc(sys.argv[1])
    entrada = json.load(open(sys.argv[2], encoding="utf-8"))
    print(json.dumps(construir(revision, indice_entradas(body), entrada), ensure_ascii=False, indent=1))
