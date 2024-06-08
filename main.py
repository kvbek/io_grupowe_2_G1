import random
from time import sleep
import pandas as pd
from collections import Counter
import csv
import datetime

# Zadanie 2
def wyslij_sowe(adresat, tresc_wiadomosci):
    print(f'''
        Wysyłam sowę do: {adresat}\n
        Treść: "{tresc_wiadomosci}"
        ''')
    sleep(1)
    return [True if randint(1,10) in range(1,10) else False]

# Zadanie 3

def licz_sume():
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

    def licz_sume_calc(dict):
        galeon_out = sum(slownik.get("galeon")) 
        sykl_out = sum(slownik.get("sykl"))/17 
        knut_out = sum(slownik.get("knut"))/357 
        slownik_out = {"galeon": galeon_out,
                        "sykl": sykl_out,
                        "knut": knut_out}

        print(slownik_out)


    licz_sume_calc(slownik)


# Zadanie 4

def wybierz_sowe_zwroc_koszt(potwierdzenie_odbioru, odleglosc, typ, specjalna):
    
    wielkosc_funduszu = {"galeon": 0, "sykl": 0, "knut": 0}
    sowa = [potwierdzenie_odbioru, odleglosc, typ, specjalna]

    if sowa[0] == True:
        wielkosc_funduszu["knut"] += 7
    
    match sowa[1]:
        case "lokalna":
            if typ == "list":
                wielkosc_funduszu["knut"] += 2
            elif typ == "paczka":
                wielkosc_funduszu["knut"] += 7
        case "krajowa":
            if typ == "list":
                wielkosc_funduszu["knut"] += 12
            elif typ == "paczka":
                wielkosc_funduszu["knut"] += 2
                wielkosc_funduszu["sykl"] += 1
        case "dalekobiezna":
            if typ == "list":
                wielkosc_funduszu["knut"] += 12
            elif typ == "paczka":
                wielkosc_funduszu["knut"] += 2
                wielkosc_funduszu["sykl"] += 1

    match sowa[3]:
        case "wyjec":
            wielkosc_funduszu["knut"] += 4
        case "list gonczy":
            wielkosc_funduszu["sykl"] += 1
    
    return wielkosc_funduszu

'''
TEST INPUT ZAD 4
potwierdzenie_odbioru = True
odleglosc = "lokalna"
typ = "list"
specjalna = None


print(wybierz_sowe_zwroc_koszt(potwierdzenie_odbioru, odleglosc, typ, specjalna))
'''

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

# Zadanie 6
def waluta_str_na_dict():
    text =input("Podaj ilość i nazwę waluty: ")
    klucze = ["galeon", "sykl", "knut"]
    wielkosc_funduszu = dict.fromkeys(klucze, 0)
    print(wielkosc_funduszu)
    def waluta_str_na_dict_calc(wejscie):
        string  =  wejscie.split()
        wartosci = []
        for index, wartosc in enumerate(string):
            if wartosc.startswith("g"):
                wielkosc_funduszu["galeon"] = string[index-1]
            elif wartosc.startswith("s"):
                wielkosc_funduszu["sykl"] = string[index-1]
            elif wartosc.startswith("k"):
                wielkosc_funduszu["knut"] = string[index-1]
            else:
                wartosci.append(wartosc)
        print(wielkosc_funduszu)    

'''
waluta_str_na_dict(text)
'''
# Zadanie 7

'''
TEST DEFs

def wybierz_sowe_zwroc_koszt(odleglosc, typ, specjalna):
   
    return {"PLN": 15.0}

def waluta_dict_na_str(koszt_dict):
 
    return f"{koszt_dict['PLN']} PLN"
'''

def nadaj_sowe(adresat, tresc_wiadomosci, potwierdzenie_odbioru, odleglosc, typ, specjalna):
    try:   
        wielkosc_funduszu = wybierz_sowe_zwroc_koszt(odleglosc, typ, specjalna)
        koszt_str = waluta_dict_na_str(wielkosc_funduszu)
        
        potwierdzenie_str = "TAK" if potwierdzenie_odbioru else "NIE"
        
        row = [adresat, tresc_wiadomosci, koszt_str, potwierdzenie_str]
        
        with open('poczta_nadania_lista.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)
        return True
    except:
        return False

'''
nadaj_sowe(
    adresat="Luna Lovegood",
    tresc_wiadomosci="Wiadomość testowa",
    potwierdzenie_odbioru=True,
    odleglosc="lokalna",
    typ="list",
    specjalna="nie dotyczy"
)
'''

# Zadanie 8

'''
def wyslij_sowe(adresat, tresc_wiadomosci):
    print(f'Sowa wyslana do: {adresat}')
    return random.random() < 0.9    # Symulacja: 90% szans na to, że sowa doleci

'''

def poczta_wyslij_sowy(file_path):
    today = datetime.datetime.now()
    output_file = f"output_sowy_z_poczty_{today.day}_{today.month}_{today.year}.csv"

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        content = csv.DictReader(csvfile)
        owls = list(content)

    results_output = []
    for owl in owls:
        adresat = owl['adresat']
        tresc_wiadomosci = owl['treść wiadomości']
        wielkosc_funduszu = float(owl['koszt przesyłki'])
        potwierdzenie_odbioru = bool(owl['potwierdzenie odbioru'])

        owl_delivered = wyslij_sowe(adresat, tresc_wiadomosci)

        if owl_delivered == True:
            real_price = wielkosc_funduszu
        else:
            if potwierdzenie_odbioru == True:
                real_price = 0.0
            else:
                real_price = wielkosc_funduszu

        results_output.append({
            'adresat': adresat,
            'treść wiadomości': tresc_wiadomosci,
            'koszt przesyłki': wielkosc_funduszu,
            'potwierdzenie odbioru': potwierdzenie_odbioru,
            'rzeczywisty koszt': real_price
        })

    with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['adresat', 'treść wiadomości', 'koszt przesyłki', 'potwierdzenie odbioru', 'rzeczywisty koszt']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for result in results_output:
            writer.writerow(result)


'''
# Przykład użycia funkcji
file_path = 'input_sowy.csv'
poczta_wyslij_sowy(file_path)
'''