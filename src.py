import csv
from coinmetrics.api_client import CoinMetricsClient
import pandas

def fix_nulls(s):
    for line in s:
        yield line.replace('\0', ' ')
def imprimir_csv():

#with open('Base_de_datos.csv', newline='') as f:
    
    with fix_nulls( open('Base_de_datos.csv', newline='') ) as f:
        reader = csv.reader(f, delimiter='	', quotechar='|')
        i = 0
        for row in reader:
            print("Numero de linea: ", i, row[0], row[1], row[2])
            i += 1

def imprimir_api():
    client = CoinMetricsClient()
    metrics = client.get_asset_metrics(assets= 'btc', 
                                        metrics = [
                                            'PriceUSD',
                                            'AdrActCnt',
                                            'CapMrktCurUSD',
                                            'CapMVRVCur',
                                            'NVTAdj',
                                            'VelCur1yr',
                                            'TxCnt',
                                            'TxTfrValAdjUSD'
                                            'SplyCur',
                                            'HashRate'
                                        ],
                                        start_time = '2018-01-01',
                                        end_time = '2022-01-01',
                                        frequency = '1d')
    print(client)
    print(metrics)

#imprimir_csv()
imprimir_api()