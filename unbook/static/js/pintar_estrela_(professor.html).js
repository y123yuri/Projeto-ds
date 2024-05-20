window.onload = function () {
    console.log(nota_apoio)
    console.log(nota_didatica)
    console.log(nota_dificuldade)
    pintar_estrela_tela(nota_didatica, "didatica")
    pintar_estrela_tela(nota_apoio, "apoio")
    pintar_estrela_tela(nota_dificuldade, "dificuldade")
}

function pintar_estrela_tela(nota, categoria){
    cont_nota =0.5
    while (cont_nota<=nota){
        id = `estrela_${cont_nota}_${categoria}`
        console.log(id)
        estrela = document.getElementById(id)
        estrela.style.color = '#ffd000'
        cont_nota +=0.5
        console.log(cont_nota +",  "+ nota)
    }
}