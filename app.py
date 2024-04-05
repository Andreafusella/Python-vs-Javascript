from flask import Flask,render_template, url_for, flash, request, redirect, sessions
import random
import time

app  = Flask(__name__ , static_folder='templates')


@app.route("/")
def initial_page():
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

@app.route("/second_page")
def second_page():
    return render_template('second_page.html')

@app.route("/second_page_1000")
def second_page_1000():
    lista = []
    tempo_totale = 0
    tempo_inizio = time.perf_counter()
    for i in range(1000):
        k = random.randrange(0,1001)
        lista.append(k)
    tempo_fine = time.perf_counter()
    tempo_totale = tempo_fine - tempo_inizio
    flag = 1000
    print(tempo_totale)
    return render_template('second_page.html', tempo_totale = tempo_totale, flag = flag)

@app.route("/second_page_100000")
def second_page_100000():
    lista = []
    tempo_totale = 0
    tempo_inizio = time.perf_counter()
    for i in range(100000):
        k = random.randrange(0,1001)
        lista.append(k)
    tempo_fine = time.perf_counter()
    tempo_totale = tempo_fine - tempo_inizio
    tempo_totale = f'{tempo_totale * 10:.3f}'
    flag = 100000
    return render_template('second_page.html', tempo_totale = tempo_totale, flag = flag)


@app.route("/second_page_mil")
def second_page_mil():
    lista = []
    tempo_totale = 0
    tempo_inizio = time.perf_counter()
    for i in range(1000000):
        k = random.randrange(0,1001)
        lista.append(k)
    tempo_fine = time.perf_counter()
    flag = 1000000
    tempo_totale = tempo_fine - tempo_inizio
    return render_template('second_page.html', tempo_totale = tempo_totale, flag = flag)