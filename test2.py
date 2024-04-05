from pelicandb import Pelican
import os
from pathlib import Path
import json
import android

jdocs = {"customcards":         {
    "options": {
        "search_enabled": True,
        "save_position": True
    },

    "layout": {
        "type": "LinearLayout",
        "orientation": "vertical",
        "height": "match_parent",
        "width": "match_parent",
        "weight": "0",
        "Elements": [
                {
                    "type": "LinearLayout",
                    "orientation": "horizontal",
                    "height": "wrap_content",
                    "width": "match_parent",
                    "weight": "0",
                    "Elements": [

                        {
                            "type": "LinearLayout",
                            "orientation": "vertical",
                            "height": "wrap_content",
                            "width": "match_parent",
                            "weight": "1",
                            "Elements": [
                                {
                                    "type": "TextView",
                                    "show_by_condition": "",
                                    "Value": "@string1",
                                    "NoRefresh": False,
                                    "document_type": "",
                                    "mask": "",
                                    "Variable": ""
                                },
                                {
                                    "type": "TextView",
                                    "show_by_condition": "",
                                    "Value": "@string2",
                                    "NoRefresh": False,
                                    "document_type": "",
                                    "mask": "",
                                    "Variable": ""
                                },
                                {
                                    "type": "TextView",
                                    "show_by_condition": "",
                                    "Value": "@string3",
                                    "NoRefresh": False,
                                    "document_type": "",
                                    "mask": "",
                                    "Variable": ""
                                }
                            ]
                        },
                        {
                            "type": "TextView",
                            "show_by_condition": "",
                            "Value": "@val",
                            "NoRefresh": False,
                            "document_type": "",
                            "mask": "",
                            "Variable": "",
                            "TextSize": "16",
                            "TextColor": "#DB7093",
                            "TextBold": True,
                            "TextItalic": False,
                            "BackgroundColor": "",
                            "width": "match_parent",
                            "height": "wrap_content",
                            "weight": 2
                        }
                    ]
                },
            {
                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "@descr",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": "",
                    "Variable": "",
                    "TextSize": "-1",
                    "TextColor": "#6F9393",
                    "TextBold": False,
                    "TextItalic": True,
                    "BackgroundColor": "",
                    "width": "wrap_content",
                    "height": "wrap_content",
                    "weight": 0
            }
        ]
    }

}
}

jdocs["customcards"]["cardsdata"] = []
db = Pelican("liteDB", path=os.path.dirname(Path(__file__).parent))
documents = db['orders'].all()
# hashMap.put("toast", json.dumps(type(documents), ensure_ascii=False))
hashMap.put("toast", json.dumps(documents, ensure_ascii=False))

for doc in documents:
    card = {
        "key": doc.get("_id"),
        "string1": doc.get("name"),
        "string2": doc.get("warehouse"),
        "string3": doc.get("client")
    }

    jdocs["customcards"]["cardsdata"].append(card)

hashMap.put("cards", json.dumps(jdocs, ensure_ascii=False))


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


db = Pelican("liteDB", path=os.path.dirname(Path(__file__).parent))

android.toast("Конект к базе")

res = db["orders"].all()


android.toast(str(res))
