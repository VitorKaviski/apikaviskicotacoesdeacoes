from fastapi import FastAPI
from pandas_datareader import data as web
from fastapi.encoders import jsonable_encoder


app = FastAPI()

@app.get("/")

def home():
    return {'API Online'}

@app.get('/{id_valores}')

def adquirir_valores(id_valores: str):
    x = id_valores.split(',')

    y = x[0]
    z = x[1]
    w = x[2]

    dataframe = web.DataReader(f'{y}', data_source='yahoo', start=f'{z}', end=f'{w}')
    Index_ADJ_Close = dataframe['Adj Close'].index.tolist()
    lista_Volume = dataframe['Volume'].to_list()
    Alta = dataframe['High'].to_list()
    Baixa = dataframe['Low'].to_list()
    Abertura = dataframe['Open'].to_list()
    Fechamento = dataframe['Close'].to_list()
    lista_ADJ_Close = dataframe['Adj Close'].to_list()
    x = {'Index_ADJ_Close': Index_ADJ_Close,'lista_ADJ_Close': lista_ADJ_Close,'lista_Volume': lista_Volume, 'Alta': Alta, 'Baixa': Baixa, 'Abertura':Abertura, 'Fechamento': Fechamento}
    return jsonable_encoder(x)

