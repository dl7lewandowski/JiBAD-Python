
def insertSort(tab):

    for i in range(1, len(tab)):

        for j in range(i-1, -2, -1):
            
            if j == -1 or tab[j] <= tab[i]:
                if j+1 != i:
                    tab.insert(j+1, tab[i])
                    del tab[i+1]
                    break   # ten break jest niepotrzebny, bo i tak się wykona następny
                break   # czy nie lepiej użyć while'a?

t1 = [2, 5, 0, 8, -3, 2, 5, 3, 3, 10, -20]
t2 = []
t3 = [3]
t4 = [2, 1]
t5 = [1,2]
t6 = [0, 0, 0, 1, 1, 1, -2]

insertSort(t1)
insertSort(t2)
insertSort(t3)
insertSort(t4)
insertSort(t5)
insertSort(t6)

print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(t6)
