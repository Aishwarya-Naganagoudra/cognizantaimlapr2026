from confluent_kafka import Consumer
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent

conf = {
    "bootstrap.servers": "kafka-283c824f-aimltraining2026-53a8.i.aivencloud.com:20583",
    "security.protocol": "SSL",

    "ssl.ca.location": str(BASE_DIR / "ca.pem"),
    "ssl.certificate.location": str(BASE_DIR / "service.cert"),

    # Use service_plain.key if you converted the key
    "ssl.key.location": str(BASE_DIR / "service.key"),

    "group.id": "tax-consumer-group",
    "auto.offset.reset": "earliest",
}

consumer = Consumer(conf)
consumer.subscribe(["test-topic"])

print("Waiting for messages from Aiven Kafka...")

try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue

        if msg.error():
            print("Kafka error:", msg.error())
            continue

        data = json.loads(msg.value().decode("utf-8"))

        cost = float(data["cost"])
        tax = cost * 0.10

        print({
            "product": data["product"],
            "cost": cost,
            "tax": tax
        })

except KeyboardInterrupt:
    print("Consumer stopped")

finally:
    consumer.close()