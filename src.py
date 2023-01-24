import csv
from coinmetrics.api_client import CoinMetricsClient
import pandas
import matplotlib.pyplot as plt
import math

def graph(data):
    precio = []
    for row in data:
        precio = precio + [ row[1] ]
    plt.plot( precio )
    plt.ylabel('some numbers')
    plt.yscale("log")
    plt.show()

def imprimir_csv():
    datos = []
    with open('Base_de_datos.csv', newline='', encoding = "utf-16") as f:
        reader = csv.reader(f, delimiter='	', quotechar='|')
        i = 0
        for row in reader:
            #print("Numero de linea: ", i, row[0], row[1], row[2])
            datos = datos + [( row[0] , float(row[1]), float(row[2]) )]
            i += 1
        graph(datos)

def imprimir_api():
    client = CoinMetricsClient()
    metrics = client.get_asset_metrics(assets= 'btc', 
                                        metrics = [
                                            'PriceUSD',
                                            'CapRealUSD',
                                            #'AdrActCnt',
                                            #'CapMrktCurUSD',
                                            #'CapMVRVCur',
                                            #'NVTAdj',
                                            #'VelCur1yr',
                                            #'TxCnt',
                                            #'TxTfrValAdjUSD',
                                            #'SplyCur',
                                            #'HashRate'
                                        ],
                                        start_time = '2022-01-10',
                                        end_time = '2023-01-22',
                                        frequency = '1d')

    metrics_P = pandas.DataFrame(metrics)
    print(metrics_P['time'][0])

imprimir_csv()
#imprimir_api()