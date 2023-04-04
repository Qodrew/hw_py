"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), 
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). 
Результатом сложения должна быть новая матрица.
"""

class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        for row in self.list:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''
    
    def __add__(self, other):
        for i in range(len(self.list)):
            for i_2 in range(len(other.list[i])):
                self.list[i][i_2] = self.list[i][i_2] + other.list[i][i_2]
        return Matrix.__str__(self)


first_matrix = Matrix([[3, 1, 2], [1, 0, -1], [-2, -1, 1], [2, -1, 0]])
new_matrix = Matrix([[-2, 0, -2], [2, 1, 1], [0, 2, 2], [-2, -2, 3]])
print(first_matrix.__add__(new_matrix))