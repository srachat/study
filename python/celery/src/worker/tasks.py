import logging
from time import sleep

from .celery import app, logger


TASKS = ["add", "mul", "xsum"]

__all__ = ["TASKS", *TASKS]


@app.task
def add(x, y):
    logging.info("Starting the addition")
    sleep(5)
    return x + y


@app.task
def mul(x, y):
    logger.info("Starting the multiplying")
    sleep(5)
    return x * y


@app.task
def xsum(numbers):
    logger.info("Summing all numbers in the array")
    sleep(5)
    return sum(numbers)
