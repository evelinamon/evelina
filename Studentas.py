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
    def gauti_kolegas(self, fakultetas):
        """Studentas is Fakulteto gauna studentu sarasa ir sugeba juos isvardinti"""
        vardai = fakultetas.gauti_studentus()
        print("Mano vardas {}, o mano kolegos yra:".format(self.gauti_varda()), end=' ')
        for vardas in vardai:
            if vardas != self.gauti_varda():
                print(vardas, end=' ')
        print("\n")
    def spausdinti(self):
        return(self.gauti_varda(), self.gauti_pavarde(), self.studiju_programa, self.kursas)