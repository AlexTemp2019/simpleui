from pelicandb import Pelican
import os
from pathlib import Path
import json
import android

db = Pelican("liteDB", path=os.path.dirname(Path(__file__).parent))

android.toast("Конект к базе")

z = [
    {
        "_id": "ac48584f-a0bb-11ea-86ca-782bcbe5684f",
        "name": "Заказ покупателя НМ00-000003 от 25.05.2020",
        "warehouse": "Адміністрація",
        "client": "Рута, ТОВ",
        "goods": [
            {
                "barcode": "9785222192672",
                "nom": "Шафа-купе",
                "unit": "шт",
                "qty": 0,
                "qty_plan": 1
            }
        ]
    },
    {
        "_id": "ac485865-a0bb-11ea-86ca-782bcbe5684f",
        "name": "Заказ покупателя ОМ00-000015 от 09.03.2020",
        "warehouse": "Адміністрація",
        "client": "Таурег, ПП",
        "goods": [
            {
                "barcode": "9786177198238",
                "nom": "Журнальний столик (індивідуальне замовлення)",
                "unit": "шт",
                "qty": 0,
                "qty_plan": 1
            }
        ]
    }
]

res = db["orders"].insert(
    {"name": "Персик", "price": 100, "_id": "2"}, upsert=True)

android.toast(str(res))


db = Pelican("liteDB", path=os.path.dirname(Path(__file__).parent))
android.toast("Конект к базе")

z = [
    {
        "_id": "ac48584f-a0bb-11ea-86ca-782bcbe5684f",
        "name": "Заказ покупателя НМ00-000003 от 25.05.2020",
        "warehouse": "Адміністрація",
        "client": "Рута, ТОВ",
        "goods": [
            {
                "barcode": "9785222192672",
                "nom": "Шафа-купе",
                "unit": "шт",
                "qty": 0,
                "qty_plan": 1
            }
        ]
    },
    {
        "_id": "ac485865-a0bb-11ea-86ca-782bcbe5684f",
        "name": "Заказ покупателя ОМ00-000015 от 09.03.2020",
        "warehouse": "Адміністрація",
        "client": "Таурег, ПП",
        "goods": [
            {
                "barcode": "9786177198238",
                "nom": "Журнальний столик (індивідуальне замовлення)",
                "unit": "шт",
                "qty": 0,
                "qty_plan": 1
            }
        ]
    }
]

comand = [{
    "database": "liteDB",
    "collection": "orders",
    "command": "upsert",
    "value": z
}]

comandJSON = [
    {
        "database": "liteDB",
        "collection": "orders",
        "command": "upsert",
        "value": [
            {
                "_id": "ac48584f-a0bb-11ea-86ca-782bcbe5684f",
                "name": "Заказ покупателя НМ00-000003 от 25.05.2020",
                "warehouse": "Адміністрація",
                "client": "Рута, ТОВ",
                "goods": [
                    {
                        "barcode": "9785222192672",
                        "nom": "Шафа-купе",
                        "unit": "шт",
                        "qty": 0,
                        "qty_plan": 1
                    }
                ]
            },
            {
                "_id": "ac485865-a0bb-11ea-86ca-782bcbe5684f",
                "name": "Заказ покупателя ОМ00-000015 от 09.03.2020",
                "warehouse": "Адміністрація",
                "client": "Таурег, ПП",
                "goods": [
                    {
                        "barcode": "9786177198238",
                        "nom": "Журнальний столик (індивідуальне замовлення)",
                        "unit": "шт",
                        "qty": 0,
                        "qty_plan": 1
                    }
                ]
            }
        ]
    }
]

android.toast(comandJSON)


hashMap.put("RunSimpleBase", comandJSON)
android.toast("Данные переданы")


db = SimpleBase("liteDB", path=suClass.get_simplebase_dir(), timeout=200)
android.toast("Конект к базе")

z = [
    {
        "_id": "ac48584f-a0bb-11ea-86ca-782bcbe5684f",
        "name": "Заказ покупателя НМ00-000003 от 25.05.2020",
        "warehouse": "Адміністрація",
        "client": "Рута, ТОВ",
        "goods": [
            {
                "barcode": "9785222192672",
                "nom": "Шафа-купе",
                "unit": "шт",
                "qty": 0,
                "qty_plan": 1
            }
        ]
    },
    {
        "_id": "ac485865-a0bb-11ea-86ca-782bcbe5684f",
        "name": "Заказ покупателя ОМ00-000015 от 09.03.2020",
        "warehouse": "Адміністрація",
        "client": "Таурег, ПП",
        "goods": [
            {
                "barcode": "9786177198238",
                "nom": "Журнальний столик (індивідуальне замовлення)",
                "unit": "шт",
                "qty": 0,
                "qty_plan": 1
            }
        ]
    }
]

comand = [{
    "database": "liteDB",
    "collection": "orders",
    "command": "upsert",
    "value": z
}]

comandJSON = json.dumps(comand, ensure_ascii=False)
android.toast(comandJSON)


hashMap.put("RunSimpleBase", comandJSON)
android.toast("Данные переданы")
