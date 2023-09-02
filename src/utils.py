import json
from datetime import datetime


def load_json(file_name):
    with open(file_name, 'r') as json_file:
        return json.load(json_file)


def format_date(operation):
    date = datetime.strptime(operation['date'], "%Y-%m-%dT%H:%M:%S.%f")
    description = operation['description']

    return f"{date.strftime('%d.%m.%Y')} {description}"


def format_amount(operation):
    return operation["amount"] + " " + operation["currency"]["name"]


def extract_card_info(card_string):
    if card_string is None:
        return "Нет данных"
    card_parts = card_string.split()
    account_number = card_parts[-1]
    name = " ".join(card_parts[:-1])

    if len(account_number) == 16:
        return f"{name} {account_number[:4]} {account_number[4:6]}** **** {account_number[-4:]}"
    elif len(account_number) == 20:
        return f"{name} **{account_number[-4:]}"
    else:
        return "Неизвестный номер"


def get_recent_operations(operations):
    sorted_operations = sorted(operations, key=lambda x: x['date'], reverse=True)
    return sorted_operations[:5]


def get_executed(operations):
    return [operation for operation in operations if operation and operation["state"] == "EXECUTED"]



