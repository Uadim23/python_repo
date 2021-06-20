#Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при хранении
#данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая. Написать код,
#загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить
#словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
#задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём
#данных в файлах во много раз меньше объема ОЗУ.
#Фрагмент файла с данными о пользователях (users.csv):
#Иванов,Иван,Иванович
#Петров,Петр,Петрович
#Фрагмент файла с данными о хобби (hobby.csv):
#скалолазание,охота
#горные лыжи

from itertools import zip_longest
from json import dump

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:

        if len(users.readline()) > len(hobby.readline()):
            with open('merge', "w", encoding='utf-8') as f:
                all_lst = zip_longest((' '.join(user.strip().split(',')) for user in users), hobby, fillvalue=None)
                my_dict = dict((rows[0], rows[1].strip()) for rows in all_lst)

                dump(my_dict, f, ensure_ascii=False, indent=4)
            print(my_dict)
        else:
            exit(1)