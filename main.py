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