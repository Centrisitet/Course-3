from funcs import *

file = '../operations.json'

operations = open_file(file)
operations = sort_dates(operations)
operations = delete_cancelled(operations)
last_operations = operations[-5:]
rev_last = last_operations[::-1]

for operation in rev_last:
    if 'from' in operation.keys():
        if "Счет" in operation['from']:
            hide_number_from(operation)
        elif len(operation['from'].split(' ')) == 2 and 'Счет' not in operation['from'].split(' '):
            hide_card_11(operation)
        elif len(operation['from'].split(' ')) == 3 and 'Счет' not in operation['from'].split(' '):
            hide_card_21(operation)
    if "Счет" in operation['to']:
        hide_number_to(operation)
    elif len(operation['to'].split(' ')) == 2 and 'Счет' not in operation['to'].split(' '):
        hide_card_12(operation)
    elif len(operation['to'].split(' ')) == 3 and 'Счет' not in operation['to'].split(' '):
        hide_card_22(operation)
    print(show_operation(operation))
