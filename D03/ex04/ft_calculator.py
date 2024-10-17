class calculator:
    """
    A calculator class that is able to do calculations
    (addition, multiplication, subtraction, division)
    of two vectors of the same size.
    """
    def __init__(self):
        """ Initialization of the calculator"""

    # a @staticmethod decorator in Python allows a method to be called
    # on the class itself rather than on an instance of the class.
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Multiplication of two vectors"""
        res = sum(v1 * v2 for v1, v2 in zip(V1, V2))
        print(f"Dot product is: {res}")
        return None

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Addition of two vectors"""
        res = [float(v1 + v2) for v1, v2 in zip(V1, V2)]
        print(f"Add vector is: {res}")
        return None

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtraction of two vectors"""
        res = [float(v1 - v2) for v1, v2 in zip(V1, V2)]
        print(f"Sous vector is: {res}")
        return None
