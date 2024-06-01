

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