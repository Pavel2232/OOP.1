from typing import Dict

from app.request import Request
from app.storage import Storage


class Courier:

    def __init__(self, request: Request, storages: Dict[str, Storage]):
        self.__request = request

        if self.__request.departure in storages:
            self.__from = storages[self.__request.departure]

        if self.__request.destination in storages:
            self.__to = storages[self.__request.destination]

    def move(self):
        self.__from.remove_items(titile=self.__request.title, quantity=self.__request.quantity)
        print(f'Курьер забрал {self.__request.quantity} {self.__request.title} из {self.__request.departure}')

        self.__to.add_items(titile=self.__request.title, quantity=self.__request.quantity)
        print(f'Курьер доставил {self.__request.quantity} {self.__request.title} в {self.__request.destination}')
