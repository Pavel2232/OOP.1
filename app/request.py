from typing import Dict

from app.exception import InvalidRequest, InvalidNameShopOrStorages
from app.storage import Storage


class Request:

    def __init__(self, request: str, storages :Dict[str,Storage]):

        splited_request = request.lower().split(' ')
        if len(splited_request) != 7:
            raise InvalidRequest

        self.quantity = int(splited_request[1])
        self.title = splited_request[2]
        self.departure = splited_request[4]
        self.destination = splited_request[6]

        if self.departure not in storages or self.destination not in storages:
            raise InvalidNameShopOrStorages