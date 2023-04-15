"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

*Попытайтесь получить кодовые точки без онлайн-конвертера!
без хардкода!

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции
"""

string1 = 'разработка'
string2 = 'сокет'
string3 = 'декоратор'

print(type(string1))
print(type(string2))
print(type(string3))

string1_utf8 = b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'
string2_utf8 = b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82'
string3_utf8 = b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80'


print(type(string1_utf8))
print(type(string2_utf8))
print(type(string3_utf8))

print(string1_utf8.decode())
print(string2_utf8.decode())
print(string3_utf8.decode())

show_size(string1)
show_size(string1_utf8)
