

function posizionamento_1000() {
    let dati = []
    let lista = []
    let tempoInizio = performance.now();
    for (let i = 0; i < 1000; i++) {
        let k = Math.floor(Math.random() * 1001);
        lista.push(k);
    }
    let tempoFine = performance.now();
    let tempoTotale = ((tempoFine - tempoInizio)/1000).toFixed(5);
    dati.push(tempoTotale)

    // const len = lista.length;
    // let tempoiniziobubble = performance.now();
	// for (let i = 0; i < len - 1; i++) {
	// 	for (let j = 0; j < len - 1 - i; j++) {
	// 		if (lista[j] > lista[j + 1]) {
	// 			[lista[j], lista[j + 1]] = [lista[j + 1], lista[j]];
	// 		}
	// 	}
	// }
    // let tempofinebubble = performance.now();
    // let tempototaleBubble = ((tempofinebubble - tempoiniziobubble)/1000).toFixed(5);
    // dati.push(tempototaleBubble)
	return(dati);
}

function posizionamento_100000() {
    let dati = []
    let lista = []
    let tempoInizio = performance.now();
    for (let i = 0; i < 100000; i++) {
        let k = Math.floor(Math.random() * 1001);
        lista.push(k);
    }
    let tempoFine = performance.now();
    let tempoTotale = ((tempoFine - tempoInizio)/1000).toFixed(5);
    dati.push(tempoTotale)

    // const len = lista.length;
    // let tempoiniziobubble = performance.now();
	// for (let i = 0; i < len - 1; i++) {
	// 	for (let j = 0; j < len - 1 - i; j++) {
	// 		if (lista[j] > lista[j + 1]) {
	// 			[lista[j], lista[j + 1]] = [lista[j + 1], lista[j]];
	// 		}
	// 	}
	// }
    // let tempofinebubble = performance.now();
    // let tempototaleBubble = tempofinebubble - tempoiniziobubble
    // dati.push(tempototaleBubble)
	return(dati);
}
function posizionamento_milione() {
    let dati = []
    let lista = []
    let tempoInizio = performance.now();
    for (let i = 0; i < 1000000; i++) {
        let k = Math.floor(Math.random() * 1001);
        lista.push(k);
    }
    let tempoFine = performance.now();
    let tempoTotale = ((tempoFine - tempoInizio)/1000).toFixed(5);
    dati.push(tempoTotale)

    // const len = lista.length;
    // let tempoiniziobubble = performance.now();
	// for (let i = 0; i < len - 1; i++) {
	// 	for (let j = 0; j < len - 1 - i; j++) {
	// 		if (lista[j] > lista[j + 1]) {
	// 			[lista[j], lista[j + 1]] = [lista[j + 1], lista[j]];
	// 		}
	// 	}
	// }
    // let tempofinebubble = performance.now();
    // let tempototaleBubble = tempofinebubble - tempoiniziobubble
    // dati.push(tempototaleBubble)
	return(dati);
}


var dati_1000 = posizionamento_1000()
let tempo_1000 = dati_1000[0]
let tempo_1000_bubble = dati_1000[1]
console.log(tempo_1000);

var dati_100000 = posizionamento_100000()
let tempo_100000 = dati_100000[0]
let tempo_100000_bubble = dati_100000[1]
console.log(tempo_100000);

var dati_milione = posizionamento_milione()
let tempo_milione = dati_milione[0]
let tempo_milione_bubble = dati_milione[1]
console.log(tempo_milione);








