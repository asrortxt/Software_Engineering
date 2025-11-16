def read_file_data(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.read().strip()

        if not data:
            raise ValueError("Файл пустой")

        print(f"Данные из файла: {data}")
        return data

    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден")
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
    finally:
        print("Обработка файла завершена")


# Тестирование
if __name__ == '__main__':
    print("=== Тест 1: Файл с данными ===")
    read_file_data("data.txt")

    print("\n=== Тест 2: Пустой файл ===")
    read_file_data("empty.txt")

    print("\n=== Тест 3: Несуществующий файл ===")
    read_file_data("nonexistent.txt")