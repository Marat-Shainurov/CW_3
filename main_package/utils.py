from datetime import datetime


def sort_processed_array(array: dict):
    """
    Функция принимет в качетве аргумента словарь, возвращает отсортированный по kyes, по возрастанию.
    """
    sorted_array = {}
    for k in sorted(array.keys()):
        sorted_array[k] = array[k]
    return sorted_array


def get_last_elements(array: dict, number_of_elements: int):
    """
    Функция принимет в качетве аргументов словарь и число number_of_elements.
    Преобразует в список из кортежей, возвращает нужное кол-во элементов от конца списка,
    в зависимости от второго аргумента (array[-number_of_elements:]).
    """
    array_list = list(array.items())
    array_list_last = array_list[-number_of_elements:]
    return array_list_last


def convert_data(data):
    """
    Функция принимет строку с датой транзакции, возвращает дату в формате д.м.г.
    """
    the_date = datetime.fromisoformat(data)
    new_format = [str(the_date.day), str(the_date.month), str(the_date.year)]
    return ".".join(new_format)


def hide_account_recipient(account):
    """
    Функция получает строку (номер счета получателя вида "Счет 64686473678894779589").
    Возвращает в виде "Счет **9589".
    """
    account_list = account.split()
    account_number = account_list[-1]
    hidden_number = f"**{account_number[-4:]}"
    account_list[-1] = hidden_number
    return " ".join(account_list)


def hide_account_sender(account):
    """
    Функция получает строку (номер счета отправиителя вида Maestro 1596837868705199).
    Возвращает в виде Maestro 1596 83** **** 5199.
    Для кейсов с Открытием счета (т.е. отсутствием счета отправителя), ринимает элемент 'Open',
    указанный в массиве вместо номра счета, возвращает 'Deposit' вместо номера счета.
    """
    if account != "Open":
        account_list = account.split()
        account_number = account_list[-1]
        hidden_number = f"{account_number[0:4]} {account_number[4:6]}** **** {account_number[-4:]}"
        account_list[-1] = hidden_number
        return " ".join(account_list)
    else:
        return "Deposit"


def print_results(array: list):
    """
    Принимает итоговый список из кортежей с последнийми операциями, возвращает список, для вывода в необзодимом виде:
    14.10.2018 Перевод организации
    Visa Platinum 7000 79** **** 6361 -> Счет **9638
    82771.72 руб.
    """
    res = []
    for element in range(len(array)):
        res.extend([convert_data(array[element][0]), " ", array[element][1][0], "\n"])
        res.extend([hide_account_sender(array[element][1][1]), " -> ", hide_account_recipient(array[element][1][2]), "\n"])
        res.extend([array[element][1][3], " ", array[element][1][4], "\n"])
        res.append("\n")
    return res
