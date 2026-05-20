#read from .env file
import os
from dotenv import load_dotenv
from pymongo import MongoClient
import certifi
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')

# Load environment variables from .env file
load_dotenv(env_path)
# Kafka configuration
class KafkaConfig:
    BOOTSTRAP_SERVERS = os.getenv('bootstrapserver')
    TOPIC_NAME = os.getenv('topicname')
    SECURITY_PROTOCOL = os.getenv('securityprotocol')
    client = MongoClient(os.getenv("conn_string"), tls=True,tlsCAFile=certifi.where())
    db = client["customerdb"]
    pizza_path = os.getenv('pizza_path')
    report_path = os.getenv('report_path')
