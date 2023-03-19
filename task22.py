'''Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.'''

countNum1=(int(input("Введите количество элементов 1 массива: ")))
num_list_1=[]
for i in range(countNum1):
    num_list_1.append(int(input(f"Введите {i+1} число: ")))

countNum2=(int(input("Введите количество элементов 2 массива: ")))
num_list_2 = []
for i in range(countNum2):
    num_list_2.append(int(input(f"Введите {i+1} число:")))

print(num_list_1)
print(num_list_2)

num_list3 = num_list_1+num_list_2

checked_nums_list = []
for i in num_list3:
    if num_list3.count(i) > 1 and i not in checked_nums_list:
        checked_nums_list.append(i)
print(sorted(checked_nums_list));