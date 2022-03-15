from abc import ABC


class CustomerDAOInterface(ABC):

    @abstractmethod
    def create_customer_entry(self, customer:Customer) -> Customer:
        pass

    @abstractmethod
    def delete_customer_entry_by_id(self, customer_id: int) -> bool
        pass

