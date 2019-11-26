"""
Programa parasyta Evelinos Monastyrskos
"""
from Fakultetas import Fakultetas
from Studentas import Studentas
from Destytojas import Destytojas

MIFfakultetas = Fakultetas("MIF", "Naugarduko 24")
MIFfakultetas.priimti_studenta()
MIFfakultetas.priimti_studenta()
MIFfakultetas.priimti_destytoja()
MIFfakultetas.priimti_destytoja()
MIFfakultetas.spausdinti_studentus()
MIFfakultetas.spausdinti_destytojus()
MIFfakultetas.istrinti_studenta()
MIFfakultetas.gauti_studentus()
MIFfakultetas.gauti_studenta().gauti_kolegas(MIFfakultetas)
MIFfakultetas.istrinti_destytojus()
MIFfakultetas.gauti_destytojus()
MIFfakultetas.gauti_destytoja().gauti_kolegas(MIFfakultetas)
