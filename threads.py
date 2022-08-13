from array import array
from statistics import median
from time import sleep, perf_counter
from threading import Thread
import pandas as pd

listaFem = pd.read_csv('./ibge-fem-10000.csv', delimiter=',')
listaMas = pd.read_csv('./ibge-mas-10000.csv', delimiter=',')

listaM = listaMas.sort_values("nome").loc[:,"nome"].values.tolist()
listaF = listaFem.sort_values("nome").loc[:,"nome"].values.tolist()

def buscaBinaria(lista, nome):
    lenght = len(lista)
    left = 0
    right = lenght - 1

    while(left <= right):
        middle = int ((left + right)/2)
        if lista[middle] == nome:
            print(nome)
            return nome
            break
        if nome < lista[middle]:
            right = middle -1
        if nome > lista[middle]:
            left = middle + 1
        else:
            print("Nome não encontrado")

nomeM = input("Insira um nome masculino: ")
nomeF = input("Insira um nome feminino: ")

start_time = perf_counter()

t1 = Thread(target=buscaBinaria(listaM, nomeM))
t2 = Thread(target=buscaBinaria(listaF, nomeF))

t1.start()
t2.start()

t1.join()
t2.join()

end_time = perf_counter()

print(f'It took {end_time- start_time :0.2f} second(s) to complete.')
