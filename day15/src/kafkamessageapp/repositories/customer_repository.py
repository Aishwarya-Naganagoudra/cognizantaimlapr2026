#create customer repository abstract class

from abc import ABC, abstractmethod


class CustomerRepository(ABC):
   
    @abstractmethod
    def get_all_customers(self):
        pass
    @abstractmethod
    def create_customer(self, customer):
        pass