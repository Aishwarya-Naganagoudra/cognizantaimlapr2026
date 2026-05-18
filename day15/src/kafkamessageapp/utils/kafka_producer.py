#publish kafka message to aiven kafka cluster topic name comedy-movies
import json
from pathlib import Path
from confluent_kafka import Producer
from kafkamessageapp.configurations.conf import KafkaConfig

BASE_DIR = Path(__file__).resolve().parent.parent
def kafka_config():
    conf = {
        'bootstrap.servers': KafkaConfig.BOOTSTRAP_SERVERS,
        'security.protocol': KafkaConfig.SECURITY_PROTOCOL,
        'ssl.ca.location': str(BASE_DIR / "ca.pem"),
        'ssl.certificate.location': str(BASE_DIR / "service.cert"),
        'ssl.key.location': str(BASE_DIR / "service.key"),
    }
    return conf

def kafka_producer():
    conf = kafka_config()
    producer = Producer(conf)
    return producer

def publish_message(producer, topic, message):
    producer.produce(topic, value=json.dumps(message), callback=message_delivery_report)
    producer.flush()

def message_delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered')


if __name__ == "__main__":
    producer = kafka_producer()
    topic = KafkaConfig.TOPIC_NAME
    message = {
    "movie_id": 1,
    "title": "The Shawshank Redemption",
    }
    publish_message(producer, topic, message)

    message_delivery_report(None, None)