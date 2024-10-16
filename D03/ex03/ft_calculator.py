class calculator:
    """
    A calculator class that is able to do calculations
    (addition, multiplication, subtraction, division)
    of vector with a scalar.
    """
    def __init__(self, vector):
        """ Initialization of the calculator"""
        self.vector = vector

    def __add__(self, object) -> None:
        ''' Addition'''
        self.vector = [elmt + object for elmt in self.vector]
        print(self.vector)
        return None

    def __mul__(self, object) -> None:
        ''' Multiplication'''
        self.vector = [elmt * object for elmt in self.vector]
        print(self.vector)
        return None

    def __sub__(self, object) -> None:
        ''' Substraction'''
        self.vector = [elmt - object for elmt in self.vector]
        print(self.vector)
        return None

    def __truediv__(self, object) -> None:
        ''' Division'''
        if object == 0:
            raise ZeroDivisionError("Cannot divide by 0")
        self.vector = [elmt / object for elmt in self.vector]
        print(self.vector)
        return None
