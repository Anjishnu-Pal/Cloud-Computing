from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

while True:
    data = {
        "student_id": random.randint(1, 5),
        "marks": random.randint(40, 100),
        "subject": "Cloud Kafka"
    }

    producer.send("student-marks", data)
    producer.flush()

    print("Sent:", data)
    time.sleep(2)
