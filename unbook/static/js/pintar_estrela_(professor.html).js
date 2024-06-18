window.onload = function () {
    console.log(nota_didatica + 'didatica')
    console.log(nota_apoio + 'apoio')
    console.log(nota_dificuldade + 'dificuldade')



    //pintar estrelas
    pintar_estrela_tela(nota_didatica, "didatica")
    pintar_estrela_tela(nota_apoio, "apoio")
    pintar_estrela_tela(nota_dificuldade, "dificuldade")
}

function pintar_estrela_tela(nota, categoria){
    cont_nota =0.5
    
    while (cont_nota<=nota){
        id = `estrela_${cont_nota}_${categoria}`
        console.log('id: ' + id + '| nota' + nota)
        estrela = document.getElementById(id)
        estrela.style.color = '#ffd000'
        cont_nota +=0.5
        console.log(cont_nota +" ,  "+ nota)
    }
}

let circular = document.getElementById('percents');
let num = document.getElementById('indice');
let indice = document.getElementById('indice_js').textContent;
indice = parseFloat(indice);
console.log(indice)

if(indice !== 0) {

let start = 0, end = indice, speed = 15;
    let progress = setInterval(() => {
        start++;
    
        num.textContent = `${start}%`;
        circular.style.transition = "all 0.3s ease";

        if (start < 25) {
            circular.style.background = `conic-gradient(#d43b5a ${start * 3.6}deg, #777D89 0deg)`;
        }
        else if (start > 25 && start < 75) {
            circular.style.background = `conic-gradient(#ffd000 ${start * 3.6}deg, #777D89 0deg)`;
        }
        else if (start > 75) {
            circular.style.background = `conic-gradient(#008940 ${start * 3.6}deg, #777D89 0deg)`;
        }
    
        if (start == indice){
            clearInterval(progress);
        }
        
    }, speed);

}