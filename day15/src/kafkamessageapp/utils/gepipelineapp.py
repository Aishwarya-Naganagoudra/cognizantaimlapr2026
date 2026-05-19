
from kafkamessageapp.services.customer_service_impl import CustomerServiceImpl

if __name__ == "__main__":
    customer_service=CustomerServiceImpl()
    #customer_service.validate_customer_data()
    customer_service.customer_data_quality_check()