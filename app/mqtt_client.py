

import asyncio
import random
import paho.mqtt.client as mqtt
import json
import logging

logging.basicConfig(level=logging.DEBUG)

BROKER = "localhost"  
PORT = 1883 
TOPIC = "mqtt/status"
client_id = f"publish-{random.randint(0, 1000)}"

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            logging.info("Connected to MQTT Broker!")
        else:
            logging.error("Connection failed with result code %d", rc)
    
    client = mqtt.Client(client_id=client_id)
    client.on_connect = on_connect
    client.username_pw_set("guest", "guest") 
    client.connect(BROKER, PORT, 60)
    return client

async def wait_for_connection(client, timeout=5):
    for _ in range(timeout * 10): 
        if client.is_connected():
            return True
        await asyncio.sleep(0.1)
    raise TimeoutError("MQTT connection timeout.")

async def publish_messages(client):
    try:
        client.loop_start()
        await wait_for_connection(client)

        while True:
            message = {"status": random.randint(0, 6)}
            result = client.publish(TOPIC, json.dumps(message))
            
            if result.rc == mqtt.MQTT_ERR_SUCCESS:
                logging.info(f"Published: {message}")
            else:
                logging.error(f"Failed to publish message: {result}")
            
            await asyncio.sleep(1)
    except Exception as e:
        logging.error("Error occurred: %s", e)
    finally:
        client.loop_stop()

async def main():
    client = connect_mqtt()
    await publish_messages(client)

if __name__ == "__main__":
    asyncio.run(main())
