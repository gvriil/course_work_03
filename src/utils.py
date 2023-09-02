import json
from datetime import datetime


def load_json(file_name):
    """
        Загружает данные из JSON-файла.

        Args:
            file_name (str): Имя JSON-файла для загрузки.

        Returns:
            dict: Загруженные данные из файла.
        """
    with open(file_name, 'r') as json_file:
        return json.load(json_file)


def format_date(operation):
    """
        Форматирует дату операции в нужный формат и возвращает строку вида "дд.мм.гггг Описание операции".

        Args:
            operation (dict): Словарь с данными операции.

        Returns:
            str: Форматированная строка даты и описания операции.
    """
    date = datetime.strptime(operation['date'], "%Y-%m-%dT%H:%M:%S.%f")
    description = operation['description']

    return f"{date.strftime('%d.%m.%Y')} {description}"


def format_amount(operation):
    """
        Форматирует сумму операции и валюту в строку.

        Args:
            operation (dict): Словарь с данными операции.

        Returns:
            str: Строка с форматированной суммой и валютой.
    """
    return operation["amount"] + " " + operation["currency"]["name"]


def extract_card_info(card_string):
    """
        Извлекает информацию о карте из строки.

        Args:
            card_string (str): Строка с данными карты.

        Returns:
            str: Строка с извлеченной информацией о карте.
    """
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
    """
        Получает список пяти самых недавних операций.

        Args:
            operations (list): Список операций.

        Returns:
            list: Список из пяти самых недавних операций.
    """
    sorted_operations = sorted(operations, key=lambda x: x['date'], reverse=True)
    return sorted_operations[:5]


def get_executed(operations):
    """
        Фильтрует список операций, оставляя только выполненные.

        Args:
            operations (list): Список операций.

        Returns:
            list: Список выполненных операций.
    """
    return [operation for operation in operations if operation and operation["state"] == "EXECUTED"]
