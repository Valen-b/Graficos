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
    
    def round_float(n):
        return round(float(n),2)
    
    client = CoinMetricsClient()
    metrics = client.get_asset_metrics(assets= asset_par, 
                                        metrics = metrics_par,
                                        start_time = '2010-07-18',
                                        end_time = date.today()- timedelta(1),
                                        #frequency = '1d'
                                        )

    #correción de los datos:

    metrics_P = pandas.DataFrame(metrics)

    for el in metrics_par: #hace que todas las métricas importadas sean números en vez de texto, y los redondea a 2 decimales
        metrics_P[el] = list(map(round_float, metrics_P[el]))

    metrics_P['time'] = pandas.to_datetime(metrics_P['time'])


    return metrics_P

def indicador_1(datos):

    datos['PriceRealUSD'] = 0.0 #crea una nueva columa en 'datos' con un Header 'PriceRealUSD' y le asgina tantas filas con el valor 0.0 como filas tenga el dataframe.

    i = 0
    for el in datos['PriceRealUSD']:
        datos['PriceRealUSD'][i] = datos['CapRealUSD'][i] / datos['SplyCur'][i]
        i += 1


datos = import_data_coinmetrics('btc', ['PriceUSD','CapRealUSD','SplyCur'])

indicador_1(datos)

print(datos)

graph(datos, ['PriceUSD', 'PriceRealUSD']) #toma el dataframe (primer parámetro) e imprime en un gráfico los valores de tantos Headers como le sea indicado en la lista (segundo parámetro).