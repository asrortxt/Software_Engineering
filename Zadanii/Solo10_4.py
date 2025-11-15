import time
import random
import time
import random


class RetryDecorator:
    """
    Декоратор для повторного выполнения функции при возникновении исключений
    """

    def __init__(self, max_attempts=3, delay=1):
        self.max_attempts = max_attempts
        self.delay = delay

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for attempt in range(self.max_attempts):
                try:
                    print(f"Попытка {attempt + 1} выполнить {func.__name__}...")
                    result = func(*args, **kwargs)
                    print(f"Функция {func.__name__} выполнена успешно!")
                    return result
                except Exception as e:
                    print(f"Ошибка: {e}")
                    if attempt < self.max_attempts - 1:
                        print(f"Повторная попытка через {self.delay} секунду...")
                        time.sleep(self.delay)
                    else:
                        print(f"Все {self.max_attempts} попыток исчерпаны!")
                        raise

        return wrapper  # ← ЭТУ СТРОКУ НУЖНО ВЫНЕСТИ ИЗ ЦИКЛА


# Первая функция - имитация ненадежного сетевого запроса
@RetryDecorator(max_attempts=3, delay=2)
def unstable_network_request(url):
    """
    Имитирует ненадежный сетевой запрос, который часто падает
    """
    if random.random() < 0.7:  # 70% вероятность ошибки
        raise ConnectionError(f"Не удалось подключиться к {url}")
    return f"Данные с {url} получены успешно"


# Вторая функция - работа с файлом, который может быть заблокирован
@RetryDecorator(max_attempts=2, delay=1)
def read_locked_file(filename):
    """
    Имитирует чтение файла, который может быть временно заблокирован
    """
    if random.random() < 0.6:  # 60% вероятность ошибки
        raise PermissionError(f"Файл {filename} заблокирован для чтения")
    return f"Содержимое файла {filename} прочитано"


# Тестирование
if __name__ == '__main__':
    print("=== Тестирование декоратора RetryDecorator ===\n")

    print("1. Тестирование unstable_network_request:")
    try:
        result = unstable_network_request("https://api.example.com/data")
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Итоговая ошибка: {e}")

    print("\n" + "=" * 50 + "\n")

    print("2. Тестирование read_locked_file:")
    try:
        result = read_locked_file("important_data.txt")
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Итоговая ошибка: {e}")