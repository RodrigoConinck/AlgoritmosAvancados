from array import array
from statistics import median
import pandas as pd

listaFem = pd.read_csv('./ibge-fem-10000.csv', delimiter=',')
listaMas = pd.read_csv('./ibge-mas-10000.csv', delimiter=',')

frames = [listaFem,listaMas]

listas = pd.concat(frames)

lista = listas.sort_values("nome").loc[:,"nome"].values.tolist()

def buscaBinaria(lista, nome):
    lenght = len(lista)
    left = 0
    right = lenght - 1

    while(left <= right):
        middle = int ((left + right)/2)
        if lista[middle] == nome:
            print (middle)
            break
        if nome < lista[middle]:
            right = middle -1
        if nome > lista[middle]:
            left = middle + 1
    else:
        print("Nome não encontrado")

nome=input("insira um nome: ")
buscaBinaria(lista, nome)