#access .env variables
import os
from dotenv import load_dotenv
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(env_path)
class Config:
    def __init__(self):
        self.csv_path = os.getenv('csv_path')
        self.api_requests_csv_path = os.getenv('api_requests_csv_path')
        self.delivery_time_csv_path = os.getenv('delivery_time_csv_path')   
        self.sip_path = os.getenv('sip_path')
        self.uniform_path = os.getenv('uniform_path')