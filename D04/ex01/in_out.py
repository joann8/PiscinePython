def square(x: int | float) -> int | float:
    """returns the square of a number"""
    if not isinstance(x,(int, float)):
        print("x must be an int or a float")
        return None
    return x ** 2

def pow(x: int | float) -> int | float:
    """returns the exponentiation of a number by himself"""
    if not isinstance(x,(int, float)):
        print("x must be an int or a float")
        return None
    return x ** x


def outer(x: int | float, function) -> object:
    """Returns an object that, when called, returns the result of the
    arguments calculation.
    """
    count = 0
    def inner() -> float:
        """
        Returns the result of the arguments calculation.
        """
        nonlocal x, count
        # nonlocal portée englobante, permet de modifier ds une fonction
        # interne une variable definie dans une fonction externe
        count += 1
        x = function(x)
        return x
    return inner