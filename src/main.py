from src.utils import load_json, get_recent_operations, get_executed,\
    format_date, format_amount, extract_card_info
FILE_NAME = "data/operations.json"
if __name__ == '__main__':
    """
        Этот скрипт загружает операции из JSON-файла, фильтрует и сортирует их, 
        а затем выводит информацию о них в удобном формате.
    """
    # Загружаем операции из JSON-файла
    operations = load_json(FILE_NAME)

    # Фильтруем операции, оставляя только выполненные
    operations = get_executed(operations)

    # Получаем пять самых последних выполненных операций
    operations = get_recent_operations(operations)

    # Выводим информацию о каждой операции
    for operation in operations:

        # Выводим дату и описание операции
        print(format_date(operation))

        # Выводим информацию о карте отправителя (если есть) и получателе
        print(extract_card_info(operation.get("from", None)), "->", operation["to"])

        # Выводим сумму операции и валюту
        print(format_amount(operation["operationAmount"]))

        # Пустая строка для разделения операций
        print()
