from random import randint
from time import sleep

# Zadanie 2
def wyslij_sowe(adresat, tresc_listu):
    print(f'''
        Wysyłam sowę do: {adresat}\n
        Treść: "{tresc_listu}"
        ''')
    sleep(1)
    return [True if randint(1,10) in range(1,10) else False]

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

