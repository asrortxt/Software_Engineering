class Shape:
    def area(self):
        pass

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