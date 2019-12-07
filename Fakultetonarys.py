"""
Programa parasyta Evelinos Monastyrskos
"""
class Fakultetonarys:
    """Klase priskirianti kiekvienam fakulteto nariui varda ir pavarde"""
    def __init__(self, vardas, pavarde):
        """Konstruktorius"""
        self.__vardas = vardas
        self.__pavarde = pavarde
    def gauti_varda(self):
        """Suteikia fakulteto nariui varda"""
        return self.__vardas
    def gauti_pavarde(self):
        """Suteikia fakluteto nariui pavarde"""
        return self.__pavarde
