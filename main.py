from random import randint
from time import sleep
import pandas as pd
from collections import Counter

# Zadanie 2
def wyslij_sowe(adresat, tresc_listu):
    print(f'''
        Wysyłam sowę do: {adresat}\n
        Treść: "{tresc_listu}"
        ''')
    sleep(1)
    return [True if randint(1,10) in range(1,10) else False]

#Zadanie 3
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

# Zadanie 5
def waluta_dict_na_str(wielkosc_funduszu):
    result = ""
    try:
        for key, value in wielkosc_funduszu.items():
            if int(value) > 1:
                result += f"{value} {key}ów "
            elif value != 0:
                result += f"{value} {key} "
        print(result.strip())
    except ValueError:
        print("Podano niepoprawne wartości!")

#Zadanie 6
text =input("Podaj ilość i nazwę waluty: ")
klucze = ["galeon", "sykl", "knut"]
slownik = dict.fromkeys(klucze, 0)
print(slownik)
def waluta_str_na_dict(wejscie):
    string  =  wejscie.split()
    wartosci = []
    for index, wartosc in enumerate(string):
        if wartosc.startswith("g"):
            slownik["galeon"] = string[index-1]
        elif wartosc.startswith("s"):
            slownik["sykl"] = string[index-1]
        elif wartosc.startswith("k"):
            slownik["knut"] = string[index-1]
        else:
            wartosci.append(wartosc)
    print(slownik)    


waluta_str_na_dict(text)


