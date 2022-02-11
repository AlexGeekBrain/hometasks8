from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        n_list = [num for num in (*args, *kwargs.values())]
        result = [f'{func.__name__}({num}: {type(num)})' for num in n_list]
        print(*result, *func(*args, **kwargs), sep=',\n')

    return wrapper


@type_logger
def calc_cube(*x, **y):
    n_list = [num for num in (*x, *y.values()) if isinstance(num, int) or isinstance(num, float)]
    return [i ** 3 for i in n_list]


calc_cube(5, 12.5, ui=7, ip=89.9, name='Aleksey')
print(calc_cube.__name__)
help(calc_cube)
