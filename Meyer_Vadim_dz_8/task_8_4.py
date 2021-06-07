# Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать
# исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
# Примечание: сможете ли вы замаскировать работу декоратора?

def val_checker(func_1):
    def _val_checker(func_2):
        def wrapper(number):
            if func_1(number):
                print(func_2(number))
            else:
                raise ValueError(f"wrong val {number}")

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


try:
    b = calc_cube(3)
except ValueError as err:
    print(err)