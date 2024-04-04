import random
import time
lista0_100000 = []
lista0_1000 = []
lista0_mil = []


def posizionamneto(n):
    somma = 0
    for i in range(n):
        k = random.randrange(0,1001)
        if n == 1000:
            tempo_inizio = time.perf_counter()
            lista0_1000.append(k)
            tempo_fine = time.perf_counter()
            tempo_totale = tempo_fine - tempo_inizio
            somma += tempo_totale
        elif n == 100000:
            tempo_inizio = time.perf_counter()
            lista0_100000.append(k)
            tempo_fine = time.perf_counter()
            tempo_totale = tempo_fine - tempo_inizio
            somma += tempo_totale
        elif n == 10000000:
            tempo_inizio = time.perf_counter()
            lista0_mil.append(k)
            tempo_fine = time.perf_counter()
            tempo_totale = tempo_fine - tempo_inizio
            somma += tempo_totale
    print(f'{somma * 10:.3f}')
    

posizionamneto(1000)
posizionamneto(100000)
posizionamneto(10000000)










