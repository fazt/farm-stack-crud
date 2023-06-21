from models import Task
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient('mongodb://localhost:27017')
database = client.taskdb
collection = database.tasks

async def get_one_task_id(id):
    task = await collection.find_one({"_id": id})
    return task

async def get_one_task(title):
    task = await collection.find_one({"title": title})
    return task

async def get_all_tasks():
    tasks = []
    cursor = collection.find({})
    async for document in cursor:
        tasks.append(Task(**document))
    return tasks

async def create_task(task):
    new_task = await collection.insert_one(task)
    created_task = await collection.find_one({"_id": new_task.inserted_id})
    return created_task

async def update_task(id, data: Task):
    await collection.update_one({"_id": id}, {"$set": data})
    document = await collection.find_one({"_id": id})
    return document

async def delete_task(id):
    await collection.delete_one({"_id": id})
    return True



