#  Выяснить тип результата выражений:
# 15 * 3
# 15 / 3
# 15 // 2
# 15 ** 2

#а
a = 15 * 3
b = 15 / 3
c = 15 // 2
d = 15 ** 2
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))


#b
my_list = [a, b, c, d]
a = 15 * 3
b = 15 / 3
c = 15 // 2
d = 15 ** 2
for num in my_list:
    if type(num) is int:
        print(f'{num} int')
    else:
        print(f'{num} float')


#c
my_list = [15 * 3, 15 / 3, 15 // 2, 15 ** 2]
for num in my_list:
    if type(num) is int:
        print(f'{num} int')
    else:
        print(f'{num} float')


#d
my_list = [a, b, c, d]
a = 15 * 3
b = 15 / 3
c = 15 // 2
d = 15 ** 2
for num in my_list:
    print(type(num))


