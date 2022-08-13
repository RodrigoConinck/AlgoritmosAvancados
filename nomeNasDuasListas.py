from array import array
from statistics import median
import pandas as pd

listaFem = pd.read_csv('./ibge-fem-10000.csv', delimiter=',')
listaMas = pd.read_csv('./ibge-mas-10000.csv', delimiter=',')

listaM = listaMas.sort_values("nome").loc[:,"nome"].values.tolist()
listaF = listaFem.sort_values("nome").loc[:,"nome"].values.tolist()

def buscaBinaria(lista , nome):
    lenght = len(lista)
    left = 0
    right = lenght - 1

    while(left <= right):
        middle = int ((left + right)/2)
        if lista[middle] == nome:
            return True
        if nome < lista[middle]:
            right = middle -1
        if nome > lista[middle]:
            left = middle + 1
        else:
            return False

nome=input("insira um nome: ")
listaM = buscaBinaria(listaM, nome)
listaF = buscaBinaria(listaF, nome)
if(listaM == False or listaF == False):
    print("O nome não está nas duas listas")
else:
    print("O nome está nas duas litas")