import json
# import android
# from pysimplebase import SimpleBase
# from ru.travelfood.simple_ui import SimpleUtilites as suClass

# set = []
# cards = json.loads(hashMap.get("cards"))
# goods = cards["customcards"]["cardsdata"]
# for line in goods:
#     if 'cb1' in line and line['cb1'] == True:
#         set.append(line['doc_bd'])

# android.toast("Данные получены")
# db = SimpleBase("liteDB", path=suClass.get_simplebase_dir(), timeout=200)
# android.toast("Конект к базе")
# db["orders"].insert(json.dumps(set, ensure_ascii=False), upsert=True)
# android.toast("Данные в базе")


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
                        "height": "wrap_content",
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
    set = []
    cards = json.loads(y)
    goods = cards["customcards"]["cardsdata"]
    for line in goods:
        if 'cb1' in line and line['cb1'] == True:
            set.append(line['doc_bd'])
    answer = json.dumps(set, ensure_ascii=False)
    a = 0 type(set)


add_to_base()
