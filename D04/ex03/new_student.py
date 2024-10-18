import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate random ID"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


# @dataclass est utilisé pour simplifier la création de classes en Python
# principalement dans les cas où la classe est principalement utilisée pour
# stocker des données. Il permet de générer automatiquement certaines méthodes
# comme __init__(), __repr__(), __eq__(), et d'autres, en fonction des
# attributs définis dans la classe.
@dataclass
class Student:
    """Class Student"""
    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __init__(self, name, surname, active=True, **kwargs):

        try:
            if 'id' in kwargs:
                raise TypeError("Student.__init__() got an unexpected keyword\
                                argument 'id'")
            if 'login' in kwargs:
                raise TypeError("Student.__init__() got an unexpected keyword\
                                argument 'login'")
            self.name = name
            self.surname = surname
            self.active = active
            self.id = generate_id()
            self.login = (self.name[0] + self.surname).lower()

        except Exception as e:
            print(type(e).__name__ + ":", e)
            exit(1)
