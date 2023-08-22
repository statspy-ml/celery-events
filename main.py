from fastapi import FastAPI
from celery_app import celery_app
#from main import new_task_function

app = FastAPI()

@app.post("/execute_task/")
async def execute_task(value: int):
    task = new_task_function.delay(value)  # Envia uma tarefa para ser executada pelo Celery
    return {"task_id": task.id}


@celery_app.task
def new_task_function(param):
    # faz alguma coisa cool
    result = param * 2
    return result

