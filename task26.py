'''Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.'''

def recApowB(a, b):
    if (a > 0 and b > 0): 
        return a * recApowB(a, b - 1)
    if b == 0:
        return 1
    

number = int(input('Введите число: '))
degree = int(input('Введите степень: '))
print(recApowB(number, degree))