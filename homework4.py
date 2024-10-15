a = input("Введите целое число a: ")
b = input("Введите целое число b: ")
c = input("Введите целое число c: ")

error = False

if not a.isdigit():
    print("Ошибка! 'a' должно быть целым числом.")
    error = True

if not b.isdigit():
    print("Ошибка! 'b' должно быть целым числом.")
    error = True

if not c.isdigit():
    print("Ошибка! 'c' должно быть целым числом.")
    error = True

if not error:
    a = int(a)
    b = int(b)
    c = int(c)
    r = x = 3 * a + 3 - b + 4 * c
    print(f"Результат в десятичной системе: {r}")