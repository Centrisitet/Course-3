import datetime
import json
import os


def open_file(f):
    if not os.path.exists(f):
        return None

    else:
        with open(f, "r", encoding='UTF-8') as file:
            opers = json.load(file)
            return [x for x in opers if x != {}]


def sort_dates(file):
    sorted_file = sorted(file, key=lambda oper: oper['date'])
    for oper in sorted_file:
        date = datetime.datetime.strptime(oper.get('date'), '%Y-%m-%dT%H:%M:%S.%f')
        new_date = date.strftime('%d.%m.%Y')
        oper["date"] = new_date
    return sorted_file


def delete_cancelled(file):
    for operation in file:
        if operation['state'] == 'CANCELED':
            file.remove(operation)
    return file


def hide_card_11(operation):
    card = operation['from']
    splitted_card = card.split(' ')
    hidden = ''
    for num in splitted_card[1][7:13]:
        hidden += '*'
    operation['from'] = f'{splitted_card[0]} {splitted_card[1][:7]}{hidden}{splitted_card[1][13:]}'


def hide_card_12(operation):
    card = operation['to']
    splitted_card = card.split(' ')
    hidden = ''
    for num in splitted_card[1][7:13]:
        hidden += '*'
    operation['to'] = f'{splitted_card[0]} {splitted_card[1][:7]}{hidden}{splitted_card[1][13:]}'


def hide_card_21(operation):
    card = operation['from']
    splitted_card = card.split(' ')
    hidden = ''
    for num in splitted_card[2][7:13]:
        hidden += '*'
    operation['from'] = f'{splitted_card[0]} {splitted_card[1]} {splitted_card[2][:7]}{hidden}{splitted_card[2][13:]}'


def hide_card_22(operation):
    card = operation['to']
    splitted_card = card.split(' ')
    hidden = ''
    for num in splitted_card[2][7:13]:
        hidden += '*'
    operation['to'] = f'{splitted_card[0]} {splitted_card[1]} {splitted_card[2][:7]}{hidden}{splitted_card[2][13:]}'


def hide_number_from(operation):
    splitted_num = operation['from'].split(' ')
    hidden = '**'
    operation['from'] = f'{splitted_num[0]} {hidden}{splitted_num[1][-4:]}'


def hide_number_to(operation):
    splitted_num = operation['to'].split(' ')
    hidden = '**'
    operation['to'] = f'{splitted_num[0]} {hidden}{splitted_num[1][-4:]}'


def show_operation(operation):
    if 'from' in operation.keys():
        return f'{operation["date"]} {operation["description"]}\n{operation["from"]} -> {operation["to"]}\n{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n'
    else:
        return f'{operation["date"]} {operation["description"]}\n{operation["to"]}\n{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n'