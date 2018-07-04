web: gunicorn SheetAPI.wsgi --log-file -
release: python manage.py migrate
release: python script.py