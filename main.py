from random
from time import sleep
import pandas as pd
from collections import Counter
import csv
import datetime

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


#Zadanie4

def wybierz_sowe_zwroc_koszt(confirmation, dist, type_pack, spec):
    
    cost = {"galeon": 0, "sykl": 0, "knut": 0}
    sowa = [confirmation, dist, type_pack, spec]

    if sowa[0] == True:
        cost["knut"] += 7
    
    match sowa[1]:
        case "lokalna":
            if type_pack == "list":
                cost["knut"] += 2
            elif type_pack == "paczka":
                cost["knut"] += 7
        case "krajowa":
            if type_pack == "list":
                cost["knut"] += 12
            elif type_pack == "paczka":
                cost["knut"] += 2
                cost["sykl"] += 1
        case "dalekobiezna":
            if type_pack == "list":
                cost["knut"] += 12
            elif type_pack == "paczka":
                cost["knut"] += 2
                cost["sykl"] += 1

    match sowa[3]:
        case "wyjec":
            cost["knut"] += 4
        case "list gonczy":
            cost["sykl"] += 1
    
    return cost


confirmation = True
dist = "lokalna"
type_pack = "list"
spec = None

print(wybierz_sowe_zwroc_koszt(confirmation, dist, type_pack, spec))

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


#zadanie8
def owl_sending(receiver, message):
    print(f'Sowa wyslana do: {adresat}')
    return random.random() < 0.9    # Symulacja: 90% szans na to, że sowa doleci

def owls_report(file_path):
    today = datetime.datetime.now()
    output_file = f"output_sowy_z_poczty_{today.day}_{today.month}_{today.year}.csv"

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        content = csv.DictReader(csvfile)
        owls = list(content)

    results_output = []
    for owl in owls:
        receiver = owl['receiver']
        message = owl['treść wiadomości']
        price = float(owl['koszt przesyłki'])
        deliv_conf = bool(owl['potwierdzenie odbioru'])

        owl_delivered = owl_sending(receiver, message)

        if owl_delivered:
            real_price = price
        else:
            if deliv_conf == 'TAK':
                real_price = 0.0
            else:
                real_price = price

        results_output.append({
            'receiver': receiver,
            'treść wiadomości': message,
            'koszt przesyłki': price,
            'potwierdzenie odbioru': deliv_conf,
            'rzeczywisty koszt': real_price
        })

    with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['receiver', 'treść wiadomości', 'koszt przesyłki', 'potwierdzenie odbioru', 'rzeczywisty koszt']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for result in results_output:
            writer.writerow(result)



# Przykład użycia funkcji
file_path = 'input_sowy.csv'
owls_report(file_path)
#