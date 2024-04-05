from ru.travelfood.simple_ui import SimpleUtilites as suClass
from pysimplebase import SimpleBase
import android
import json
# import android
# from pysimplebase import SimpleBase
# from ru.travelfood.simple_ui import SimpleUtilites as suClass

# order = []
# cards = json.loads(hashMap.get("cards"))
# goods = cards["customcards"]["cardsdata"]
# for line in goods:
#     if 'cb1' in line and (line['cb1'] == 'true' or line['cb1'] == True):
#         order.append(line['doc_bd'])

# ordertxt = json.dumps(order, ensure_ascii=False)
# android.toast(ordertxt)
# android.toast("Данные получены")
# db = SimpleBase("liteDB", path=suClass.get_simplebase_dir(), timeout=200)
# android.toast("Конект к базе")
# db["orders"].insert(ordertxt, upsert=True)
# android.toast("Данные в liteDB")


# hashMap.put("myset", ordertxt)
# android.stop(hashMap)


# import json
# import android
# from pysimplebase import SimpleBase
# from ru.travelfood.simple_ui import SimpleUtilites as suClass

# android.toast("Конект к базе старт")
# db = SimpleBase("liteDB", path=suClass.get_simplebase_dir(), timeout=200)
# android.toast("Конект к базе финиш")
# doc = db['orders'].all()
# android.toast("Запрос выполнен")
# android.toast(json.dumps(doc, ensure_ascii=False))
# android.toast("Конец")


def add_to_base():
    y = '''{
    "customcards": {
            "options": {"search_enabled": true, "save_position": true},
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
                                "type": "CheckBox",
                                "Value": "@cb1",
                                "NoRefresh": false,
                                "document_type": "",
                                "mask": "",
                                "Variable": "cb1",
                                "BackgroundColor": "#DB7093",
                                "width": "match_parent",
                                "height": "wrap_content",
                                "weight": 2
                            },
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
                                        "NoRefresh": false,
                                        "document_type": "",
                                        "mask": "",
                                        "Variable": ""
                                    },
                                    {
                                        "type": "TextView",
                                        "show_by_condition": "",
                                        "Value": "@string2",
                                        "NoRefresh": false,
                                        "document_type": "",
                                        "mask": "",
                                        "Variable": ""
                                    },
                                    {
                                        "type": "TextView",
                                        "show_by_condition": "",
                                        "Value": "@string3",
                                        "NoRefresh": false,
                                        "document_type": "",
                                        "mask": "",
                                        "Variable": ""
                                    },
                                    {
                                        "type": "TextView",
                                        "show_by_condition": "",
                                        "Value": "@string4",
                                        "NoRefresh": false,
                                        "document_type": "",
                                        "mask": "",
                                        "Variable": ""
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "TextView",
                        "show_by_condition": "",
                        "Value": "@descr",
                        "NoRefresh": false,
                        "document_type": "",
                        "mask": "",
                        "Variable": "",
                        "TextSize": "-1",
                        "TextColor": "#6F9393",
                        "TextBold": false,
                        "TextItalic": true,
                        "BackgroundColor": "",
                        "width": "wrap_content",
                        "height": "wrap_content",ё
                        "weight": 0
                    }
                ]
            },
            "cardsdata": [
                {
                    "key": "ac48584f-a0bb-11ea-86ca-782bcbe5684f",
                    "string1": "Номер НМ00-000003</strong>",
                    "string2": "Дата 25.05.2020 12:00:00</strong>",
                    "string3": "Склад Адміністрація</strong>",
                    "string4": "Клиент Рута, ТОВ</strong>",
                    "descr": "",
                    "doc_bd": {
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
                    "cb1": true
                },
                {
                    "key": "ac485865-a0bb-11ea-86ca-782bcbe5684f",
                    "string1": "Номер ОМ00-000015</strong>",
                    "string2": "Дата 09.03.2020 12:00:02</strong>",
                    "string3": "Склад Адміністрація</strong>",
                    "string4": "Клиент Таурег, ПП</strong>",
                    "descr": "",
                    "doc_bd": {
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
                }
            ]
        }
    }'''
    doc = []
    cards = json.loads(y)
    goods = cards["customcards"]["cardsdata"]
    for line in goods:
        if 'cb1' in line and (line['cb1'] == 'true' or line['cb1'] == True):
            doc.append(line['doc_bd'])
    doc_txt = json.dumps(doc, ensure_ascii=False)
    hashMap.put("toast", doc_txt)
    db['orders'].insert(doc, upsert=True)
    hashMap.put("toast", "Данные в базе")

    return hashMap


add_to_base()


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


db["orders"].insert(z, upsert=True)
android.toast("Данные в liteDB")


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
