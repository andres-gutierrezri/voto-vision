web: python manage.py collectstatic && python manage.py makemigrations && python manage.py migrate && gunicorn VOTO_VISION.wsgi:application --workers 3 --log-file -