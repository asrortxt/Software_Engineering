class InvalidDataFormatException(Exception):
    """
    Пользовательское исключение для неверного формата данных
    """

    def __init__(self, message="Неверный формат данных"):
        self.message = message
        super().__init__(self.message)


def validate_email(email):
    """
    Функция для проверки формата email адреса
    """
    print(f"Проверка email: {email}")

    if not isinstance(email, str):
        raise InvalidDataFormatException("Email должен быть строкой")

    if '@' not in email:
        raise InvalidDataFormatException("Email должен содержать символ '@'")

    if '.' not in email.split('@')[-1]:
        raise InvalidDataFormatException("Email должен содержать домен с точкой")

    print("✓ Email прошел валидацию")
    return True


def validate_age(age):
    """
    Функция для проверки возраста пользователя
    """
    print(f"Проверка возраста: {age}")

    if not isinstance(age, int):
        raise InvalidDataFormatException("Возраст должен быть целым числом")

    if age < 0:
        raise InvalidDataFormatException("Возраст не может быть отрицательным")

    if age > 150:
        raise InvalidDataFormatException("Возраст не может превышать 150 лет")

    print("✓ Возраст прошел валидацию")
    return True


def process_user_data(email, age):
    """
    Основная функция обработки данных пользователя
    """
    try:
        validate_email(email)
        validate_age(age)
        print(f"\n✅ Данные пользователя приняты: {email}, {age} лет")
        return True

    except InvalidDataFormatException as e:
        print(f"\n❌ Ошибка валидации: {e}")
        return False
    except Exception as e:
        print(f"\n⚠️ Неожиданная ошибка: {e}")
        return False


# Тестирование
if __name__ == '__main__':
    print("=== ТЕСТИРОВАНИЕ ПОЛЬЗОВАТЕЛЬСКОГО ИСКЛЮЧЕНИЯ ===\n")

    # Тест 1: Корректные данные
    print("ТЕСТ 1 - Корректные данные:")
    process_user_data("user@example.com", 25)

    print("\n" + "=" * 50 + "\n")

    # Тест 2: Неверный email
    print("ТЕСТ 2 - Неверный формат email:")
    process_user_data("invalid-email", 30)

    print("\n" + "=" * 50 + "\n")

    # Тест 3: Неверный возраст
    print("ТЕСТ 3 - Неверный возраст:")
    process_user_data("test@domain.com", -5)

    print("\n" + "=" * 50 + "\n")

    # Тест 4: Неверный тип данных
    print("ТЕСТ 4 - Неверный тип данных:")
    process_user_data(123, "25")  # Число вместо email, строка вместо возраста