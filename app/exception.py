

class BaseError(Exception):
    message = "Неожиданная ошибка"

class NotEnoughSpace(BaseError):
    message = "Нет места на складе"

class NotEnoughroduct(BaseError):
    message = "Нет места на складе"

class TooManyDifferentProducts(BaseError):
    message = "Слишком много разных товаров"

class InvalidRequest(BaseError):
    message = "Неправильный запрос.Попробуйте ещё раз"

class InvalidNameShopOrStorages(BaseError):
    message = "Неправильное названия пункта А или В"