"""
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
"""

class Worker:

    def __init__(self, name='Tolik', surname='Karpov', position='chess playes', wage=1500, bonus=200):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

n_person = Position('Shota', 'Rustaveli', 'poet', 1600, 300)
print(f'New attributes are: {n_person.name}, {n_person.surname}, {n_person.position}, {n_person._income}')
print(f'Total salary of {n_person.get_full_name()} is {n_person.get_total_income()}')