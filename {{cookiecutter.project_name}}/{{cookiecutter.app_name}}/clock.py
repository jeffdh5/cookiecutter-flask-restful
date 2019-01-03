import datetime
import logging

from apscheduler.schedulers.blocking import BlockingScheduler
from rq import Queue

from extensions import redis_conn
from {{cookiecutter.app_name}}.app import create_app

app = create_app()

logging.basicConfig()
default_queue = Queue('default', connection=redis_conn)
sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def dummy():
    print("Dummy!")

sched.start()