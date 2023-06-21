from fastapi import APIRouter, HTTPException
from database import (
    get_all_tasks,
    get_one_task,
    get_one_task_id,
    create_task,
    update_task,
    delete_task
)
from models import Task, UpdateTask

task = APIRouter()

@task.get("/ping")	
def welcome():
    return {"message": "Welcome to the API!"}

@task.get('/api/tasks')
async def get_tasks():
    response = await get_all_tasks()
    return response

@task.get('/api/tasks/{id}', response_model=Task)
async def get_task(id: str):
    response = await get_one_task_id(id)
    if response:
        return response
    raise HTTPException(404, f"There is no task with the id {id}")


@task.post('/api/tasks', response_model=Task)
async def save_task(task: Task):
    taskFound = await get_one_task(task.title)
    if taskFound:
        raise HTTPException(409, "Task already exists")

    response = await create_task(task.dict())
    print(response)
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@task.put('/api/tasks/{id}', response_model=Task)
async def put_task(id: str, data: UpdateTask):
    response = await update_task(id, data)
    if response:
        return response
    raise HTTPException(404, f"There is no task with the id {id}")
    

@task.delete('/api/tasks/{id}')
async def remove_task(id: str):
    response = await delete_task(id)
    if response:
        return "Successfully deleted task"
    raise HTTPException(404, f"There is no task with the id {id}")
    