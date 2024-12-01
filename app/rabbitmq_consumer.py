import asyncio
from aio_pika import connect_robust
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime,timezone
import json

from config import settings


QUEUE_NAME = "mqtt_queue"

async def process_message(message_body: str, mongo_client: AsyncIOMotorClient):
    data = json.loads(message_body)
    collection = mongo_client[settings.database_name][settings.collection_name]
    document = {
        "status": data["status"],
        "timestamp": datetime.now(timezone.utc),
    }
    await collection.insert_one(document)
    print(f"Saved to MongoDB: {document}")

async def consume_messages():
    print("Starting to consume messages...")
    mongo_client = AsyncIOMotorClient(settings.mongo_url)
    connection = await connect_robust(settings.rabbitmq_url)
    channel = await connection.channel()
    queue = await channel.declare_queue(QUEUE_NAME, durable=True)

    print(f"Waiting for messages on queue {QUEUE_NAME}...")
    async for message in queue:
        async with message.process():
            await process_message(message.body.decode(), mongo_client)


if __name__ == "__main__":
    asyncio.run(consume_messages())
