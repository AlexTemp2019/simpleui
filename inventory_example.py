from pelicandb import Pelican
import os
from pathlib import Path
import json

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

jtable = {
    "customtable": {
        "options": {
            "search_enabled": True,
            "save_position": True
        },
        "layout": {
            "type": "LinearLayout",
            "orientation": "vertical",
            "height": "wrap_content",
            "width": "match_parent",
            "weight": "1",
            "Elements": [
                    {
                        "type": "LinearLayout",
                        "orientation": "horizontal",
                        "height": "wrap_content",
                        "width": "match_parent",


                        "Padding": "0",
                        "StrokeWidth": "1",

                        "weight": "1",
                        "Elements": [
                            {
                                  "type": "LinearLayout",
                                  "orientation": "vertical",
                                  "height": "wrap_content",
                                  "width": "match_parent",
                                  "weight": "3",

                                  "Elements": [
                                      {
                                          "type": "TextView",
                                          "show_by_condition": "",
                                          "Value": "@sku",
                                          "height": "wrap_content",
                                          "width": "match_parent",
                                          "TextSize": "16",

                                          "weight": "1",
                                          "TextBold": True,
                                          "gravity_horizontal": "left"
                                      },

                                      {
                                          "type": "TextView",
                                          "show_by_condition": "",
                                          "Value": "@charac",
                                          "height": "wrap_content",
                                          "width": "match_parent",
                                          "TextSize": "16",

                                          "weight": "1",
                                          "TextBold": True,
                                          "gravity_horizontal": "left"
                                      },

                                      {
                                          "type": "TextView",
                                          "show_by_condition": "",
                                          "Value": "@barcode",
                                          "height": "wrap_content",
                                          "width": "match_parent",
                                          "TextSize": "12",

                                          "weight": "1",
                                          "TextBold": False,
                                          "gravity_horizontal": "left"
                                      }

                                  ]
                            },
                            {
                                "type": "LinearLayout",
                                "orientation": "vertical",
                                "height": "wrap_content",
                                "width": "match_parent",
                                "weight": "1",
                                "StrokeWidth": "1",
                                "BackgroundColor": "#F0F8FF",
                                "Elements": [

                                    {"type": "TextView",
                                     "show_by_condition": "",
                                     "Value": "План",
                                     "height": "wrap_content",
                                     "width": "match_parent",
                                     "weight": "1",

                                     "gravity_horizontal": "center"
                                     },

                                    {"type": "TextView",
                                     "show_by_condition": "",
                                     "Value": "@qty",
                                     "height": "wrap_content",
                                     "width": "match_parent",
                                     "weight": "1",
                                     "TextBold": True,
                                     "gravity_horizontal": "center"
                                     },
                                    {"type": "TextView",
                                     "show_by_condition": "",
                                     "Value": "Факт",
                                     "height": "wrap_content",
                                     "width": "match_parent",
                                     "weight": "1",

                                     "gravity_horizontal": "center"
                                     },

                                    {"type": "TextView",
                                     "show_by_condition": "",
                                     "Value": "@qty_fact",
                                     "height": "wrap_content",
                                     "width": "match_parent",
                                     "weight": "1",
                                     "TextBold": True,
                                     "gravity_horizontal": "center"
                                     }


                                ]
                            }
                        ]
                    }
            ]
        }
    }
}


db = Pelican("liteDB", path=os.path.dirname(Path(__file__).parent))


def inventory_list_open(hashMap, _files=None, _data=None):

    jdocs["customcards"]["cardsdata"] = []
    documents = db['inventory'].all()

    for doc in documents:
        card = {
            "key": doc.get("_id"),
            "string1": doc.get("name"),
            "string2": doc.get("warehouse"),
            "string3": doc.get("descr")
        }

        jdocs["customcards"]["cardsdata"].append(card)

    hashMap.put("cards", json.dumps(jdocs, ensure_ascii=False))

    return hashMap


def orders_list_open(hashMap, _files=None, _data=None):

    jdocs["customcards"]["cardsdata"] = []
    db = Pelican("liteDB", path=os.path.dirname(Path(__file__).parent))
    documents = db['orders'].all()

    for doc in documents:
        card = {
            "key": doc.get("_id"),
            "string1": doc.get("name"),
            "string2": doc.get("warehouse"),
            "string3": doc.get("client")
        }

        jdocs["customcards"]["cardsdata"].append(card)

    hashMap.put("cards", json.dumps(jdocs, ensure_ascii=False))

    return hashMap


document = None


def inventory_list_click(hashMap, _files=None, _data=None):
    global document

    document = db['inventory'].get(hashMap.get("selected_card_key"))
    hashMap.put("toast", json.dumps(document["goods"], ensure_ascii=False))

    hashMap.put("ShowScreen", "Инвентаризация")

    return hashMap


def orders_list_click(hashMap, _files=None, _data=None):
    global document

    document = db['orders'].get(hashMap.get("selected_card_key"))
    hashMap.put("toast", hashMap.get("selected_card_key"))

    hashMap.put("ShowScreen", "Сборка заказа")

    return hashMap


def inventory_open(hashMap, _files=None, _data=None):

    jtable["customtable"]["tabledata"] = []

    for line in document["goods"]:
        l = {"sku": line.get("nom"),
             "charac": line.get("charac"),
             "barcode": line.get("barcode"),
             "qty": line.get("qty_plan"),
             "qty_fact": line.get("qty")
             }
        jtable["customtable"]["tabledata"].append(l)

    hashMap.put("toast", json.dumps(
        jtable["customtable"]["tabledata"], ensure_ascii=False))
    hashMap.put("table", json.dumps(jtable, ensure_ascii=False))

    return hashMap


def orders_open(hashMap, _files=None, _data=None):

    jtable["customtable"]["tabledata"] = []

    for line in document["goods"]:
        l = {"sku": line.get("nom"),
             "barcode": line.get("barcode"),
             "qty": line.get("qty_plan"),
             "qty_fact": line.get("qty")

             }
        jtable["customtable"]["tabledata"].append(l)

    hashMap.put("table", json.dumps(jtable, ensure_ascii=False))

    return hashMap


pos = -1


def inventory_input(hashMap, _files=None, _data=None):
    global document
    global pos

    if hashMap.get("listener") == "barcode":

        for line in document["goods"]:
            if line["barcode"] == hashMap.get("barcode"):
                pos = document["goods"].index(line)
                break

        if pos == -1:
            hashMap.put("toast", "Штрихкод не найден")
            return hashMap

        layout = {
            "Value": "",
            "Variable": "",
            "type": "LinearLayout",
            "weight": "0",
            "height": "match_parent",
            "width": "match_parent",
            "orientation": "vertical",
            "Elements": [
                {
                    "type": "TextView",
                    "height": "wrap_content",
                    "width": "match_parent",
                    "weight": "0",
                    "Value": "Количество",
                    "Variable": ""
                },
                {
                    "type": "EditTextText",
                    "height": "wrap_content",
                    "width": "match_parent",
                    "weight": "0",
                    "Value": "",
                    "Variable": "qty"
                }
            ],
            "BackgroundColor": "",
            "StrokeWidth": "",
            "Padding": ""
        }

        hashMap.put("ShowDialogLayout", json.dumps(layout, ensure_ascii=False))
        hashMap.put("ShowDialog", "")
        hashMap.put("ShowDialogStyle", json.dumps(
            {"title": "Ввод количества", "yes": "Сохранить", "no": "Отмена"}, ensure_ascii=False))

    elif hashMap.get("event") == "onResultPositive":
        hashMap.put("toast", str(pos))
        if pos > -1:
            document["goods"][pos]["qty"] = hashMap.get("qty")
            db['inventory'].insert(document, upsert=True)

    return hashMap


def orders_input(hashMap, _files=None, _data=None):
    global document
    global pos

    if hashMap.get("listener") == "barcode":

        for line in document["goods"]:
            if line["barcode"] == hashMap.get("barcode"):
                pos = document["goods"].index(line)
                break

        if pos == -1:
            hashMap.put("toast", "Штрихкод не найден")
            return hashMap

        layout = {
            "Value": "",
            "Variable": "",
            "type": "LinearLayout",
            "weight": "0",
            "height": "match_parent",
            "width": "match_parent",
            "orientation": "vertical",
            "Elements": [
                {
                    "type": "TextView",
                    "height": "wrap_content",
                    "width": "match_parent",
                    "weight": "0",
                    "Value": "Количество",
                    "Variable": ""
                },
                {
                    "type": "EditTextText",
                    "height": "wrap_content",
                    "width": "match_parent",
                    "weight": "0",
                    "Value": "",
                    "Variable": "qty"
                }
            ],
            "BackgroundColor": "",
            "StrokeWidth": "",
            "Padding": ""
        }

        hashMap.put("ShowDialogLayout", json.dumps(layout, ensure_ascii=False))
        hashMap.put("ShowDialog", "")
        hashMap.put("ShowDialogStyle", json.dumps(
            {"title": "Ввод количества", "yes": "Сохранить", "no": "Отмена"}, ensure_ascii=False))

    elif hashMap.get("event") == "onResultPositive":
        hashMap.put("toast", str(pos))
        if pos > -1:
            document["goods"][pos]["qty"] = hashMap.get("qty")
            db['inventory'].insert(document, upsert=True)

    return hashMap


def add_to_base(hashMap, _files=None, _data=None):
    if hashMap.get("current_operation_name") == "Загрузка заказов":
        hashMap.put("toast", "это Загрузка")
        collection = 'orders'
    else:
        collection = 'inventory'

    doc = []
    cards = json.loads(hashMap.get("cards"))
    goods = cards["customcards"]["cardsdata"]
    for line in goods:
        if 'cb1' in line and (line['cb1'] == 'true' or True):
            doc.append(line['doc_bd'])
    doc_txt = json.dumps(doc, ensure_ascii=False)
    hashMap.put("toast", doc_txt)
    db[collection].clear()
    res = db[collection].insert(doc, upsert=True)
    hashMap.put("toast", str(res))

    return hashMap
