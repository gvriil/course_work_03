import pytest
import json
from src.utils import format_amount, extract_card_info, format_date, get_recent_operations, \
    get_executed, load_json
DATA_FILE = "tests/test_load_json.json"


@pytest.fixture
def sample_data():
    """
    Фиктивные данные для тестирования.
    """
    with open(DATA_FILE, 'r') as json_file:
        return json.load(json_file)


@pytest.fixture
def sample_operation(sample_data):
    """
    Выбирает первую операцию из фиктивных данных для тестирования.
    """
    return sample_data[0]


def test_format_date(sample_operation):
    """
    Тестирование функции format_date.
    Проверяет корректность форматирования даты и описания операции.
    """
    assert format_date(sample_operation) == "08.02.2010 Перевод организации"


def test_format_amount(sample_operation):
    """
    Тестирование функции format_amount.
    Проверяет корректность форматирования суммы и валюты операции.
    """
    assert format_amount(sample_operation["operationAmount"]) == "62654.30 USD"


def test_extract_card_info():
    """
    Тестирование функции extract_card_info.
    Проверяет корректность извлечения информации о карте отправителя.
    """
    assert extract_card_info("Visa Classic 1203921041964079") == "Visa Classic 1203 92** **** 4079"
    assert extract_card_info("Счет 34616199494072692721") == "Счет **2721"
    assert extract_card_info("Visa Classic 120392001041964079") == "Неизвестный номер"
    assert extract_card_info(None) == "Нет данных"


def test_get_recent_operations(sample_data):
    """
    Тестирование функции get_recent_operations.
    Проверяет корректность выбора пяти последних операций.
    """
    result_list = get_recent_operations(sample_data)
    assert len(result_list) == 5
    assert result_list[0]["id"] == 692008409
    assert result_list[-1]["id"] == 636137913


def test_get_executed(sample_data):
    """
    Тестирование функции get_executed.
    Проверяет корректность выбора выполненных операций.
    """
    result_list = get_executed(sample_data)
    assert len(result_list) == 5


def test_load_json():
    """
    Тестирование функции load_json.
    Проверяет корректность загрузки JSON-данных из файла.
    """
    result_list = load_json(DATA_FILE)
    assert len(result_list) == 6
