#publish kafka message to aiven kafka cluster topic name comedy-movies
from pathlib import Path
from confluent_kafka import Producer
from kafkamessageapp.configurations.conf import Config

BASE_DIR = Path(__file__).resolve().parent.parent
def kafka_config():
    conf = {
        'bootstrap.servers': Config.KAFKA_BOOTSTRAP_SERVERS,
        'security.protocol': Config.KAFKA_SECURITY_PROTOCOL,
        'ssl.ca.location': str(BASE_DIR / "ca.pem"),
        'ssl.certificate.location': str(BASE_DIR / "service.cert"),
        'ssl.key.location': str(BASE_DIR / "service.key"),
    }
    return conf