from utils.funcs import *

import datetime
import json
import json
import pytest

with open('../test.json', 'r', encoding='UTF-8') as f:
  opers = json.load(f)
  file = [x for x in opers]


def test_open_file():
    assert open_file('') == None
    assert open_file("../test.json") == [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Maestro 1596837868705199"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Classic 7158300734726758",
    "to": "Visa Classic 7158300734726758"
  },
  {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  },
  {
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
  },
  {
    "id": 594226727,
    "state": "CANCELED",
    "date": "2018-09-12T21:27:25.241689",
    "operationAmount": {
      "amount": "67314.70",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    }
  }
]


def test_sort_dates():
    assert sort_dates(file) == [
      {
    "id": 587085106,
    "state": "EXECUTED",
    "date": "23.03.2018",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
  },{
    "id": 939719570,
    "state": "EXECUTED",
    "date": "30.06.2018",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  },
        {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "26.08.2019",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },{
    "id": 594226727,
    "state": "CANCELED",
    "date": "12.09.2018",
    "operationAmount": {
      "amount": "67314.70",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    }},
    {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "03.07.2019",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }]


def test_delete_cancelled():
        assert delete_cancelled(file) == [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
  {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  },
  {
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
  }
]


def test_hide_card_11():
    operation = file[0]
    assert hide_card_11(operation)['from'] == "Maestro 1596837******199"


def test_hide_card_12():
    operation = file[0]
    assert hide_card_12(operation)['to'] == "Maestro 1596837******199"


def test_hide_card_21():
    operation = file[1]
    assert hide_card_21(operation)['from'] == "Visa Classic 7158300******758"


def test_hide_card_22():
    operation = file[1]
    assert hide_card_22(operation)['to'] == "Visa Classic 7158300******758"


def test_hide_number_from():
    operation = file[2]
    assert hide_number_from(operation)['from'] == "Счет **6952"


def test_hide_number_to():
    operation = file[2]
    assert hide_number_to(operation)['to'] == "Счет **6952"


def test_show_operation():
    assert show_operation(operation = file[0]) == f'{operation["date"]} {operation["description"]}\n{operation["from"]} -> {operation["to"]}\n{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n'
    assert show_operation(operation= file[4]) == f'{operation["date"]} {operation["description"]}\n{operation["to"]}\n{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n'
