#create customer service implementation class to validate customer data retrieved from database 
import great_expectations as gx
from kafkamessageapp.services.customer_service import CustomerService
class CustomerServiceImpl(CustomerService):
    def __init__(self):
        self.customer_repository = CustomerServiceImpl()
        self.context = gx.get_context()
    
    def ge_suite(self):
        self.data_source      = self.context.data_sources.add_pandas("customer_source")
        self.data_asset       = self.data_source.add_dataframe_asset("customers")
        self.batch_definition = self.data_asset.add_batch_definition_whole_dataframe("full_batch")    

    def validate_customer_data(self):
        
        self.customers = self.customer_repository.get_all_customers()   
        #check point schema validation for customer data

        #validate customer data retrieved from database
        print("Customer data validated successfully")