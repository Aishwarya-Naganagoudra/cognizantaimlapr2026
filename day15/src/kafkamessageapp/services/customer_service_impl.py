#create customer service implementation class to validate customer data retrieved from database 
from unittest import suite

from unittest import suite

import great_expectations as gx
import great_expectations.expectations as gxe
import pandas as pd
from kafkamessageapp.repositories.customer_repository_impl import CustomerRepositoryImpl
from kafkamessageapp.services.customer_service import CustomerService
class CustomerServiceImpl(CustomerService):
    def __init__(self):
        self.customer_repository = CustomerRepositoryImpl()
        self.context = gx.get_context()
    
    def ge_suite(self):
        self.data_source      = self.context.data_sources.add_pandas("customer_source")
        self.data_asset       = self.data_source.add_dataframe_asset("customers")
        self.batch_definition = self.data_asset.add_batch_definition_whole_dataframe("full_batch")    
        # Create suite (GX 1.0: context.suites, not get_validator)
        self.suite = self.context.suites.add(
            gx.ExpectationSuite(name="customers_suite")
        )
        return self.suite, self.batch_definition, self.data_asset, self.data_source
    
    def create_dataframe(self):
         self.customers = self.customer_repository.get_all_customers() 
        #create pandas dataframe from customer data
         self.df = pd.DataFrame([customer.__dict__ for customer in self.customers]
                               ,columns=["id","first_name","last_name","email","password","created_at","updated_at"])
         print(self.df.head())
         return self.df
 
    def validate_customer_data(self):
        
        self.df = self.create_dataframe()
        #check point schema validation for customer data

        #validate customer data retrieved from database
        print("Customer data validated successfully")
        self.suite, self.batch_definition, self.data_asset, self.data_source = self.ge_suite()
        # ─── EXERCISE 1: Schema — column presence & uniqueness ────────────────────────
        print("── Exercise 1: Schema")
        self.suite.add_expectation(gxe.ExpectColumnToExist(column="id"))
        self.suite.add_expectation(gxe.ExpectColumnToExist(column="first_name"))
        self.suite.add_expectation(gxe.ExpectColumnToExist(column="last_name"))
        self.suite.add_expectation(gxe.ExpectColumnToExist(column="email"))
        self.suite.add_expectation(gxe.ExpectColumnToExist(column="password"))
        self.suite.add_expectation(gxe.ExpectColumnToExist(column="created_at"))
        self.suite.add_expectation(gxe.ExpectColumnToExist(column="updated_at"))
        self.suite.add_expectation(gxe.ExpectColumnValuesToBeUnique(column="id"))
        #validate customer data using expectation suite
        validation_definition = self.context.validation_definitions.add(
            gx.ValidationDefinition(
                name="customer_data_validation",
                data=self.batch_definition,
                suite=self.suite,
            )
        )

        batch      = self.batch_definition.get_batch(batch_parameters={"dataframe": self.df})
        results    = validation_definition.run(batch_parameters={"dataframe": self.df})
 
        print(results)  
    def customer_data_quality_check(self):
        #check point data quality for customer data
        print("Customer data quality check completed successfully")
        self.df= self.create_dataframe()
        self.suite, self.batch_definition, self.data_asset, self.data_source = self.ge_suite()
        self.suite.add_expectation(gxe.ExpectColumnValuesToNotBeNull(column="id"))
        # T004 has null user_id — will FAIL
        self.suite.add_expectation(gxe.ExpectColumnValuesToNotBeNull(column="first_name"))
        # T008 has null amount — will FAIL
        self.suite.add_expectation(gxe.ExpectColumnValuesToNotBeNull(column="last_name"))
        # category: allow up to 20% nulls via mostly threshold
        self.suite.add_expectation(gxe.ExpectColumnValuesToNotBeNull(column="email"))
        #validate customer data using expectation suite
        validation_definition = self.context.validation_definitions.add(
            gx.ValidationDefinition(
                name="customer_data_validation",
                data=self.batch_definition,
                suite=self.suite,
            )
        )

        batch      = self.batch_definition.get_batch(batch_parameters={"dataframe": self.df})
        results    = validation_definition.run(batch_parameters={"dataframe": self.df})
 
        print(results)  