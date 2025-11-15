def add_two():
    try:
        user_input = input("Введите число: ")
        number = float(user_input)
        result = 2 + number
        print(f"Результат: 2 + {number} = {result}")
        return result

    except ValueError:
        print("Ошибка: Неподходящий тип данных. Ожидалось число.")


# Тестирование
if __name__ == '__main__':
    print("=== Тест 1: Корректный ввод (целое число) ===")
    add_two()

    print("\n=== Тест 2: Корректный ввод (дробное число) ===")
    add_two()

    print("\n=== Тест 3: Некорректный ввод (строка) ===")
    add_two()

    print("\n=== Тест 4: Некорректный ввод (спецсимволы) ===")
    add_two()