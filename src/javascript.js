function posizionamento(n, lista) {
    let somma = 0;
    for (let i = 0; i < n; i++) {
        let k = Math.floor(Math.random() * 1001);
        let tempoInizio = performance.now();
        lista.push(k);
        let tempoFine = performance.now();
        let tempoTotale = tempoFine - tempoInizio;
        somma += tempoTotale;
    }
    console.log((somma / 1000).toFixed(4));
}

let lista0_1000 = [];
let lista0_100000 = [];
let lista0_mil = [];

posizionamento(1000, lista0_1000);
posizionamento(100000, lista0_100000);
posizionamento(10000000, lista0_mil);
