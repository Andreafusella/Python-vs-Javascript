from flask import Flask,render_template, url_for, flash, request, redirect, sessions
import random
import time

app  = Flask(__name__ , static_folder='templates')
    

@app.route("/")
def second_page():
    return render_template('second_page.html')

@app.route("/second_page_1000")
def second_page_1000():
    lista0_1000 = []
    tempo_inizio = time.perf_counter()
    for i in range(1000):
        k = random.randrange(0,1001)
        lista0_1000.append(k)
    tempo_fine = time.perf_counter()
    tempo_totale = tempo_fine - tempo_inizio
    flag = 1000
    print (f'{tempo_totale:.4f}')
    return render_template('second_page.html', tempo_totale = tempo_totale, flag = flag)

@app.route("/second_page_100000")
def second_page_100000():
    lista0_100000 = []
    tempo_inizio = time.perf_counter()
    for i in range(100000):
        k = random.randrange(0,1001)
        lista0_100000.append(k)
    tempo_fine = time.perf_counter()
    tempo_totale = tempo_fine - tempo_inizio
    flag = 100000
    print (f'{tempo_totale:.4f}')
    return render_template('second_page.html', tempo_totale = tempo_totale, flag = flag)


@app.route("/second_page_mil")
def second_page_mil():
    lista0_mil = []
    tempo_inizio = time.perf_counter()
    for i in range(1000000):
        k = random.randrange(0,1001)
        lista0_mil.append(k)
    tempo_fine = time.perf_counter()
    tempo_totale = tempo_fine - tempo_inizio
    flag = 1000000
    print (f'{tempo_totale:.4f}')
    return render_template('second_page.html', tempo_totale = tempo_totale, flag = flag)