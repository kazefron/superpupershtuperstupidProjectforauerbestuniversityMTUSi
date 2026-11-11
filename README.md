# superpupershtuperstupidProjectforauerbestuniversityMTUSi

Самое главное чтоб попа подтерта была

## CSV Statistics API

Простой API принимает CSV-файл и возвращает количество строк и названия столбцов.

### Установка и запуск в PowerShell

Из корневой папки репозитория `VVIT` выполните:

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

### Совместная работа через GitHub

Git-репозиторий проекта: https://github.com/kazefron/superpupershtuperstupidProjectforauerbestuniversityMTUSi

Отправьте изменения командой:

```powershell
git push -u origin main
```

Чтобы пригласить соавтора, откройте **Settings → Collaborators** на GitHub и добавьте его username. Для совместной работы создавайте отдельные ветки и отправляйте изменения через Pull Request.
