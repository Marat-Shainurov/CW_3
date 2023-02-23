from main_package.AccountsTransfers import AccountsTransfers
from main_package import utils

path_to_main_array = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=" \
                     "0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-" \
                     "aad1945e5421&expirationTimestamp=1677253225716&signature=" \
                     "cPiw52cHRncnz3IIC54vAxqR6VeGtPtpR0i1TYv9h9U&downloadName=operations.json"

# Создаем экземпляр класса, по основной ссылке.
example_main = AccountsTransfers(path_to_main_array)

# Обрабатываем экземпляр, получив список-массив к работе.
data_from_example_main = example_main.get_data_from_link()

# Обрабатываем список методом process_array, оставив необходимую для работы и вывода пользователю инфо.
processed_data = example_main.process_array(data_from_example_main)

# Сортируем массив по дате транзакции, с помощью функции sort_processed_array.
sorted_data = utils.sort_processed_array(processed_data)

# Получаем 5 последних транзакцийб с помощью функции get_last_elements.
last_transactions = utils.get_last_elements(sorted_data, 5)

# Выводим итоговый результат, с помощью функции print_results.
print("".join(utils.print_results(last_transactions)))
