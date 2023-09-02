from src.utils import load_json, get_recent_operations, get_executed,\
    format_date, format_amount, extract_card_info
FILE_NAME = "data/operations.json"
if __name__ == '__main__':
    operations = load_json(FILE_NAME)
    operations = get_executed(operations)
    operations = get_recent_operations(operations)
    for operation in operations:
        print(format_date(operation))
        print(extract_card_info(operation.get("from", None)), "->", operation["to"])
        print(format_amount(operation["operationAmount"]))
        print()

