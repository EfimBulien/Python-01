import math
while True:
    operation = int(input('Выберите математическую операцию: \nСложение -- 1\nВычитание -- 2\nУмножение -- 3\nДеление -- 4\nВозведение в степень -- 5\nВычисление квадратного корня -- 6\nВычисление синуса -- 7\nВычисление косинуса -- 8\nВычисление тангенса -- 9\nВычисление факториала -- 10\n'))
    if operation == 1:
        first_number = int(input('Введите первое число: '))
        second_number = int(input('Введите второе число: '))
        result = first_number + second_number
    elif operation == 2:
        first_number = int(input('Введите первое число: '))
        second_number = int(input('Введите второе число: '))
        result = first_number - second_number
    elif operation == 3:
        first_number = int(input('Введите первое число: '))
        second_number = int(input('Введите второе число: '))
        result = first_number * second_number
    elif operation == 4:
        first_number = int(input('Введите первое число: '))
        second_number = int(input('Введите второе число: '))
        if second_number == 0:
            result = None
            print('Деление на ноль невозможно')
        else:
            result = float(first_number / second_number)
    elif operation == 5:
        number = int(input('Введите число: '))
        stepen = int(input('Введите степень: '))
        result = number ** stepen
    elif operation == 6:
        number = int(input('Введите число: '))
        if number >= 0:
            sqrt = number ** (0.5)
            result = sqrt
        else:
            result = None
            print('Корень из отрицательного числа не существует')
    elif operation == 7:
        number = int(input('Введите число: '))
        result = math.sin(number)
    elif operation == 8:
        number = int(input('Введите число: '))
        result = math.cos(number)
    elif operation == 9:
        number = int(input('Введите число: '))
        result = math.tan(number)
    elif operation == 10:
        number = int(input('Введите число: '))
        result = math.factorial(number)
    elif operation == 11:
        print('Калькулятор завершил свою работу!')
        break
    print('Ответ:', result, '\nНапишите 11 для завершения работы калькулятора')