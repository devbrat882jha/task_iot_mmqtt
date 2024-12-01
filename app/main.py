from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
from typing import Dict

from config import settings
from mqtt_client import main
from rabbitmq_consumer import consume_messages
import asyncio

app = FastAPI()



mongo_client = AsyncIOMotorClient(settings.mongo_url)
collection = mongo_client[settings.database_name][settings.collection_name]

@app.get("/status_counts/")
async def get_status_counts(start_time: datetime, end_time: datetime) -> Dict[int, int]:
    if start_time >= end_time:
        raise HTTPException(status_code=400, detail="start_time must be before end_time")

    pipeline = [
        {"$match": {"timestamp": {"$gte": start_time, "$lte": end_time}}},
        {"$group": {"_id": "$status", "count": {"$sum": 1}}},
    ]

    results = await collection.aggregate(pipeline).to_list(length=None)
    return {entry["_id"]: entry["count"] for entry in results}
