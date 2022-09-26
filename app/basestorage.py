from typing import Dict

from app.exception import NotEnoughSpace, NotEnoughroduct, TooManyDifferentProducts
from app.storage import Storage


class BaseStorage(Storage):

    def __init__(self,items: Dict[str,int],capacity: int):
        self.__items = items
        self.__capacity = capacity

    def add_items(self,titile: str,quantity:int) -> None:


        if self.get_free_space() < quantity:
            raise NotEnoughSpace


        if titile in self.__items:
            self.__items[titile] += quantity
        else:
            self.__items[titile] = quantity

    def get_free_space(self) -> int:
        current_space = 0
        for value in self.__items.values():
            current_space += value
        return self.__capacity - current_space


    def remove_items(self,titile: str,quantity: int)-> None:
        if titile not in self.__items or self.__items[titile] < quantity:
            raise NotEnoughroduct

        self.__items[titile] -= quantity
        if self.__items[titile] == 0:
            self.__items.pop(titile)

    def get_items(self)-> Dict[str,int]:
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items)


class Shop(BaseStorage):
    def __init__(self, items: dict, capacity: int = 20):
        super().__init__(items,capacity)


    def add_items(self,titile,quantity) -> None:
        if self.get_unique_items_count() >= 5:
            raise TooManyDifferentProducts

        super().add_items(titile,quantity)


