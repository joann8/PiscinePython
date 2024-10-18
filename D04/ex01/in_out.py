def square(x: int | float) -> int | float:
    """returns the square of a number"""
    if not isinstance(x, (int, float)):
        raise TypeError("x must be an int or a float")
    return x ** 2


def pow(x: int | float) -> int | float:
    """returns the exponentiation of a number by himself"""
    if not isinstance(x, (int, float)):
        raise TypeError("x must be an int or a float")
    return x ** x


# La structure ci dessous est souvent utilisée dans les décorateurs ou
# dans les fonctions qui conservent un état entre différents appels.
# Le mot-clé nonlocal est essentiel ici pour permettre à la fonction
# interne d'accéder et de modifier les variables de la fonction englobante,
# créant ainsi un effet de fermeture (closure).

def outer(x: int | float, function) -> object:
    """Returns an object that, when called, returns the result of the
    arguments calculation.
    """

    count = 0
    if not callable(function):  # Vérifie que 'function' est bien une fonction
        raise TypeError(f"{function} n'est pas une fonction valide.")

    def inner() -> float:
        """
        Returns the result of the arguments calculation.
        """
        nonlocal x, count
        try:
            count += 1
            # chaque fois que inner est appelée, elle modifie x en appliquant
            # la fonction sdéfinie dans outer.s
            x = function(x)
        except Exception as e:
            print(f"Error: {e}")
        return x
    return inner
