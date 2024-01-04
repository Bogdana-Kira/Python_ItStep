def divide_numbers():
    try:
        numerator = float(input("Введіть чисельник: "))
        denominator = float(input("Введіть знаменник: "))
        result = numerator / denominator
        print(f"Результат ділення: {result}")
    except ZeroDivisionError:
        print("Помилка: Ділення на нуль неможливе.")
    except ValueError:
        print("Помилка: Будь ласка, введіть коректні числа.")

# Виклик функції
divide_numbers()

def access_list_element():
    my_list = [1, 2, 3, 4, 5]
    try:
        index = int(input("Введіть індекс для доступу до списку: "))
        value = my_list[index]
        print(f"Значення за індексом {index}: {value}")
    except IndexError:
        print("Помилка: Введений індекс виходить за межі списку.")
    except ValueError:
        print("Помилка: Будь ласка, введіть коректний цілочисельний індекс.")

# Виклик функції
access_list_element()


def convert_to_number():
    try:
        user_input = input("Введіть число: ")
        number = float(user_input)
        print(f"Введене число: {number}")
    except ValueError:
        print("Помилка: Введений рядок не може бути перетворений у число.")

# Виклик функції
convert_to_number()
