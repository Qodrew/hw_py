
'''Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения count_elements-го члена прогрессии: an = element_1 + (count_elements-1) * def_elements.
 Каждое число вводится с новой строки.'''



element_1= int(input("Введите значение 1-го элемента:"))
def_elements=int(input("Введите разность элементов:"))
count_elements=int(input("Введите количество элементов:"))
res = [element_1 + (i - 1) * def_elements for i in range(1, count_elements + 1)]
print(*res)