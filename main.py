import csv
import datetime
import random

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
