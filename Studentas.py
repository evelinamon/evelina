"""
Programa parasyta Evelinos Monastyrskos
"""
from Fakultetonarys import Fakultetonarys

class Studentas(Fakultetonarys):
    """Klase priskiria studentui studiju_programa ir kursa"""
    def __init__(self, vardas, pavarde, studiju_programa, kursas):
        """Konstruktorius"""
        super().__init__(vardas, pavarde)
        self.studiju_programa = studiju_programa
        self.kursas = kursas
