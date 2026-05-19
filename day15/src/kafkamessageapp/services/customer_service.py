#validate customer data retrieved from database

from abc import ABC, abstractmethod


class CustomerService(ABC):
    @abstractmethod
    def validate_customer_data(self):
        pass