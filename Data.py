import time
import json
import random
from azure.eventhub import EventHubProducerClient, EventData

EVENT_HUB_CONNECTION_STR = "<EVENT_HUB_CONNECTION_STRING>"
EVENT_HUB_NAME = "stockdatahub"

SYMBOLS = ["AAPL", "MSFT", "GOOG"]
PRICE_RANGE = (100, 200)  # Random price between 100 and 200
VOLUME_RANGE = (1000, 100000)  # Random volume between 1k and 100k

producer = EventHubProducerClient.from_connection_string(
    conn_str=EVENT_HUB_CONNECTION_STR,
    eventhub_name=EVENT_HUB_NAME
)

def generate_random_stock_data(symbol):
    price = round(random.uniform(*PRICE_RANGE), 2)
    volume = random.randint(*VOLUME_RANGE)
    data = {
        "Global Quote": {
            "01. symbol": symbol,
            "05. price": str(price),
            "06. volume": str(volume),
            "07. latest trading day": time.strftime("%Y-%m-%d"),
            "08. previous close": str(price - random.uniform(0, 5)),
            "09. change": str(random.uniform(-5, 5)),
            "10. change percent": f"{random.uniform(-5, 5):.2f}%"
        }
    }
    return data

while True:
    event_data_batch = producer.create_batch()
    for sym in SYMBOLS:
        data = generate_random_stock_data(sym)
        event_data_batch.add(EventData(json.dumps(data)))
    producer.send_batch(event_data_batch)
    print("Sent batch of dummy events")
    time.sleep(5)
