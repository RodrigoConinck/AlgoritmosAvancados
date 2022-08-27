import pandas as pd

listaMusicas = pd.read_csv('./TikTok_songs_2019.csv', delimiter=',')

lista = listaMusicas.sort_values("track_name").loc[:,"track_name"].values.tolist()

def heapify(lista, n, i): 
    largest = i  # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and lista[i] < lista[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and lista[largest] < lista[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        lista[i],lista[largest] = lista[largest],lista[i]  # swap 
  
        # Heapify the root. 
        heapify(lista, n, largest) 
  
# The main function to sort an array of given size 
def heapSort(lista): 
    n = len(lista) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(lista, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        lista[i], lista[0] = lista[0], lista[i]   # swap 
        heapify(lista, i, 0) 
  
# Driver code to test above 
arr = [ 12, 11, 13, 5, 6, 7] 
heapSort(lista) 
n = len(lista) 
print ("Sorted array is") 
for i in range(n): 
    print (lista[i])