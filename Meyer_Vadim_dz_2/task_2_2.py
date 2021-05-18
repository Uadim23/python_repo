# Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём до двух разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Новый список не создавать! Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов

list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#print(dir(list))
num = 0
for i in range(len(list)):
    i += num
    if list[i][-1].isdigit():
        if list[i][0] in '+-':
            list[i] = f'{list[i][0]}{int(list[i]):02}'
        else:
            list[i] = f'{int(list[i]):02}'
        list.insert(i, '"')
        list.insert(i + 2, '" ')
        num += 2
    else:
        list[i] = f'{list[i]} '

print(list)
print(''.join(list))