import csv
from coinmetrics.api_client import CoinMetricsClient
import pandas
import matplotlib.pyplot as plt
import math

def graph(data,headers): # data: es un dataframe de pandas. Lista con todos los "column headers" a graficar. Siempre se plotea en función del tiempo.

    i = 0
    


    #print(len(data3), " AAAAA ", len(data2))

    plt.plot( data, label = "precio")
    #plt.plot(data3, data2, label = "precio/2")
    plt.legend()
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
        graph(datos,1)

def import_data_coinmetrics(asset_par, metrics_par):
    
    
    client = CoinMetricsClient()
    metrics = client.get_asset_metrics(assets= asset_par, 
                                        metrics = metrics_par,
                                        start_time = '2010-07-18',
                                        #end_time = '2022-01-10',
                                        #frequency = '1d'
                                        )

    metrics_P = pandas.DataFrame(metrics)

    


    print(metrics_P)

    def round_float(n):
        return round(float(n),2)

    for el in metrics_par: #hace que todas las métricas importadas sean números en vez de texto, y los redondea a 2 decimales
        metrics_P[el] = list(map(round_float, metrics_P[el]))

    print(metrics_P)


    #realized_price = []
    #i = 0
    #for el in metrics_P['PriceUSD']:
    #    realized_price = realized_price + [i]
    #    i += 1
  

    #metrics_2 = metrics_P.assign(PriceReal=realized_price)

    #print(metrics_P)


    #for el in metrics_P['PriceReal']:
    #    print(el)

    #graph(metrics_P['PriceUSD'])

#imprimir_csv()

import_data_coinmetrics('btc', ['PriceUSD','CapRealUSD','SplyCur'])