def convert(a):
    if a < 6:
        return str(a)
    else:
        return convert(a // 6) + str(a % 6)

number = input("Введите десятичное целое положительное число: ")

if number.isdigit():
    number = int(number)
    print(f"Результат(шестеричная система счисления): {convert(number)}")
else:
    print("Ошибка! Для реализации программы необходимо ввести целое положительное число.")
