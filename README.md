# CSV Statistics API

Простой API принимает CSV-файл и возвращает количество строк и названия столбцов.

## Установка и запуск в PowerShell

```powershell
cd .\Proect
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Для установки используются базовые `fastapi` и `uvicorn`, без extra-пакета `standard`, который может потребовать сборки PyYAML.

После запуска откройте `http://127.0.0.1:8000/docs`, выберите `POST /analyze`, нажмите **Try it out**, укажите CSV-файл и нажмите **Execute**.

- `GET /health` проверяет, что сервер запущен.
- `POST /analyze` принимает CSV в UTF-8 и возвращает число строк и список столбцов.

## Совместная работа через GitHub

Проект хранится в отдельном Git-репозитории в папке `Proect`. После создания пустого GitHub-репозитория выполните команды из этой папки:

```powershell
git remote add origin https://github.com/<владелец>/<репозиторий>.git
git push -u origin main
```

Замените адрес на URL своего репозитория. Добавьте соавтора через **Settings → Collaborators** на GitHub. Для совместной работы создавайте отдельные ветки и отправляйте изменения через Pull Request.
