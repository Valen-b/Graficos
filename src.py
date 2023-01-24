import csv
from coinmetrics.api_client import CoinMetricsClient
import pandas
import matplotlib.pyplot as plt
import math

def graph(data,data2):

    data3 = []

    i = 0
    for el in data:
        data[i] = float(el)
        data3 = data3 + [i]
        i += 1


    #print(len(data3), " AAAAA ", len(data2))

    plt.plot(data3, data, label = "precio")
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

def imprimir_api():
    client = CoinMetricsClient()
    metrics = client.get_asset_metrics(assets= 'btc', 
                                        metrics = [
                                            'PriceUSD',
                                            'CapRealUSD',
                                            'SplyCur',
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
                                        start_time = '2010-07-18',
                                        #end_time = '2022-01-10',
                                        frequency = '1d')

    metrics_P = pandas.DataFrame(metrics)

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

    graph(metrics_P['PriceUSD'], metrics_P['PriceUSD'])

#imprimir_csv()
imprimir_api()