import math
while True:
    operation = int(input('\nВыберите математическую операцию: \nСложение -- 1\nВычитание -- 2\nУмножение -- 3\nДеление -- 4\nВозведение в степень -- 5\nВычисление квадратного корня -- 6\nВычисление синуса -- 7\nВычисление косинуса -- 8\nВычисление тангенса -- 9\nВычисление факториала -- 10\n'))
    if operation == 1:
        try:
            first_number = int(input('Введите первое число: '))
            second_number = int(input('Введите второе число: '))
            result = first_number + second_number
        except:
            print('Вы ввели не число!')
            result = None
    elif operation == 2:
        try:
            first_number = int(input('Введите первое число: '))
            second_number = int(input('Введите второе число: '))
            result = first_number - second_number
        except:
            print('\nВы ввели не число!')
            result = None
    elif operation == 3:
        try:
            first_number = int(input('Введите первое число: '))
            second_number = int(input('Введите второе число: '))
            result = first_number * second_number
        except:
             print('\nВы ввели не число!')
             result = None
    elif operation == 4:
        try:
            first_number = int(input('Введите первое число: '))
            second_number = int(input('Введите второе число: '))
            if second_number == 0:
                result = None
                print('Деление на ноль невозможно')
            else:
                result = float(first_number / second_number)
        except:
             print('\nВы ввели не число!')
             result = None
    elif operation == 5:
        try:
            first_number = int(input('Введите первое число: '))
            second_number = int(input('Введите второе число: '))
            result = first_number ** second_number
        except:
             print('\nВы ввели не число!')
             result = None
    elif operation == 6:
        try:
            number = int(input('Введите число: '))
            if number >= 0:
                sqrt = number ** (0.5)
                result = sqrt
            else:
                result = None
                print('Корень из отрицательного числа не существует')
        except:
            print('\nВы ввели не число!')
            result = None
    elif operation == 7:
        try:
            number = int(input('Введите число: '))
            result = math.sin(number)
        except:
            print('\nВы ввели не число!')
            result = None
    elif operation == 8:
        try:
            number = int(input('Введите число: '))
            result = math.cos(number)
        except:
            print('\nВы ввели не число!')
            result = None
    elif operation == 9:
        try:
            number = int(input('Введите число: '))
            result = math.tan(number)
        except:
            print('\nВы ввели не число!')
            result = None
    elif operation == 10:
        try:
            number = int(input('Введите число: '))
            if number >= 0:
                result = math.factorial(number)
            else:
                result = None
                print('Факториал нельзя посчитать из отрицательного числа')
        except:
            print('\nВы ввели не число!')
            result = None
    elif operation == 11:
        print('Калькулятор завершил свою работу!')
        break
    print('Ответ:', result, '\nНапишите 11 для завершения работы калькулятора')
