
def minIndex(tab):
    
    min_index = 0
    for i in range(1, len(tab)):
        if tab[i] < tab[min_index]:
            min_index = i
    
    return min_index

def selectionSort(tab):

    for i in range(len(tab)-1):
       
        min_index = minIndex(tab[i:])
        tab.insert(i, tab[min_index + i])
        del tab[min_index + i + 1]

t1 = [2, 5, 0, 8, -3, 2, 5, 3, 3, 10, -20]
t2 = []
t3 = [3]
t4 = [2, 1]
t5 = [1,2]
t6 = [0, 0, 0, 1, 1, 1, -2]

selectionSort(t1)
selectionSort(t2)
selectionSort(t3)
selectionSort(t4)
selectionSort(t5)
selectionSort(t6)

print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(t6)