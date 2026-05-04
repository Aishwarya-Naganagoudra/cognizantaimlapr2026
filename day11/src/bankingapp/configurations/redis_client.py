#rceate redis client
import redis.asyncio as redis
import os
from dotenv import load_dotenv
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)

class RedisClient:
    def __init__(self):
        host = os.getenv("redis_host")
        port = int(os.getenv("redis_port"))   
        #logical database number, default is 0     
        self.client = redis.Redis(host=host, port=port, db=0, decode_responses=True)

    def set(self, key, value):
        self.client.set(key, value)

    def get(self, key):
        return self.client.get(key)