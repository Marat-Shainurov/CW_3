from main_package.AccountsTransfers import AccountsTransfers

# Тестовая ссылка на массив. Массив составлен на основе ссылки на рабочий массив,
# Выбраны 6 элементов, включая кейс пустого словаря, и отсутствия отправителя (Открытие вклада).
testing_path = "https://www.jsonkeeper.com/b/IL6A"


class TestAccountsTransfers:

    def test_get_data_from_link_normal(self):
        """
        Тестирукт обработку ссылки на json массив.
        Должен возвращать подготовленный список из транзакций.
        """
        testing_example = AccountsTransfers(testing_path)
        assert testing_example.get_data_from_link() == [
            {"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041", "operationAmount":
                {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
             "description": "Перевод организации", "from": "Maestro 1596837868705199",
             "to": "Счет 64686473678894779589"},
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364", "operationAmount":
                {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
             "description": "Перевод организации", "from": "MasterCard 7158300734726758",
             "to": "Счет 35383033474447895560"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572", "operationAmount":
                {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
             "description": "Перевод организации", "from": "Счет 75106830613657916952",
             "to": "Счет 11776614605963066702"},
            {"id": 587085106, "state": "EXECUTED", "date": "2018-03-23T10:45:06.972075", "operationAmount":
                {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
             "description": "Открытие вклада", "to": "Счет 41421565395219882431"},
            {},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689", "operationAmount":
                {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
             "description": "Перевод организации", "from": "Visa Platinum 1246377376343588",
             "to": "Счет 14211924144426031657"}
        ]

    def test_process_array(self):
        """
        Метод проверяет обработку полученного массива.
        Должен возвращать словарь, где keys - даты транзакций,
        values - список из необходимых для итогового вывода значения (description, from, to, amount, currency).
        Выбираются только транзакции со статусом "EXECUTED", отбрасываются пустые элементы {}.
        Для случает без счета отправителя (Открытие влкада), на месте счета отправителя присваевается значение "Open",
        для корректной дальнейшей работы с такими кейсами при итоговом выводе инфо.
        """
        testing_example = AccountsTransfers(testing_path)
        data = testing_example.get_data_from_link()
        assert testing_example.process_array(data) == \
               {"2019-08-26T10:50:58.294041":
                ["Перевод организации", "Maestro 1596837868705199", "Счет 64686473678894779589", "31957.58", "руб."],
                "2019-07-03T18:35:29.512364":
                ["Перевод организации", "MasterCard 7158300734726758", "Счет 35383033474447895560", "8221.37", "USD"],
                "2018-06-30T02:08:58.425572":
                ["Перевод организации", "Счет 75106830613657916952", "Счет 11776614605963066702", "9824.07", "USD"],
                "2018-03-23T10:45:06.972075":
                ["Открытие вклада", "Open", "Счет 41421565395219882431", "48223.05", "руб."]
                }
