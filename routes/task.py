from fastapi import APIRouter, HTTPException
from database import (
    get_all_tasks,
    get_one_task,
    create_task,
    update_task,
    delete_task
)
from models import Task

task = APIRouter()

@task.get("/")	
def welcome():
    return {"message": "Welcome to the API!"}

@task.get('/api/tasks')
async def get_tasks():
    response = await get_all_tasks()
    return response

@task.get('/api/tasks/{id}', response_model=Task)
async def get_task(id: int):
    response = await get_one_task(id)
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
async def put_task(id: int, data):
    response = await update_task(id, data)
    if response:
        return response
    raise HTTPException(404, f"There is no task with the id {id}")
    

@task.delete('/api/tasks/{id}')
async def remove_task(id: int):
    response = await delete_task(id)
    if response:
        return "Successfully deleted task"
    raise HTTPException(404, f"There is no task with the id {id}")
    