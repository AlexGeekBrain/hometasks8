from functools import wraps


def val_checker(l_func):
    def _val_checker(func):

        @wraps(func)
        def wrapper(number):
            if l_func(number):
                print(func(number))
            else:
                raise ValueError(f'wrong val {number}')

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


try:
    print(calc_cube(int(input('Введите число: '))))
except ValueError as error:
    print(error)
