"""
Programa parasyta Evelinos Monastyrskos
"""
from Studentas import Studentas
from Destytojas import Destytojas

class Fakultetas:
    """Universiteto fakultetu klase, kuri pasako fakulteto pavadinima ir adresa"""
    def __init__(self, pavadinimas, adresas):
        """Konstruktorius"""
        self.__pavadinimas = pavadinimas
        self.__adresas = adresas
        self.studentai = {}
        self.destytojai = {}

    def gauti_pavadinima(self):
        """Suteikia fakultetui pavadinima"""
        return self.__pavadinimas

    def gauti_adresa(self):
        """Suteikia fakultetui adresa"""
        return self.__adresas

    def priimti_studenta(self, vardas, pavarde, studiju_programa, kursas):
        """Prideda studenta prie fakulteto"""
        studentas = Studentas(vardas, pavarde, studiju_programa, kursas)
        self.studentai[studentas.gauti_varda()] = studentas
        print("Pridejau studenta. Studentu skaicius {}".format(len(self.studentai)))

    def gauti_studentus(self):
        """Fakultetas suteikia studentui prieiga prie kitu studentu saraso"""
        return self.studentai.keys()

    def gauti_studentu_sarasa(self):
        return self.studentai

    def spausdinti_studentus(self):
        for studentas in self.studentai.values():
            print(studentas.spausdinti())

    def istrinti_studenta(self, vardas):
        del self.studentai[vardas]

    def gauti_studenta(self):
        vardas = input("Iveskite ieskomo studento varda: ")
        return self.studentai[vardas]

    def priimti_destytoja(self, vardas, pavarde, pareiga, kada_pradejo):
        """Prideda destytoja prie fakulteto"""
        destytojas = Destytojas(vardas, pavarde, pareiga, kada_pradejo)
        self.destytojai[destytojas.gauti_varda()] = destytojas
        print("Pridejau destytoja. Destytoju skaicius {}".format(len(self.destytojai)))

    def gauti_destytojus(self):
        """Fakultetas suteikia destytojui prieiga prie kitu studentu saraso"""
        return self.destytojai.keys()

    def gauti_destytoju_sarasa(self):
        return self.destytojai

    def spausdinti_destytojus(self):
        for destytojas in self.destytojai.values():
            print(destytojas.spausdinti())

    def istrinti_destytojus(self, vardas):
        del self.destytojai[vardas]

    def gauti_destytoja(self):
        vardas = input("Iveskite ieskomo destytojo varda: ")
        return self.destytojai[vardas]