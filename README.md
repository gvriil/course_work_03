# Course Work 03

Это третья курсовая работа в рамках обучения на курсах SkyPro. Проект направлен на обработку данных, представленных в формате JSON, которые представляют собой записи о банковских операциях с различными параметрами, такими как дата, статус, валюта, сумма и участники. Основная цель проекта - разработать программу, которая выводит информацию о последних пяти выполненных операциях, а также обеспечивает маскировку конфиденциальных данных.

## Функциональность

Программа предоставляет следующую функциональность:

- Загрузка данных из JSON-файла.
- Форматирование даты операции и вывод описания.
- Маскирование номеров карт и счетов для обеспечения анонимности данных.
- Отображение суммы операции в человеко-читаемом формате с указанием валюты.
- Вывод на экран информации о последних пяти выполненных операциях.

## Установка и использование

1. Склонируйте репозиторий на свой компьютер:

git clone https://github.com/gvriil/course_work_03
markdown
2. Перейдите в директорию проекта:

cd course_work_03
markdown
3. Запустите программу:

python main.py
markdown
Программа автоматически загрузит данные из JSON-файла и выведет информацию о последних пяти выполненных операциях, а также маскированные данные о плательщиках.

## Тестирование

Все функции программы покрыты тестами для обеспечения корректной работы. Вы можете запустить тесты с помощью библиотеки pytest. Для этого выполните следующие шаги:

1. Убедитесь, что у вас установлен pytest:

pip install pytest
markdown
2. Запустите тесты:

pytest tests/test_utils.py
markdown
## Преимущества

- Программа обрабатывает данные о банковских операциях и предоставляет информацию о последних выполненных операциях.
- Данные о плательщиках анонимизированы для обеспечения конфиденциальности.
- Все функции покрыты тестами, обеспечивая надежность и корректную работу.

## Возможные улучшения

- Добавление обработки исключений для предотвращения сбоев при чтении данных из файлов и выполнении операций с датами.
- Улучшение алгоритма маскирования данных для более гибкой обработки различных форматов номеров карт и счетов.
- Расширение функциональности для работы с данными о банковских клиентах, а не только операциях.

## Автор

Гавриил Бордюков  

## Лицензия

Этот проект лицензирован в соответствии с условиями MIT License.

__________________________________________________________________________________________________________________________________
english version

# Course Work 03

This is the third course project as part of the SkyPro courses. The project focuses on processing data presented in the JSON format, which represents records of bank operations with various parameters such as date, status, currency, amount, and participants. The main objective of the project is to develop a program that displays information about the last five executed operations while also ensuring the masking of confidential data.
Functionality

The program provides the following functionality:

    Loading data from a JSON file.
    Formatting the operation date and displaying its description.
    Masking card and account numbers to ensure data anonymity.
    Displaying the operation amount in a human-readable format along with the currency.
    Displaying information about the last five executed operations.

Installation and Usage

    Clone the repository to your computer:

git clone https://github.com/gvriil/course_work_03

    Navigate to the project directory:

cd course_work_03

    Run the program:

python main.py

The program will automatically load data from the JSON file and display information about the last five executed operations, as well as masked payer data.
Testing

All program functions are covered by tests to ensure correct functionality. You can run the tests using the pytest library. Follow these steps:

    Make sure you have pytest installed:

pip install pytest

    Run the tests:

pytest tests/test_utils.py

Advantages

    The program processes bank operation data and provides information about the latest executed operations.
    Payer data is anonymized to ensure confidentiality.
    All functions are covered by tests, ensuring reliability and correct operation.

Possible Enhancements

    Adding exception handling to prevent failures when reading data from files and performing date operations.
    Improving the data masking algorithm for more flexible handling of various card and account number formats.
    Extending the functionality to work with bank customer data, not just operations.

Author

Gavriil Bordyukov

License

This project is licensed under the terms of the MIT License.
