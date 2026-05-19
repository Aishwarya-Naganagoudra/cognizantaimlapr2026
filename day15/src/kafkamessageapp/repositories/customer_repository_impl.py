#create customer respository implementation

from kafkamessageapp.models.customer import Customer
from kafkamessageapp.models.full_name import FullName
from kafkamessageapp.repositories.customer_repository import CustomerRepository
from kafkamessageapp.configurations.mysql_conf import session_local
from kafkamessageapp.configurations.conf import KafkaConfig


from datetime import datetime
class CustomerRepositoryImpl(CustomerRepository):     
        
     def get_all_customers(self):
          session = session_local()
          try:
                customers = session.query(Customer).all()
                return customers
          except Exception as e:
                raise e
          finally:
                session.close()

     def create_customer(self, customers):
           #write to mongodb
           mongo_client = KafkaConfig.client
           mongo_db = KafkaConfig.db
           customer_collection = mongo_db["customers"]
           for customer in customers:
                  customer_dict = {
                        "id": customer.id,
                        "first_name": customer.first_name,
                        "last_name": customer.last_name,
                        "email": customer.email,
                        "password": customer.password,
                        "created_at": customer.created_at,
                        "updated_at": customer.updated_at
                  }
                  customer_collection.insert_one(customer_dict)



    
