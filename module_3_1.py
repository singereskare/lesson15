# Глобальная переменная для подсчета вызовов
calls = 0

# Объяснение кода:
# Глобальная переменная calls: Изначально установлена в 0, она будет использоваться для подсчета вызовов функций.

def count_calls():
    global calls
    calls += 1

# Объяснение кода:
# Функция count_calls:
# Использует оператор global для доступа к переменной calls.
# Увеличивает значение calls на 1 каждый раз, когда вызывается.

def string_info(string):
    count_calls()  # Увеличиваем счетчик вызовов
    length = len(string)
    upper = string.upper()
    lower = string.lower()
    return (length, upper, lower)

# Объяснение кода:
# Функция string_info:
# Принимает строку в качестве аргумента.
# Вызывает count_calls для увеличения счетчика.
# Возвращает кортеж, содержащий длину строки, строку в верхнем регистре и строку в нижнем регистре.

def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счетчик вызовов
    # Приводим строку и элементы списка к нижнему регистру для сравнения
    string_lower = string.lower()
    return string_lower in [item.lower() for item in list_to_search]

# Объяснение кода:
# Функция is_contains:
# Принимает строку и список в качестве аргументов.
# Вызывает count_calls для увеличения счетчика.
# Сравнивает строку с элементами списка, игнорируя регистр.

# Примеры вызовов функций
print(string_info('Capybara'))  # (8, 'CAPYBARA', 'capybara')
print(string_info('Armageddon'))  # (10, 'ARMAGEDDON', 'armageddon')
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # True
print(is_contains('cycle', ['recycling', 'cyclic']))  # False

# Объяснение кода:
# Примеры вызовов функций: Примерные вызовы функций с выводом результатов, а также вывод общего количества вызовов.

# Вывод значения переменной calls
print(calls)  # 4
