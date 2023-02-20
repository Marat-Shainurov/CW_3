from datetime import datetime


def sort_processed_array(array: dict):
    sorted_array = {}
    for k in sorted(array.keys()):
        sorted_array[k] = array[k]
    return sorted_array


def get_last_elements(array: dict, number_of_elements: int):
    array_list = list(array.items())
    array_list_last = array_list[-number_of_elements:]
    return array_list_last


def convert_data(data):
    the_date = datetime.fromisoformat(data)
    new_format = [str(the_date.day), str(the_date.month), str(the_date.year)]
    return ".".join(new_format)


def hide_account_recipient(account):
    account_list = account.split()
    account_number = account_list[-1]
    hidden_number = f"**{account_number[-4:]}"
    account_list[-1] = hidden_number
    return " ".join(account_list)


def hide_account_sender(account):
    if account != "Open":
        account_list = account.split()
        account_number = account_list[-1]
        hidden_number = f"{account_number[0:4]} {account_number[4:6]}** **** {account_number[-4:]}"
        account_list[-1] = hidden_number
        return " ".join(account_list)
    else:
        return "Deposit"


def print_results(array: list):
    res = []
    for element in range(len(array)):
        res.extend([convert_data(array[element][0]), " ", array[element][1][0], "\n"])
        res.extend([hide_account_sender(array[element][1][1]), " ", hide_account_recipient(array[element][1][2]), "\n"])
        res.extend([array[element][1][3], " ", array[element][1][4], "\n"])
        res.append("\n")
    return res
