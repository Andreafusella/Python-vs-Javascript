from flask import Flask,render_template, url_for, flash, request, redirect, sessions

app  = Flask(__name__ , static_folder='templates')


@app.route("/")
def initial_page():
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
            elif n == 1000000:
                tempo_inizio = time.perf_counter()
                lista0_mil.append(k)
                tempo_fine = time.perf_counter()
                tempo_totale = tempo_fine - tempo_inizio
                somma += tempo_totale
        return(f'{somma * 10:.3f}')
        

    tempo_1000 = posizionamneto(1000)
    tempo_100000 = posizionamneto(100000)
    tempo_mil = posizionamneto(1000000)
    return render_template('Tempo_numeri.html', tempo_1000 = tempo_1000, tempo_100000 = tempo_100000, tempo_mil = tempo_mil)