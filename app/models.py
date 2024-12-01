from pydantic import BaseModel
from datetime import datetime

class MQTTMessage(BaseModel):
    status: int
    timestamp: datetime
