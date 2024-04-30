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
    galeon_out = sum(a["galeon"]  for a in slownik)
    sykl_out = sum(b["sykl"] for b in slownik)
    knut_out = sum(c["knut"] for c in slownik )
    slownik_out = {"galeon": galon_out,
                    "sykl": sykl_out,
                    "knut": knut_out}
    return slownik_out

licz_sume(slownik)



# dict_in = {
#     "galeon" : [1, 3, 5],
#     "sykl" : [18, 20, 10],
#     "knut" : [30, 40, 7]
# }
# dict_out= {}


# def licz_sume(dict):
# count_galon =
# count_sykl =
# coubt_knut =

#     dict_out.keys[0] = count_galon
#     dict_out.keys[1] = count_sykl
#     dict_out.keys[2] = count_knut

