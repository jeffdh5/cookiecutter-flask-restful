web: newrelic-admin run-program gunicorn {{cookiecutter.app_name}}.wsgi:app
worker: python {{cookiecutter.app_name}}/worker.py default high low
clock_scheduler: python {{cookiecutter.app_name}}/clock.py
