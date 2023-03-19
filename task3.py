#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
#Функция должна принимать параметры как именованные аргументы.
#Реализовать вывод данных о пользователе одной строкой.

def personal_data(name, lastname, yearOfBirth, city, email, phone):
    return print(f'{name} {lastname} {yearOfBirth} года рождения, '
                 f'проживает в городе {city}, email: {email}, Телефон: {phone}')


personal_data(
    name=input('Имя: '),
    lastname=input('Фамилия: '),
    yearOfBirth=input('Год Рождения: '),
    city=input('Город проживания: '),
    email=input('email: '),
    phone=input('phone: '),
)