# Un fonction-décorateur est une fonction qui permet de modifier
# le comportement d'une autre fonction sans changer son code source.
# dans le code on appelle avec @callLimit

def callLimit(limit: int):
    """A decorator function that takes a int limit as an argument"""
    if not isinstance(limit, int):
        raise TypeError("Limit must be an int")

    def callLimiter(function):
        """A decorator inner function that limits the number of times
        a function can be called."""

        count = 0
        if not callable(function):  # Vérifie que 'function' est callable
            raise TypeError(f"{function} n'est pas une fonction valide.")

        def limit_function(*args: any, **kwargs: any):
            """A wrapper function that checks if the decorated function
            has been called fewer times than the limit."""
            nonlocal count
            try:
                if count < limit:
                    count += 1
                    return function(*args, **kwargs)
                else:
                    raise RuntimeError(f'{repr(function)} call too many times')
            except Exception as e:
                print(f"Error: {e}")

        return limit_function

    return callLimiter
