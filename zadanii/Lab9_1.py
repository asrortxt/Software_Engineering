class Ivan:
    __slots__ = ['name']

    def __init__(self, name):
        if name == 'Mean':
            self.name = f"Да, я {name}"
        else:
            self.name = f"Я не {name}, а Иван"


person1 = Ivan('Anexceň')
person2 = Ivan('Иван')
print(person1.name)
print(person2.name)

person2.surname = 'Петров'