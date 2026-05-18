from confluent_kafka import Producer
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent

conf = {
    "bootstrap.servers": "kafka-283c824f-aimltraining2026-53a8.i.aivencloud.com:20583",

    "security.protocol": "SSL",

    "ssl.ca.location": str(BASE_DIR / "ca.pem"),
    "ssl.certificate.location": str(BASE_DIR / "service.cert"),
    "ssl.key.location": str(BASE_DIR / "service.key"),
}
print("BASE_DIR:", BASE_DIR)
print("CA exists:", (BASE_DIR / "ca.pem").exists())
print("CERT exists:", (BASE_DIR / "service.cert").exists())
print("KEY exists:", (BASE_DIR / "service.key").exists())

print((BASE_DIR / "service.key").read_text().splitlines()[0])
producer = Producer(conf)

data = {
    "product": "Laptop",
    "cost": 50000
}

producer.produce(
    "test-topic",
    value=json.dumps(data)
)

producer.flush()

print("Message sent successfully")