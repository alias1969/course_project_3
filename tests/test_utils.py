from utils.utils import get_dict_value, parse_string, get_value
from utils.utils import read_file_json, exist_file

import pytest


# Тестирование функций чтения операций из словаря json
@pytest.fixture
def dict_operation():
    # создаем фикстуру исходного словаря одной записи операции
    return {
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
    }


@pytest.fixture
def structure_operation():
    """Фикстура для структуры соответствия ключей словаря из json и класса"""
    return {
        'date': 'date',
        'state': 'state',
        'description': 'd'
                       'escription',
        'number_from': 'from',
        'number_to': 'to',
        'sum': 'operationAmount/amount',
        'currency': 'operationAmount/currency/name'
    }


def test_get_value(dict_operation):
    """ Тестирование функции получения значения словаря по ключу"""
    assert get_value(dict_operation, 'state') == 'EXECUTED'
    assert get_value(dict_operation, 'date') == '2019-08-26T10:50:58.294041'
    assert get_value({}, 'new') == ''


def test_parse_string(dict_operation):
    """ Тестирование функции получения значения словаря по ключу-полному пути в json"""
    assert parse_string({}, 'date') == ''
    assert parse_string(dict_operation, 'state') == 'EXECUTED'
    assert parse_string(dict_operation, 'date') == '2019-08-26T10:50:58.294041'
    assert parse_string(dict_operation, 'operationAmount/amount') == '31957.58'
    assert parse_string(dict_operation, 'operationAmount/currency/name') == 'руб.'
    assert parse_string({}, 'operationAmount/currency/name') == ''


def test_get_dict_value_1(dict_operation):
    structure_operation_1 = {
        'date': 'date',
        'state': 'state',
        'description': 'description',
        'number_from': 'from',
        'number_to': 'to',
    }

    assert get_dict_value(dict_operation, structure_operation_1) == {
        "date": "2019-08-26T10:50:58.294041",
        "state": "EXECUTED",
        'description': 'Перевод организации',
        "number_from": "Maestro 1596837868705199",
        "number_to": "Счет 64686473678894779589",
    }


def test_get_dict_value_2(dict_operation):
    structure_operation_2 = {
        'sum': 'operationAmount/amount',
        'currency': 'operationAmount/currency'
    }

    assert get_dict_value(dict_operation, structure_operation_2) == {
        "sum": "31957.58",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    }


def test_get_dict_value_3(dict_operation):
    structure_operation_3 = {
        'sum': 'operationAmount/amount',
        'currency': 'operationAmount/currency/name'
    }

    assert get_dict_value(dict_operation, structure_operation_3) == {
        "sum": "31957.58",
        "currency": "руб."
    }


def test_get_dict_value_4(dict_operation, structure_operation):
    assert get_dict_value(dict_operation, structure_operation) == {
        "date": "2019-08-26T10:50:58.294041",
        "state": "EXECUTED",
        'description': 'Перевод организации',
        "number_from": "Maestro 1596837868705199",
        "number_to": "Счет 64686473678894779589",
        "sum": "31957.58",
        "currency": "руб."
    }


def test_get_dict_value_5(structure_operation):
    assert get_dict_value({}, {'sum': 'operationAmount/amount'}) == {'sum': ''}
    assert get_dict_value({}, structure_operation) == {
        'date': '',
        'state': '',
        'description': '',
        'number_from': '',
        'number_to': '',
        'sum': '',
        'currency': ''
    }


def test_get_dict_value_6(structure_operation):
    dict_operation_5 = {
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
        "to": "Счет 64686473678894779589"
    }

    assert get_dict_value(dict_operation_5, structure_operation) == {
        "date": "2019-08-26T10:50:58.294041",
        "state": "EXECUTED",
        'description': 'Перевод организации',
        "number_from": "",
        "number_to": "Счет 64686473678894779589",
        "sum": "31957.58",
        "currency": "руб."
    }


def test_exist_file():
    """ Проверка существования файла"""
    assert exist_file('__init__.py') is True
    assert exist_file('') is False
    assert exist_file('test_format.py') is True


def test_read_file_json():
    """Чтение файла json"""
    assert read_file_json('') == []
