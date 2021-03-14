import logging
import os

from celery import Celery


BROKER_HOST = os.getenv("BROKER_HOST", "amqp://rabbitmq/")

app = Celery(
    "src.worker",
    broker=BROKER_HOST,
    backend='rpc://',
    include=["src.worker.tasks"]
)

logging.basicConfig(
    level=logging.INFO,
    filename='celery.log',
    filemode='w'
)
logger = logging.getLogger("CELERY")
