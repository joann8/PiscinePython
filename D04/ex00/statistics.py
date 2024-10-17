def mean(values: list):
    """Print the arithmetic mean"""
    n = len(values)
    if n == 0:
        print('ERROR')
    else:
        print(f'mean : {(sum([v for v in values])/ n)}')
    return


def median(values: list):
    """Print the median value"""
    s_lst = sorted(values)
    n = len(values)
    if n == 0:
        print('ERROR')
    elif n % 2 == 1:
        print(f'median : {s_lst[int(n / 2)]}')
    else:
        print(f'median : {(s_lst[int((n / 2) - 1)] + s_lst[int(n / 2)]) / 2}')
    return


def quartile(values: list):
    """Print the 25% and 75% quartile"""
    s_lst = sorted(values)
    n = len(values)
    if n == 0:
        print('ERROR')
    else:
        if n % 2 == 1:
            first = float(s_lst[int(n / 4)])
            third = float(s_lst[int(n * (3 / 4))])
        else:
            first = float((s_lst[int((n / 4) - 1)] + s_lst[int(n / 4)]) / 2)
            third = float((s_lst[int((n * (3 / 4)) - 1)] +
                           s_lst[int(n * (3 / 4))]) / 2)
        print(f'quartile : [{first:.1f}, {third:.1f}]')
    return


def std(values: list):
    """Print the standard deviation"""
    n = len(values)
    if n == 0:
        print('ERROR')
    else:
        if n == 1:
            std = 0
        else:
            mean = sum([v for v in values]) / n
            sum_squared_diff = sum((v - mean) ** 2 for v in values)
            std = (sum_squared_diff / n) ** 0.5
        print(f'std : {std}')
    return


def var(values: list):
    """Print the variance"""
    n = len(values)
    if n == 0:
        print('ERROR')
    else:
        if n == 1:
            var = 0
        else:
            mean = sum([v for v in values]) / n
            sum_squared_diff = sum((v - mean) ** 2 for v in values)
            var = sum_squared_diff / n
        print(f'var : {var}')
    return


def ft_statistics(*args: any, **kwargs: any) -> None:
    '''
    Statistics
    '''
    # *args capture les arguments positionnels sous forme de tuple.
    # **kwargs capture les arguments nommés sous forme de dictionnaire.
    try:
        if not all(isinstance(arg, (int, float)) for arg in args):
            raise ValueError("All args must be int or float")
        operations = {'mean': mean, 'median': median, 'quartile': quartile,
                      'std': std, 'var': var}
        for cle, valeur in kwargs.items():
            if valeur in operations:
                operations[valeur](args)
        return None

    except Exception as e:
        print(f"Une erreur est survenue : {e}")
