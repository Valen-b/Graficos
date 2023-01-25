import csv
from coinmetrics.api_client import CoinMetricsClient
import pandas
import matplotlib.pyplot as plt
import math
from datetime import date, timedelta

def graph(data,headers): # data: es un dataframe de pandas. Lista con todos los "column headers" a graficar. Siempre se plotea en función del tiempo.

    xaxis =  list(range(0, len(data[headers[0]]) ))
    
    color = 1
    for header in headers:
        print("hacemos el plot con el headder " ,header)
        plt.plot(xaxis, data[header] ,color, label = header)
        color = color + 1
    
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

def import_data_coinmetrics(asset_par, metrics_par):
    
    
    client = CoinMetricsClient()
    metrics = client.get_asset_metrics(assets= asset_par, 
                                        metrics = metrics_par,
                                        start_time = '2010-07-18',
                                        end_time = date.today()- timedelta(1),
                                        #frequency = '1d'
                                        )

    metrics_P = pandas.DataFrame(metrics)


    def round_float(n):
        return round(float(n),2)


    #correción de los datos:

    for el in metrics_par: #hace que todas las métricas importadas sean números en vez de texto, y los redondea a 2 decimales
        metrics_P[el] = list(map(round_float, metrics_P[el]))

    metrics_P['time'] = pandas.to_datetime(metrics_P['time'])


    return metrics_P

def indicador_1(datos):

    return datos

    #realized_price = []
    #i = 0
    #for el in metrics_P['PriceUSD']:
    #    realized_price = realized_price + [i]
    #    i += 1
  
    #metrics_2 = metrics_P.assign(PriceReal=realized_price)

    #for el in metrics_P['PriceReal']:
    #    print(el)

    #graph(metrics_P['PriceUSD'])


datos = import_data_coinmetrics('btc', ['PriceUSD','CapRealUSD','SplyCur'])

datos_nuevo = indicador_1(datos)

print(datos_nuevo)

graph(datos, ['PriceUSD', 'CapRealUSD'] ) #