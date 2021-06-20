# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и
# не завершиться с ошибкой.

class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Делить на ноль нельзя!")


div = DivisionByNull(10, 100)
#print(DivisionByNull.divide_by_null(10, 0))
#print(DivisionByNull.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))

print(f"\n\n{'*' * 35} b\n")

class DivisionByNull(Exception):
    def __init__(self, txt):
        self.txt = txt

num = input("Введите делимое: ")
num_2 = input("Введите делитель: ")
try:
    num = int(num)
    num_2 = int(num_2)
    if num_2 == 0:
        raise DivisionByNull("На ноль делить не буду!!!")
except (ZeroDivisionError, DivisionByNull) as err:
    print(err)
else:
    print(num / num_2)