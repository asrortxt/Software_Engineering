class MyClass:
    def __init__(self, value):
        self._value = value

    def set_value(self, value): # установка значения атрибута
        self._value = value

    def get_value(self): # получение значения атрибута
        return self._value

    def deL_value(self): # удаление атрибута
        del self._value

    value = property(get_value, set_value, deL_value, "Свойство value")

obj = MyClass(42)
print(obj.get_value())
obj.set_value(45)
print(obj.get_value())
obj.set_value(100)
print(obj.get_value())
obj.deL_value()
print(obj.get_value())