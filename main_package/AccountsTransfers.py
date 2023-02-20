import requests


class AccountsTransfers:
    """
    **Поля:**
    - Ссылка на массив,
    **Методы:**
    - Обработка ссылки на массив (вернет общий список из вложенных словарей),
    - Обработка самого массива (вернет подготовленный словарь из транзакций (description, from, to, amount, currency)).
    """

    def __init__(self, path):
        self.path_to_data = path
        self.main_array = []
        self.processed_array = {}

    def get_data_from_link(self):
        """
        Метод возвращает готовый к работе массив (список из вложенных словарей),
        на основе json массива по ссылке path_to_data.
        """
        result = requests.get(self.path_to_data)
        self.main_array = result.json()
        return self.main_array

    def process_array(self, array):
        """
        Метод получает готовый к работе список из словарей, обрабатывает его,
        возвращает словарь, где keys - даты транзакций,
        values - список из необходимых для итогового вывода значения (description, from, to, amount, currency).
        Выбираются только транзакции со статусом "EXECUTED", отбрасываются пустые элементы {}.
        Для случает без счета отправителя (Открытие влкада), на месте счета отправителя присваевается значение "Open",
        для корректной дальнейшей работы с такими кейсами при итоговом выводе инфо.
        """
        for element in range(len(array)):
            if array[element] != {} and array[element]["state"] == "EXECUTED":
                try:
                    self.processed_array[self.main_array[element]["date"]] = [
                        self.main_array[element]["description"], self.main_array[element]["from"],
                        self.main_array[element]["to"], self.main_array[element]["operationAmount"]["amount"],
                        self.main_array[element]["operationAmount"]["currency"]["name"]
                    ]
                except KeyError:
                    self.processed_array[self.main_array[element]["date"]] = [
                        self.main_array[element]["description"], "Open",
                        self.main_array[element]["to"], self.main_array[element]["operationAmount"]["amount"],
                        self.main_array[element]["operationAmount"]["currency"]["name"]
                    ]
        return self.processed_array

    def __repr__(self):
        """
        Repr метод.
        """
        return f"AccountsTransfers({self.path_to_data})"
