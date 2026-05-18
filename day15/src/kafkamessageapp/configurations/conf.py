#read from .env file
import os
from dotenv import load_dotenv
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')

# Load environment variables from .env file
load_dotenv(env_path)
# Kafka configuration
class KafkaConfig:
    BOOTSTRAP_SERVERS = os.getenv('bootstrapserver')
    TOPIC_NAME = os.getenv('topicname')
    SECURITY_PROTOCOL = os.getenv('securityprotocol')