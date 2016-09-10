import random
import time

def quick_sort(v):
    quick(v, 0, len(v) - 1)


def quick(v, izq, der):
    i, j = izq, der
    x = v[int((izq + der) / 2)]
    while i <= j:
        while v[i] < x and i < der:
            i += 1
        while x < v[j] and j > izq:
            j -= 1
        if i <= j:
            v[i], v[j] = v[j], v[i]
            i += 1
            j -= 1
    if izq < j:
        quick(v, izq, j)
    if i < der:
        quick(v, i, der)

n = int(input("Enter maximum number of random integers to generate (300000)") or 300000)
it = int(input("Insert number of incremental steps (50)") or 50)
while it < 1:
    it = int(input("Insert number of incremental steps (50)") or 50)
filename = input("Enter filename (sample.csv)") or "sample.csv"
if not (".csv" in filename):
    filename += ".csv"

i = int(n // it)

for x in range(it):
    c = []
    for y in range(i):
        c.append(random.randint(0,n))
    start_time = time.time()
    quick_sort(c)
    stop_time = time.time() - start_time
    print(it,",",stop_time)



