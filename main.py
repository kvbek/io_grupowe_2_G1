import pandas as pd
from collections import Counter

lista_galeon = []
lista_sykl = []
lista_knut = []

for i in range(3):
    ilosc_galeon = float(input("Podaj ilość galeonów: "))
    lista_galeon.append(ilosc_galeon)
    #slownik["galeon"] = ilosc_galeon[i]
    ilosc_sykl = float(input("Podaj ilość sykli: "))
    lista_sykl.append(ilosc_sykl)
    #slownik["sykl"] = ilosc_sykl[i]
    ilosc_knut = float(input("Podaj ilość knutów: "))
    lista_knut.append(ilosc_knut)
    # lista_knut = lista_knut.add[i]
    #slownik["knut"] = ilosc_knut[i]
   
print(lista_galeon)
print(lista_sykl)
print(lista_knut)

slownik = {"galeon": lista_galeon, "sykl": lista_sykl, "knut": lista_knut }
print(slownik)

def licz_sume(dict):
    galeon_out = sum(slownik.get("galeon")) 
    sykl_out = sum(slownik.get("sykl"))/17 
    knut_out = sum(slownik.get("knut"))/357 
    slownik_out = {"galeon": galeon_out,
                    "sykl": sykl_out,
                    "knut": knut_out}
                    
    print(slownik_out)

licz_sume(slownik)

