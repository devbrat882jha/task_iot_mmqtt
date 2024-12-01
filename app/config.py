from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    mongo_url: str = "mongodb://localhost:27017" 
    rabbitmq_url: str = 'amqp://guest:guest@localhost/'
    database_name: str = "mqtt_database"
    collection_name: str = "mqtt_messages"

settings = Settings()

