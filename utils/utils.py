import json
import os
from .operations import Operations


def exist_file(filename):
    """Проверить наличие файла и если надо, то, при отсутствии, создать пустой"""

    if os.path.exists(filename):
        return True
    else:
        print(f'Файл {filename} не найден')
        return False


def read_file_json(filename):
    """Считывает операции из файла json в класс Operations"""

    lst_from_file = []
    # проверим наличие файла
    if exist_file(filename):
        # считаем файл с операциями в список
        with open(filename, 'r') as file:
            raw_json = file.read()
            lst_from_file = json.loads(raw_json)

    return lst_from_file


def get_dict_value(item: dict, structure: dict) -> object:
    """ Возвращает словарь значений операций"""

    result = {}

    for key_operation, key_file in structure.items():
        result[key_operation] = parse_string(item, key_file)

    return result


def parse_string(item, key):
    """ Разбирает ключ мз структуры и возвращает конечное значение по конечному пути"""

    if type(item) is not dict:
        return item

    delimiter_position = key.find('/')
    if delimiter_position == -1:
        return get_value(item, key)

    else:
        return parse_string(get_value(item, key[:delimiter_position]), key[delimiter_position + 1:])


def get_value(item, key):
    """ Возвращает из словаря значение по ключу
    item - словарь
    key - ключ
    """

    if item.get(key) is not None:
        return item[key]
    else:
        return ''


def get_structure():
    return {
        'date': 'date',
        'state': 'state',
        'description': 'description',
        'number_from': 'from',
        'number_to': 'to',
        'sum': 'operationAmount/amount',
        'currency': 'operationAmount/currency/name'
    }


def read_operations(filename):
    """ Считывает операции из файла json в список
    и преобразовывает в экземпляры класса Operations
    """

    operations = []

    # определим соответствие ключей в файле ключам в классе в словаре
    structure_operation = {
        'date': 'date',
        'state': 'state',
        'description': 'description',
        'number_from': 'from',
        'number_to': 'to',
        'sum': 'operationAmount/amount',
        'currency': 'operationAmount/currency/name'
    }

    operations_from_file = read_file_json(filename)

    for item in operations_from_file:

        # проверяем не пустая ли операция
        if item.get('id') is None:
            continue

        dict_operation = get_dict_value(item, structure_operation)

        operations.append(Operations(dict_operation))

    return operations


def print_operations(operations, count_last_operations):
    """Выводит последние операции из списка operations

    count_last_operations - число последних операций, к-рые надо вывести"""

    count = 0

    for operation in operations:
        # если число выведенных операций совпадает с аргументом, то завершаем вывод
        if count == count_last_operations:
            break

        # если операция проведена, то выводим
        if operation.state == 'EXECUTED':
            count += 1
            print(operation.print_operation())
