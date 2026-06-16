from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "student-marks",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    group_id="student-group",
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

print("Consumer started... waiting for messages")

for message in consumer:
    print("Received:", message.value)
