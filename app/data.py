from app.basestorage import Shop
from app.store import Store

store = Store(items={
    "печенька":25,
    "собачка":25,
    "ёлка":25
})

shop = Shop(items={
    "печенька":2,
    "собачка":2,
    "ёлка":2
})

storages = {
    "магазин":shop,
    "склад":store
}