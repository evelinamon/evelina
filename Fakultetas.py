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

    def gauti_studentu_sarasa(self):
        """Grazina studentu sarasa"""
        return self.studentai

    def istrinti_studenta(self, vardas):
        """Istrina studenta"""
        del self.studentai[vardas]

    def priimti_destytoja(self, vardas, pavarde, pareiga, kada_pradejo, kiek_laiko_desto):
        """Prideda destytoja prie fakulteto"""
        destytojas = Destytojas(vardas, pavarde, pareiga, kada_pradejo, kiek_laiko_desto)
        self.destytojai[destytojas.gauti_varda()] = destytojas
        print("Pridejau destytoja. Destytoju skaicius {}".format(len(self.destytojai)))

    def gauti_destytoju_sarasa(self):
        """Grazina destytoju sarasa"""
        return self.destytojai

    def istrinti_destytojus(self, vardas):
        """Istrina destytojus"""
        del self.destytojai[vardas]

    def desto_valandu(self, kiek_valandu_desto):
        """Suma visu destytoju destomu valandu"""
        suma = 0
        for destytojas in self.destytojai:
            suma = suma + int(kiek_valandu_desto)