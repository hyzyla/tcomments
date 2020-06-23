release: flask db upgrade
web: gunicorn  -b $(HOST):$(PORT) app:app