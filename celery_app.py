import os
from celery import Celery
import requests


RABBIT_HOST = os.environ.get("RABBITMQ_HOST", "localhost")
REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")

broker = f"pyamqp://guest:guest@{RABBIT_HOST}:5672//"
backend = f"redis://{REDIS_HOST}:6379"

celery_app = Celery(
    "tasks",
    broker=broker,
    backend=backend,
    task_serializer='json',
    accept_content=['json'],
)


@celery_app.task(name="celery_app.forward_to_fastapi")
def forward_to_fastapi(comment):
 
    response = requests.post("http://web:8000/process", json={"commentary": comment})
    return response.json()


