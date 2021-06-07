# Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения
# функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора?
# Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

from functools import wraps

def type_logger(func):
    @wraps(func)
    def tag_wrapper(*args, **kwargs):
        result = [el for el in (*args, *kwargs.values())]
        m = [f"{func.__name__}({el}: {type(el)})" for el in result]
        print(*m, *func(*args, **kwargs), sep="")

    return tag_wrapper

@type_logger
def calc_cube(*x, **y):
    result = [el for el in (*x, *y.values()) if isinstance(el, int) or isinstance(el, float)]
    return [i ** 3 for i in result]

a = calc_cube(5)
#print(calc_cube.__name__)
#help(calc_cube)