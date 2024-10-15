from S1E9 import Character

class Baratheon(Character):
    """Class Baratheon inherited from Character"""
    def __init__(self, first_name, is_alive=True):
        """Default Constructor Class Stark"""
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'
    
    def __repr__(self):
        """return representing Baratheon"""
        repr = f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
        return repr

    def __str__(self):
        """return str Baratheon"""
        return self.__repr__()
    

class Lannister(Character):
    """Class Lannister inherited from Character"""
    family_name = 'Lannister'
    def __init__(self, first_name, is_alive=True):
        """Default Constructor Class Stark"""
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'
    
    def __repr__(self):
        """return representing Lannister"""
        repr = f"Vector: ('{self.family_name}', '{self.eyes}','{self.hairs}')"
        return repr
    
    def __str__(self):
        """return str Lannister"""
        return self.__repr__()

    @classmethod
    def create_lannister(cls, name, is_alive=True):
        """Create an instance"""
        return (cls(name, is_alive))


