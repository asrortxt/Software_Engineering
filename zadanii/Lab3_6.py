string = 'Привет всем изучающии Python!'
value = input()
for i in string:
    index = string.find(value)
    print(f"Буква'{value}' есть в строке под {index} индексом")
    break
else:
    print(f"Буквы '{value}' нет в указанной строке")