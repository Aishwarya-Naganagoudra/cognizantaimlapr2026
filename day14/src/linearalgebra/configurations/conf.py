#read path from .env file
import os
from dotenv import load_dotenv
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')

# Load environment variables from .env file
load_dotenv(env_path)

# Get the weather path from environment variables
class Config:
    #static variable to hold the weather path
    weather_path = os.getenv('weather_path')
    digits_path = os.getenv('digits_path')
    discount_path = os.getenv('discount_path')
    census_path = os.getenv('census_path')
    image_path = os.getenv('image_path')
    sales_path = os.getenv('sales_path')
    cyber_path = os.getenv('cyber_path')
    movie_path = os.getenv('movie_path')
    cleandata_path = os.getenv('cleandata_path')
    cleandata_path_v1 = os.getenv('cleandata_path_v1')
    population_path = os.getenv('population_path')
    ceo_salary_path = os.getenv('ceo_salary_path')