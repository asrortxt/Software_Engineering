# Тема 8. Основы объектно-ориентированного программирования
Отчет по Теме #8 выполнил
- Тураев Асрорбек Ахрор угли
- ИВТ-23-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | - |
| Задание 2 | + | - |
| Задание 3 | + | - |
| Задание 4 | + | - |
| Задание 5 | + | - |
| Задание 6 | - | - |
| Задание 7 | - | - |
| Задание 8 | - | - |
| Задание 9 | - | - |
| Задание 10 | - | - |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Создайте класс “Car” с атрибутами производитель и модель. Создайте объект этого класса. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями.

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

my_car = Car("Toyota", "Corolla")
```
### Результат
![Mеню](https://github.com/asrortxt/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pic/Lab8_1.PNG)

## Выводы
В данном коде:
1. class Car: - объявляет новый класс с именем "Car".
2. def __init__(self, make, model): - определяет конструктор класса, который автоматически вызывается при создании нового объекта.
3. self.make = make - создает атрибут "make" у объекта и присваивает ему значение из параметра make.
4. self.model = model - создает атрибут "model" у объекта и присваивает ему значение из параметра model.
5. my_car = Car("Toyota", "Corolla") - создает экземпляр (объект) класса Car с конкретными значениями атрибутов.

## Лабораторная работа №2
### Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину “поехать”. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving the {self.make} {self.model}")

my_car = Car("toyota", "Cororlla")
my_car.drive()
```
### Результат
![Меню](https://github.com/asrortxt/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pic/Lab8_2.PNG)

## Выводы
В данном коде:
1. def drive(self): - объявляет метод drive, который принимает параметр self (ссылку на текущий объект).
2. print(f"Driving the {self.make} {self.model}") - выводит форматированную строку с использованием атрибутов make и model объекта.
3. my_car.drive() - вызывает метод drive для объекта my_car, что приводит к выполнению кода внутри метода.

## Лабораторная работа №3
### Создайте новый класс “ElectricCar” с методом “charge” и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
from Lab8_2 import Car
class ElectroCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make,model)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")

my_electronic_car = ElectroCar("Tesla", "Model S", 75)
my_electronic_car.drive()
my_electronic_car.charge()
```
### Результат
![Меню](https://github.com/asrortxt/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pic/Lab8_3.PNG)

## Выводы
В данном коде:
1. from Lab8_2 import Car - импортирует класс Car из файла Lab8_2.py.
2. def __init__(self, make, model, battery_capacity): - определяет конструктор класса ElectroCar с тремя параметрами.
3. self.battery_capacity = battery_capacity - создает новый атрибут battery_capacity, специфичный для ElectroCar.
4. def charge(self): - объявляет метод charge для зарядки электромобиля.
5. my_electronic_car.drive() - вызывает унаследованный метод drive из родительского класса Car.
6. my_electronic_car.charge() - вызывает метод charge, определенный в классе ElectroCar.

## Лабораторная работа №4
### Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car:
    def __init__(self, make, model):
        self._make = make # Защищенный атрибут
        self.__model = model # Приватный атрибут

    def drive(self):
        print(f"Driving the {self._make} {self.__model}")


my_car = Car("Toyota", "Corolla")
print(my_car._make) # Доступ к защищенному атрибуту
my_car.drive()
```
### Результат
![Меню](https://github.com/asrortxt/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pic/Lab8_4.PNG)

## Выводы
В данном коде:
1. self._make = make - создает защищенный атрибут производителя (одно подчеркивание).
2. self.__model = model - создает приватный атрибут модели (два подчеркивания).
3. print(my_car._make) - обращается к защищенному атрибуту извне класса.

## Лабораторная работа №5
### Реализуйте полиморфизм создав основной (общий) класс “Shape”, а также еще два класса “Rectangle” и “Circle”. Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

rect = Rectangle(5, 4) # Создан экземпляр класса Rectangle с шириной 5 и высотой 4
circle = Circle(3) # Создан экземпляр класса Circle с радиусом 3

print(rect.area()) # Вызов метода area() для прямоугольника и вывод результата
print(circle.area()) # Вызов метода area() для круга и вывод результата
```
### Результат
![Меню](https://github.com/asrortxt/Software_Engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pic/Lab8_5.PNG)

## Выводы
В данном коде:
1. def __init__(self, width, height): - конструктор класса Rectangle, инициализирует ширину и высоту.
2. self.width = width - создает атрибут width для хранения ширины прямоугольника и self.height = height - создает атрибут height для хранения высоты прямоугольника.
3. def area(self): - метод для вычисления площади прямоугольника.
4. rect = Rectangle(5, 4) - создает объект прямоугольника с шириной 5 и высотой 4.
5. circle = Circle(3) - создает объект круга с радиусом 3.
6. print(rect.area()) - вычисляет и выводит площадь прямоугольника.
7. print(circle.area()) - вычисляет и выводит площадь круга.
