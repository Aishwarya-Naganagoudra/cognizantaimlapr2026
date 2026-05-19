#validate customer data retrieved from database

from abc import ABC, abstractmethod


class CustomerService(ABC):
    @abstractmethod
    def validate_customer_data(self):
        pass

    @abstractmethod
    def customer_data_quality_check(self):
        pass
    @abstractmethod
    def create_customer_from_dataframe(self):
        pass