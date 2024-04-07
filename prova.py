import random
import time
lista0_1000 = []


def posizionamento_mille():
    tempo_inizio = time.perf_counter()
    for i in range(1000000):
        k = random.randrange(0,1001)
        lista0_1000.append(k)
    tempo_fine = time.perf_counter()
    tempo_totale = tempo_fine - tempo_inizio
    print (f'{tempo_totale:.4f}')
    return 

k = posizionamento_mille()