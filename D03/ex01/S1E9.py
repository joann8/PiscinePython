from abc import ABC, abstractmethod


class Character(ABC):
    """Class Abstraite Character."""
    # Une classe abstraite est une classe qui ne peut pas être
    # instanciée directement = modele pour d'autres classes
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Default Constructor Class Character"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Method die: Set Alive bool to False"""
        self.is_alive = False


class Stark(Character):
    """Class Stark inhereting from class Character."""
    def __init__(self, first_name, is_alive=True):
        """Default Constructor Class Stark"""
        super().__init__(first_name, is_alive)
