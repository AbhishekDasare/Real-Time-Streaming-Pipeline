from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

data = [
    {"customer_id":1,"amount":5000},
    {"customer_id":2,"amount":7000},
    {"customer_id":3,"amount":3000}
]

for record in data:
    producer.send('sales_topic', value=record)
    time.sleep(2)

producer.flush()
