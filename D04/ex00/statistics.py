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
    sorted_list = sorted(values)
    n = len(values)
    if n == 0:
        print('ERROR')
    elif n % 2 == 1:
        print(f'median : {sorted_list[(int(n / 2))]}')
    else:
         print(f'median : {((sorted_list[(n / 2) - 1] + sorted_list[(n / 2)]) / 2)}')
    return 


def quartile(values: list):
    """Print the 25% and 75% quartile"""
    sorted_list = sorted(values)
    n = len(values)
    if n == 0:
        print('ERROR')
    elif n == 1:
        print(f'quartile : {[sorted_list[0], sorted_list[0]]}')
    elif n == 2 or n == 3:
        print(f'quartile : {[sorted_list[0], sorted_list[1]]}')
    else:
        if n % 2 == 1:
            print(f'quartile : {[sorted_list[int(n / 4)], sorted_list[int(n *(3/ 4))]]}')
        else:
            first = float(((sorted_list[(n / 4) - 1]) + sorted_list[(n *(3/ 4))]) / 2)
            third = float(((sorted_list[(n / 4) - 1]) + sorted_list[(n *(3/ 4))]) / 2)
            print(f'quartile : [{first:.1f}, {third:.1f}]')
    return


def std(values: list):
    print('std')
    return


def var(values: list):
    print('var')
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
        operations = {'mean': mean, 'median': median, 'quartile':quartile, 'std': std, 'var': var}
        for cle,valeur in kwargs.items():
            if valeur in operations:
                operations[valeur](args)
            
            '''
            elif valeur == "median":
                median(args)
            elif valeur == "quartile":
                quartile(args)
            elif valeur == "std":
                quartile(args)
            elif valeur == "quartile":
                quartile(args)
            '''
            
    except Exception as e:
        print(f"Une erreur est survenue : {e}")