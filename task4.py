#Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

print('------используя sort()------ \n')
args = (
    int(input('Введите первый аргумент: ')),
    int(input('Введите второй аргумент: ')),
    int(input('Введите третий аргумент: ')),
)
print(sorted(args, reverse=True))
args_1 = (sorted(args, reverse=True))

def sum(args_1):
    return args_1[0] + args_1[1]

print(f'Сумма наибольших двух аргументов: {sum(args_1)} \n')

print('------не используя sort()------ \n')

def my_func(arg_1, arg_2, arg_3):
    print(f' \n Сумма наибольших двух аргументов равна: '
          f'{(arg_1 + arg_2 + arg_3) - min([arg_1, arg_2, arg_3])}')

my_func(
    int(input('Введите первый аргумент: ')),
    int(input('Введите второй аргумент: ')),
    int(input('Введите третий аргумент: ')),
)