import random
import time
lista0_100000 = []
lista0_1000 = []
lista0_mil = []

def posizionamento(scelta):
    tempo_inizio = time.perf_counter()
    if scelta == 1:
        n = 1000
    elif scelta == 2:
        n = 100000
    elif scelta == 3: 
        n = 10000000
    for i in range (n):
        k = random.randrange(0,1001)
        if n == 1000:
            lista0_1000.append(k)
        elif n == 100000:
            lista0_100000.append(k)
        elif n == 1000000:
            lista0_mil.append(k)
    tempo_fine = time.perf_counter()
    tempo_totale = tempo_fine - tempo_inizio
    print(f"{tempo_totale:.2f}")
        
scelta = int(input("Inserisci il valore: 1 | 1000 numeri, 2 | 100.000 numeri, 3 | 1.000.000 numeri, 4 | tutti"))
posizionamento(scelta)









