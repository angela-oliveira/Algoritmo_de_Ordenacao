def bubble_sort(lista):
    clone = lista[:]
    elementos = len(clone)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if clone[i] > clone[i+1]:
              clone[i], clone[i+1] = clone[i+1],clone[i]
              ordenado = False        
    return clone

def selectionSort(lista):
    clone = lista[:]
    for i in range(len(clone)):
        mini = min(clone[i:])
        min_index = clone[i:].index(mini) 
        clone[i + min_index] = clone[i] 
        clone[i] = mini
    return clone  

def insertionSort(lista):
    clone = lista[:]
    i=1
    while i < len(clone):
      temp = clone[i]
      troca = False
      j = i - 1
      while j>=0 and clone[j] > temp:
        clone[j+1] = clone[j]
        troca = True
        j -= 1
      if troca:
        clone[j+1] = temp
      i += 1 
    
    return clone

def shellSort(lista):
    clone = lista[:]
    temp = len(clone) // 2
    while temp > 0:
        for i in range(temp, len(clone)):
            val = clone[i]
            j = i
            while j >= temp and clone[j - temp] > val:
                clone[j] = clone[j - temp]
                j -= temp
            clone[j] = val
        temp //= 2
      
      
    return clone



from random import randint
import time


lista = []
for i in range(1,200):
  lista.append(randint(1,5000))


print("Lista desordenada !!!")
print(lista)
print('\n')

print("Lista ordenada pelo BubbleSort !!!")
antes = time.time()
print(bubble_sort(lista[:]))
depois = time.time()
total = (depois-antes)*1000
print("O tempo de ordenação do BubbleSort é igual a: %0.2f ms" % total)

print('\n')

print("Lista ordenada pelo SelectionSort !!!")
antes = time.time()
print(selectionSort(lista[:]))
depois = time.time()
total = (depois-antes)*1000
print("O tempo de ordenação do SelectionSort é igual a: %0.2f ms" % total)

print('\n')

print("Lista ordenada pelo InsertionSort !!!")
antes = time.time()
print(insertionSort(lista[:]))
depois = time.time()
total = (depois-antes)*1000
print("O tempo de ordenação do InsertionSort é igual a: %0.2f ms" % total)

print('\n')

print("Lista ordenada pelo ShellSort !!!")
antes = time.time()
print(shellSort(lista[:]))
depois = time.time()
total = (depois-antes)*1000
print("O tempo de ordenação do shellSort é igual a: %0.2f ms" % total)



