from app.courier import Courier
from app.data import storages
from app.exception import InvalidRequest, BaseError, InvalidNameShopOrStorages
from app.request import Request

def main():
    print("\nДобрый день!\n")

    while True:
        for storage_name in storages:
            print(f"Сейчас в {storage_name}:\n {storages[storage_name].get_items()}")

        user_input = input('Введите запрос в формате: "Доставить 3 печенька из склад в магазин"\n'
                      'Введите "Стоп" или "stop" если хотите закончить:\n'
                      )
        if user_input in ('stop','стоп'):
            break
        try:
            request = Request(request=user_input,storages= storages)
        except (InvalidRequest,InvalidNameShopOrStorages) as error:
            print(error.message)
            continue


        courier =Courier(request= request,storages= storages)

        try:
            courier.move()
        except BaseError as error:
            print(error.message)



if __name__ == "__main__":
    main()
