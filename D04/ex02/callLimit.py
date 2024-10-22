# Un fonction-décorateur est une fonction qui permet de modifier
# le comportement d'une autre fonction sans changer son code source.
# dans le code on l'appelle avec @callLimit
# Un décorateur prend une fonction en argument, et retourne une nouvelle
# fonction qui "encapsule" l'ancienne
# Les wrappers (ou "fonctions enveloppantes") sont les fonctions internes
# d'un décorateur qui ajoutent des comportements supplémentaires à la
# fonction décorée.

def callLimit(limit: int):
    """A function that takes an int limit as an argument"""
    if not isinstance(limit, int):
        raise TypeError("Limit must be an int")

    def callLimiter(function):
        """A decorator function that limits the number of times
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
