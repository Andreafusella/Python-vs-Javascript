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
    return((somma / 1000).toFixed(3));
}

let lista0_1000 = [];
let lista0_100000 = [];
let lista0_mil = [];

var tempo_1000 = posizionamento(1000, lista0_1000, document.getElementById("risultati-lista-1000"));
var tempo_100000 = posizionamento(100000, lista0_100000);
var tempo_mil = posizionamento(1000000, lista0_mil);

console.log(tempo_1000);
console.log(tempo_100000);
console.log(tempo_mil);


