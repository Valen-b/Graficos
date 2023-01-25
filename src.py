import csv
from coinmetrics.api_client import CoinMetricsClient
import pandas
import matplotlib.pyplot as plt
import math

def graph(data,headers): # data: es un dataframe de pandas. Lista con todos los "column headers" a graficar. Siempre se plotea en función del tiempo.

    xaxis =  list(range(0, len(data[headers[0]]) ))
    
    color = 1
    for header in headers:
        print("hacemos el plot con el headder " ,header)
        plt.plot(xaxis, data[header] ,color, label = header)
        color = color+1
    
    #print(len(data3), " AAAAA ", len(data2))

    
    #plt.plot(data3, data2, label = "precio/2")
    #handles, labels = plt.gca().get_legend_handles_labels()
    #by_label = dict(zip(labels, handles))
    #plt.legend(by_label.values(), by_label.keys())
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

def import_data_coinmetrics():
    client = CoinMetricsClient()
    metrics = client.get_asset_metrics(assets= 'btc', 
                                        metrics = [
                                            'PriceUSD',
                                            'CapRealUSD',
                                            'SplyCur',
                                        ],
                                        start_time = '2010-07-18',
                                        #end_time = '2022-01-10',
                                        frequency = '1d')

    metrics_P = pandas.DataFrame(metrics)


    print(metrics_P)

    def round_float(n):
        return round(float(n),2)

    metrics_P['PriceUSD'] = list(map(round_float, metrics_P['PriceUSD']))

    metrics_P['CapRealUSD'] = list(map(round_float, metrics_P['CapRealUSD']))

    print(metrics_P)

    graph(metrics_P, ['PriceUSD', 'CapRealUSD'] ) #

    #realized_price = []
    #i = 0
    #for el in metrics_P['PriceUSD']:
    #    realized_price = realized_price + [i]
    #    i += 1
  

    #print(metrics_P)

    #metrics_2 = metrics_P.assign(PriceReal=realized_price)

    #print(metrics_P)


    #for el in metrics_P['PriceReal']:
    #    print(el)

    #graph(metrics_P['PriceUSD'])

#imprimir_csv()
import_data_coinmetrics()