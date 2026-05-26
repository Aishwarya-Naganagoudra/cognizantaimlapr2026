# Create app FIRST
from fastapi import FastAPI
app = FastAPI(
    title="🛒 E-commerce API",
    description="API for managing e-commerce operations",
    version="1.0.0"
)

from orderapp.configurations.mysql_conf import engine, base

#  IMPORT MODELS FIRST (VERY IMPORTANT)
from orderapp.models.order import Order
#create all the tables in the database
base.metadata.create_all(bind=engine)
#make api call to the customer controller

from orderapp.controllers import order_controller


app.include_router(order_controller.order_router)




