import datetime
import json
import os


def open_file(f):
    '''
    Открывает файл, если он существует
    '''
    if not os.path.exists(f):
        return None

    else:
        with open(f, "r", encoding='UTF-8') as file:
            opers = json.load(file)
            return [x for x in opers if x != {}]


def sort_dates(file):
    '''
    Сортирует открытый файл по дате
    '''
    sorted_file = sorted(file, key=lambda oper: oper['date'])
    for oper in sorted_file:
        date = datetime.datetime.strptime(oper.get('date'), '%Y-%m-%dT%H:%M:%S.%f')
        new_date = date.strftime('%d.%m.%Y')
        oper["date"] = new_date
    return sorted_file


def delete_cancelled(file):
    '''
    Удаляет из файла с операциями все отмененные операции
    '''
    for operation in file:
        if operation['state'] == 'CANCELED':
            file.remove(operation)
    return file


def hide_card_11(operation):
    '''
    Маскирует номер карты, если с нее был перевод и она содержит 1 слово
    '''
    card = operation['from']
    splitted_card = card.split(' ')
    hidden = ''
    for num in splitted_card[1][7:13]:
        hidden += '*'
    operation['from'] = f'{splitted_card[0]} {splitted_card[1][:7]}{hidden}{splitted_card[1][13:]}'
    return operation


def hide_card_12(operation):
    '''
    Маскирует номер карты, если на нее был перевод и она содержит 1 слово
    '''
    card = operation['to']
    splitted_card = card.split(' ')
    hidden = ''
    for num in splitted_card[1][7:13]:
        hidden += '*'
    operation['to'] = f'{splitted_card[0]} {splitted_card[1][:7]}{hidden}{splitted_card[1][13:]}'
    return operation


def hide_card_21(operation):
    '''
    Маскирует номер карты, если с нее был перевод и она содержит 2 слова
    '''
    card = operation['from']
    splitted_card = card.split(' ')
    hidden = ''
    for num in splitted_card[2][7:13]:
        hidden += '*'
    operation['from'] = f'{splitted_card[0]} {splitted_card[1]} {splitted_card[2][:7]}{hidden}{splitted_card[2][13:]}'
    return operation


def hide_card_22(operation):
    '''
    Маскирует номер карты, если на нее был перевод и она содержит 2 слова
    '''
    card = operation['to']
    splitted_card = card.split(' ')
    hidden = ''
    for num in splitted_card[2][7:13]:
        hidden += '*'
    operation['to'] = f'{splitted_card[0]} {splitted_card[1]} {splitted_card[2][:7]}{hidden}{splitted_card[2][13:]}'
    return operation


def hide_number_from(operation):
    '''
    Маскирует номер счета, если с него был перевод
    '''
    splitted_num = operation['from'].split(' ')
    hidden = '**'
    operation['from'] = f'{splitted_num[0]} {hidden}{splitted_num[1][-4:]}'
    return operation


def hide_number_to(operation):
    '''
    Маскирует номер счета, если на него был перевод
    '''
    splitted_num = operation['to'].split(' ')
    hidden = '**'
    operation['to'] = f'{splitted_num[0]} {hidden}{splitted_num[1][-4:]}'
    return operation


def show_operation(operation):
    '''
    Выводит информацию по операции
    '''
    if 'from' in operation.keys():
        return f'{operation["date"]} {operation["description"]}\n{operation["from"]} -> {operation["to"]}\n{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n'
    else:
        return f'{operation["date"]} {operation["description"]}\n{operation["to"]}\n{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n'