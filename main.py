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
# W pliku main.py zaprogramuj funkcję waluta_dict_na_str, 
# która przyjmie słownik informujący o wielkości funduszu 
# po jego przeliczeniu na monety o największym nominale i przepisze na cenę.

# jeśli wartość jakiegoś bilonu jest zerowa, pomiń ją,
# wersja łatwiejsza: nie musisz odmieniać słów knutów, 
# knuty, sykle, sykli, galeony itd. możesz zostać przy knut, sykl, galeon.

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