# Тема 7. Работа с файлами (ввод, вывод)
Отчет по Теме #7 выполнил
- Тураев Асрорбек Ахрор угли
- ИВТ-23-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | - |
| Задание 2 | + | - |
| Задание 3 | + | - |
| Задание 4 | + | - |
| Задание 5 | + | - |
| Задание 6 | + | - |
| Задание 7 | + | - |
| Задание 8 | + | - |
| Задание 9 | + | - |
| Задание 10 | + | - |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Составьте текстовый файл и положите его в одну директорию с программой Python. Текстовый файл должен состоять минимум из двух строк.

```
Hello students!
Lets talk about work with files on python
```
### Результат
![Mеню](https://github.com/asrortxt/Software_Engineering/blob/Тема_7/pic/Lab7_1.png)

## Выводы

Создан текстовый документ для дальнейшей работы.

## Лабораторная работа №2
### Напишите программу, которая выводит только первую строку из вашего файла, при этом используйте конструкцию open()/close().

```python
f = open ('input.txt' , 'r')
print(f.readline())
f.close()
```
### Результат
![Меню](https://github.com/asrortxt/Software_Engineering/blob/Тема_7/pic/Lab7_2.png)

## Выводы

В данном коде:
1. f = open('input.txt', 'r') - открывает файл 'input.txt' в режиме чтения и создает файловый объект.
2. print(f.readline()) - извлекает первую строку из открытого файла и отображает ее содержимое.
3. f.close() - закрывает файл.

## Лабораторная работа №3
### Напишите программу, которая выводит все строки из вашего файла в массив, при этом используйте конструкцию open()/close().

```python
f = open ('input.txt', 'r')
print(f.readlines())
f.close()
```
### Результат
![Меню](https://github.com/asrortxt/Software_Engineering/blob/Тема_7/pic/Lab7_3.png)

## Выводы

print(f.readlines()) - считывает все строки из файла в виде списка (массива) и выводит его на экран.

## Лабораторная работа №4
### Напишите программу, которая выводит все строки из вашего файла в массив, при этом используйте конструкцию with open().

```python
with open('input.txt') as f:
  print(f.readlines())
```
### Результат
![Меню](https://github.com/asrortxt/Software_Engineering/blob/Тема_7/pic/Lab7_4.png)

## Выводы

with open('input.txt') as f: - открывает файл 'input.txt' в режиме чтения по умолчанию.

## Лабораторная работа №5
### Напишите программу, которая выводит каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().

```python
with open('input.txt') as f:
    for line in f:
        print(line)
```
### Результат
![Меню](https://github.com/asrortxt/Software_Engineering/blob/Тема_7/pic/Lab7_5.png)

## Выводы

В данном коде:
1.with open('input.txt') as f: - инициализирует работу с файлом через менеджер контекста, обеспечивая автоматическое управление ресурсами.
2. for line in f: - последовательно обрабатывает каждую текстовую строку файла в цикле чтения.

## Лабораторная работа №6
### Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.

```python
with open('input.txt', 'a') as f:
    f.write('\nIm additional time')

with open('input.txt', 'r') as f:
    result = f.readlines()
    print(result)
```
### Результат
![Меню](https://github.com/asrortxt/Software_Engineering/blob/Тема_7/pic/Lab7_6.png)

## Выводы

В данном коде:
1. with open('input.txt', 'a') as f: - открывает файл в режиме добавления ('a' - append).
2. f.write('\nIm additional time') - добавляет новую строку в конец файла (с символом переноса \n).
3. with open('input.txt', 'r') as f: - повторно открывает файл в режиме чтения.
4. esult = f.readlines() - считывает все строки файла в список

## Лабораторная работа №7
### Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить что изменения вами информация сохранилась в файле.

```python
lines = ['one', 'two', 'three']
with open('input.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run' + line)
    print('Done!')
```
### Результат
![Меню](https://github.com/asrortxt/Software_Engineering/blob/Тема_7/pic/Lab7_7.png)

## Выводы

В данном коде:
1. lines = ['one', 'two', 'three'] - создает произвольный список с данными для записи.
2. with open('input.txt', 'w') as f: - открывает файл в режиме записи ('w' - write), который перезаписывает всё содержимое файла.
3. for line in lines: - итерируется по элементам списка.
4. f.write('\nCycle run' + line) - записывает каждую строку в файл, добавляя префикс "Cycle run".

## Лабораторная работа №8
### Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).

```python
import os

def print_docs(directory):
    all_lines = os.walk(directory)
    for catalog in all_lines:
        print(f'Папка {catalog[0]} содержит:')
    print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
    print(f'Файл: {", ".join([file for file in catalog[2]])}')
    print('-' * 40)

print_docs(r'C:\Program Files\McAfee\CoreUI\scripts\dto')
```
### Результат
![Меню](https://github.com/asrortxt/Software_Engineering/blob/Тема_7/pic/Lab7_8.png)

## Выводы

В данном коде:
1.import os - подключает модуль для взаимодействия с функциями операционной системы.
2. def print_docs(directory): - объявляет функцию для вывода содержимого директории.
3. all_lines = os.walk(directory) - получает генератор для обхода дерева каталогов.
4. for catalog in all_lines: - итерируется по результатам os.walk().
5. print(f'Папка {catalog[0]} содержит:') - отображает абсолютный путь к текущей обрабатываемой директории.

## Лабораторная работа №9
### Документ «input.txt» содержит следующий текст:
Приветствие
Спасибо
Извините
Пожалуйста
До свидания
Ты готов?
Как дела?
С днем рождения!
Удача!
Я тебя люблю.
Требуется реализовать функцию, которая выводит слово, имеющее
максимальную длину (или список слов, если таковых несколько).
Проверьте работоспособность программы на своем наборе данных

```python
def longest_words(file):
    with open(file, encoding='utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_words = word

        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words

print(longest_words('input.txt'))
```
### Результат
![Меню](https://github.com/asrortxt/Software_Engineering/blob/Тема_7/pic/Lab7_9.png)

## Выводы

В данном коде:
1. with open(file, encoding='utf-8') as f: - осуществляет открытие файла с использованием кодировки UTF-8 для корректного чтения текста.
2.words = f.read().split() - считывает полное содержимое файла и разделяет его на отдельные слова по пробельным символам.
3. max_length = len(max(words, key=len)) - определяет максимальную длину слова среди всех элементов списка.
4. for word in words: - выполняет перебор каждого слова из полученного списка для анализа их длины.
5. if len(word) == max_length: - проверяет, соответствует ли текущее слово максимальной длине

## Лабораторная работа №10
### Требуется создать csv-файл «rows_300.csv» со следующими столбцами:
№ - номер по порядку (от 1 до 300);
Секунда – текущая секунда на вашем ПК;
Микросекунда – текущая миллисекунда на часах.
Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.

```python
import csv
import datetime
import time

with open ('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', ' Скунда ', 'Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second,
                         datetime.datetime.now().microsecond])

        time.sleep(0.01)
```
### Результат
![Меню](https://github.com/asrortxt/Software_Engineering/blob/Тема_7/pic/Lab7_10.png)

## Выводы

В данном коде:
1. Импорт модулей - csv для работы с CSV-файлами, datetime для времени, time для задержек.
2. with open ('rows_300.csv', 'w', encoding='utf-8', newline='') as f: - создает CSV-файл в режиме записи.
3. writer = csv.writer(f) - создает объект для записи CSV данных.
4. writer.writerow(['№', ' Скунда ', 'Микросекунда']) - записывает заголовки столбцов.
5. or line in range(1, 301): - цикл от 1 до 300 включительно.
6. datetime.datetime.now().second - получает текущую секунду.
7. datetime.datetime.now().microsecond - получает текущую микросекунду.
8. time.sleep(0.01) - приостанавливает выполнение на 0.01 секунды.

