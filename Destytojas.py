"""
Programa parasyta Evelinos Monastyrskos
"""
from Fakultetonarys import Fakultetonarys

class Destytojas(Fakultetonarys):
    """Klase priskiria detytojui pareigas ir kada pradejo dirbti universitete"""
    def __init__(self, vardas, pavarde, pareiga, kada_pradejo):
        """Konstruktorius"""
        super().__init__(vardas, pavarde)
        self.pareiga = pareiga
        self.kada_pradejo = kada_pradejo
    def apskaiciuoti_patirti(self):
        """Metodas apskaiciuoja kiek metu destytojo patirti"""
        metai = int(input("Iveskite kokie dabar metai: "))
        patirtis = metai - self.kada_pradejo
        return patirtis
    def gauti_kolegas(self, fakultetas):
        """Destytojas is Fakulteto gauna destytoju sarasa ir sugeba juos isvardinti"""
        vardai = fakultetas.gauti_destytojus()
        print("Mano vardas {}, o mano kolegos yra:".format(self.gauti_varda()), end=' ')
        for vardas in vardai:
            if vardas != self.gauti_varda():
                print(vardas, end=' ')
        print("\n")
    def spausdinti(self):
        """Spausdina destytojo duomenys"""
        return(self.gauti_varda(), self.gauti_pavarde(), self.pareiga, self.kada_pradejo)