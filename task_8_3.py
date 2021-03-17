def type_logger(func):
    def log(*args, **kwargs):
        results = []
        print('args:')
        for arg in args:
            print(f'{arg}: {type(arg)}, ', end='')
            if type(arg) == int:
                results.append(func(arg))
        print('\nkwargs:')
        for key in kwargs:
            print(f'key: {key} : {type(key)}, value: {kwargs[key]} : {type(kwargs[key])}, ', end='')
            if type(kwargs[key]) == int:
                results.append(func(kwargs[key]))
        print('\nresults:')
        for result in results:
            print(f'{result}: {type(result)}, ', end='')
    return log


@type_logger
def calc_cube(x):
    return x ** 3


calc_cube(1, {'num': 3}, (2, 'name'), {8, 5}, [19, 3], 'str', firstname='Ivan')
