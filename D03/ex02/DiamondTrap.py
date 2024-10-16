from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, first_name, is_alive=True):
        """Default Constructor Class King"""
        super().__init__(first_name, is_alive)

    def set_eyes(self, color: str):
        """Set a new eye color"""
        self.eyes = color

    def set_hairs(self, color: str):
        """Set a new hair color"""
        self.hairs = color

    def get_eyes(self):
        """Return current eye color"""
        return self.eyes

    def get_hairs(self):
        """Return current hair color"""
        return self.hairs
