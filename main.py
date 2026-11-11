import csv
from io import StringIO

from fastapi import FastAPI, File, HTTPException, UploadFile

app = FastAPI(title="CSV Statistics API")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/analyze")
async def analyze_csv(file: UploadFile = File(...)):
    if not file.filename or not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="Загрузите файл с расширением .csv")

    content = await file.read()
    try:
        text = content.decode("utf-8-sig")
    except UnicodeDecodeError as error:
        raise HTTPException(
            status_code=400,
            detail="Не удалось прочитать файл. Сохраните CSV в кодировке UTF-8.",
        ) from error

    reader = csv.DictReader(StringIO(text, newline=""))
    if not reader.fieldnames or any(not name.strip() for name in reader.fieldnames):
        raise HTTPException(
            status_code=400,
            detail="В CSV должны быть непустые заголовки столбцов.",
        )

    rows = list(reader)
    if any(None in row for row in rows):
        raise HTTPException(
            status_code=400,
            detail="В одной или нескольких строках больше значений, чем заголовков.",
        )

    return {
        "filename": file.filename,
        "row_count": len(rows),
        "columns": reader.fieldnames,
    }
