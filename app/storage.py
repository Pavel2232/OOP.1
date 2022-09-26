from abc import abstractmethod, ABC


class Storage(ABC):
    @abstractmethod
    def add_items(self, titile: str, quantity: int):
        pass

    @abstractmethod
    def remove_items(self, titile, quantity):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass
