# а)
my_list = []
for i in range(1, 1000, 2):
    my_list.append(i ** 3)
total = 0

for num in my_list:
    digit_sum = 0
    temp_number = num
    while (temp_number > 0):
        digit_sum += temp_number % 10
        temp_number //= 10
    if digit_sum % 7 == 0:
            total += num
print(total)

# б)
my_list = []
for i in range(1, 1000, 2):
    my_list.append(i ** 3)
total = 0

for num in my_list:
    digit_sum = 0
    temp_number = num + 17
    while (temp_number > 0):
        digit_sum += temp_number % 10
        temp_number //= 10
    if digit_sum % 7 == 0:
            total += num + 17
print(total)



