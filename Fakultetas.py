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
        #vardas = input("Iveskite varda: ")
        #pavarde = input("Ivskite pavarde: ")
        #studiju_programa = input("Iveskite studiju_programa: ")
        #kursas = input("Iveskite kursa: ")
        studentas = Studentas(vardas, pavarde, studiju_programa, kursas)
        self.studentai[studentas.gauti_varda()] = studentas
        print("Pridejau studenta. Studentu skaicius {}".format(len(self.studentai)))
    def gauti_studentus(self):
        """Fakultetas suteikia studentui prieiga prie kitu studentu saraso"""
        return self.studentai.keys()
    def spausdinti_studentus(self):
        for studentas in self.studentai.values():
            print(studentas.spausdinti())
    def istrinti_studenta(self):
        vardas = input("Iveskite varda zmogaus kuri norite pasalinti: ")
        del self.studentai[vardas]
        for studentas in self.studentai.values():
            print(studentas.spausdinti())
    def gauti_studenta(self):
        vardas = input("Iveskite ieskomo studento varda: ")
        return self.studentai[vardas]
    def priimti_destytoja(self):
        """Prideda destytoja prie fakulteto"""
        vardas = input("Iveskite varda: ")
        pavarde = input("Iveskite pavarde: ")
        pareiga = input("Iveskite pareiga: ")
        kada_pradejo = int(input("Iveskite kada pradejo dirbti: "))
        destytojas = Destytojas(vardas, pavarde, pareiga, kada_pradejo)
        self.destytojai[destytojas.gauti_varda()] = destytojas
        print("Pridejau destytoja. Destytoju skaicius {}".format(len(self.destytojai)))
        return self
    def gauti_destytojus(self):
        """Fakultetas suteikia destytojui prieiga prie kitu studentu saraso"""
        return self.destytojai.keys()
    def spausdinti_destytojus(self):
        for destytojas in self.destytojai.values():
            print(destytojas.spausdinti())
    def istrinti_destytojus(self):
        vardas = input("Iveskite varda zmogaus kuri norite pasalinti: ")
        del self.destytojai[vardas]
        for destytojas in self.destytojai.values():
            print(destytojas.spausdinti())
    def gauti_destytoja(self):
        vardas = input("Iveskite ieskomo destytojo varda: ")
        return self.destytojai[vardas]
    def ivesti_numeri(self, fakultetas):
        """Grazina norima metoda"""
        def print_menu():       # Your menu design here
            print(30 * "-", "MENU", 30 * "-")
            print("1. Prideda studenta ")
            print("2. Prideda destytoja ")
            print("3. Pasalina studenta ")
            print("4. Pasalina destytoja ")
            print("5. Spausdinti studentus")
            print("6. Spausdinti destytojus")
            print(73 * "-")
        ciklas = 1
        while ciklas == 1:
            print_menu()
            pasirinkimas = input("Iveskite skaiciu [1-6]: ")
            if pasirinkimas == '2':
                print (fakultetas.priimti_destytoja())
            elif pasirinkimas == '3':
                print (fakultetas.istrinti_studenta())
            elif pasirinkimas == '4':
                print (fakultetas.istrinti_destytojus())
            elif pasirinkimas == '5':
                print (fakultetas.spausdinti_studentus())
            elif pasirinkimas == '6':
                print (fakultetas.spausdinti_destytojus())
            else:
                ciklas = 2