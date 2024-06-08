from datetime import datetime
from .format_utils import mask_number


class Operations:

    def __init__(self, dict_operation):
        ##т.к. структура определена, то можно было бы свойства объекта взять из словаря
        ##но это не безопасно, поэтому закомментировала
        # for name, value in dict_operation.items():
        #    setattr(self, name, value)

        self.date = dict_operation['date']
        self.state = dict_operation['state']
        self.description = dict_operation['description']
        self.number_from = dict_operation['number_from']
        self.number_to = dict_operation['number_to']
        self.sum = dict_operation['sum']
        self.currency = dict_operation['currency']

    def print_operation(self):
        return f'{datetime.fromisoformat(self.date).strftime('%d.%m.%Y')} {self.description}\n' \
               f'{mask_number(self.number_from)} -> {mask_number(self.number_to)}\n' \
               f'{self.sum}\n'
