from celery import Celery

celery_app = Celery(
    "tasks",
    broker="pyamqp://guest:guest@rabbitmq:5672//",
    backend="redis://localhost"
)

celery_app.conf.task_routes = {"app.tasks.*": "main-queue"}
