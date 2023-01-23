import csv
from coinmetrics.api_client import CoinMetricsClient

def imprimir_csv():

    with open('Base_de_datos.csv', newline='') as f:
        reader = csv.reader(f, delimiter='	', quotechar='|')
        i = 0
        for row in reader:
            print("Numero de linea: ", i, row[0], row[1], row[2])
            i += 1

def imprimir_api():
    client = CoinMetricsClient()

    print(client)


#imprimir_csv()
imprimir_api()
