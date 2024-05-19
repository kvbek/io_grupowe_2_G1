import csv

def wybierz_sowe_zwroc_koszt(odleglosc, typ, specjalna):
   
    return {"PLN": 15.0}

def waluta_dict_na_str(koszt_dict):
 
    return f"{koszt_dict['PLN']} PLN"

def nadaj_sowe(adresat, tresc_wiadomosci, potwierdzenie_odbioru, odleglosc, typ, specjalna):

    koszt_dict = wybierz_sowe_zwroc_koszt(odleglosc, typ, specjalna)
    koszt_str = waluta_dict_na_str(koszt_dict)
    
    potwierdzenie_str = "TAK" if potwierdzenie_odbioru else "NIE"
    
    row = [adresat, tresc_wiadomosci, koszt_str, potwierdzenie_str]
    
    with open('poczta_nadania_lista.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)

nadaj_sowe(
    adresat="Luna Lovegood",
    tresc_wiadomosci="Wiadomość testowa",
    potwierdzenie_odbioru=True,
    odleglosc="lokalna",
    typ="list",
    specjalna="nie dotyczy"
)
