#fastapi part
from fastapi import FastAPI
from fastapi import APIRouter

import db
import rabbitmq
import pika
import uvicorn as uvicorn

from pydantic import BaseModel


class MessageSchema(BaseModel):
    message: str


router = APIRouter(tags=['items'], responses={404: {"description": "Not found"}})
app = FastAPI()
app.include_router(router)

@app.on_event('startup')
async def startup():
    loop = asyncio.get_running_loop()
    task = loop.create_task(app.rabbitmq.consume(loop))
    await task

@router.post('/post')
async def send_message(payload: MessageSchema):
    app.rabbitmq.send(
        {"message": payload.message}
    )
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run("fast_api:app", port=9000, reload=True)
