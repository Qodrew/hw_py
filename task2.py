#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def calculator(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError as e:
        print(f'Вы что? Пытаетесь делить на 0?!')

print(calculator(int(input('Введите первое число: ')), int(input('Введите второе число: '))))