def val_checker(lambda_f):
    def val_checker2(func):
        def dec_func(*args):
            for x in args:
                if lambda_f(x):
                    print(func(x))
                else:
                    raise ValueError(f'incorrect value: {x}')
        return dec_func
    return val_checker2


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


calc_cube(5, 10, 8)
