"""
Programa parasyta Evelinos Monastyrskos
"""
from Fakultetonarys import Fakultetonarys

class Destytojas(Fakultetonarys):
    """Klase priskiria detytojui pareigas ir kada pradejo dirbti universitete"""
    def __init__(self, vardas, pavarde, pareiga, kada_pradejo, kiek_valandu_desto):
        """Konstruktorius"""
        super().__init__(vardas, pavarde)
        self.pareiga = pareiga
        self.kada_pradejo = kada_pradejo
        self.kiek_valandu_desto = kiek_valandu_desto
