
// Objeto para armazenar as avaliações de cada categoria
let avaliacoes = {
    'Dificuldade': '',
    'Monitoria': '',
    'Didatica': ''
};

// Função para verificar se todas as avaliações foram feitas
function VerificaAvaliacoes(avaliacoes) {
    for (let categoria in avaliacoes) {
        if (avaliacoes[categoria] === '') {
            return false; // Retorna falso se alguma categoria não foi avaliada
        }
    }
    return true; // Retorna verdadeiro se todas as categorias foram avaliadas
}


// Seleciona todas as etiquetas de estrelas
let starLabels = document.querySelectorAll('.rating_modal label');



// Adiciona um ouvinte de evento de clique a cada etiqueta de estrela
starLabels.forEach(function (label) {
    label.addEventListener('click', function () {
        let value = this.previousElementSibling.value;
        let categoriaId = this.parentElement.id;

        console.log(categoriaId + ': ' + value + ' estrelas de 5');

        ShowValue = document.getElementById('notas_' + categoriaId)
        ShowValue.innerText = (value + ' de 5')

        // Atualiza o valor da avaliação para a categoria correspondente
        avaliacoes[categoriaId] = value;

        // Verifica se todas as categorias foram avaliadas
        if (VerificaAvaliacoes(avaliacoes)) {
            console_print(avaliacoes, categoriaId);
        }
    });
});

function console_print(avaliacoes, categoriaId) {
    
    var button_finalizar = document.getElementById('prox_button_4');  
    button_finalizar.addEventListener('click', () => {
        lista =[]


        for (let categoria in avaliacoes) {

            lista.push(avaliacoes[categoria]) 
        }

        lista.push(true) // GAMBIARRA DE DEBUG TIRAR DEPOIS

        enviar_para_back(lista);
    });
}

function enviar_para_back(lista){
    lista = lista.join(',')
     $.ajax({
            type: "POST",
            url: "../../../avaliacao/",
            data: {
                csrfmiddlewaretoken: csrf_token,
                avaliacao: lista,
                professor: nome,
                materia: codigo,
            }, 
            success: function (response)  {
                lista = response.split(",")
                console.log(lista)
                // dificuldade
                dificuldade_elemento = document.getElementById("dificuldade_texto")
                dificuldade_elemento.innerText = `Dificuldade : ${(Number(lista[0])/2).toPrecision(1)}`
                
                // apoio ao aluno
                apoio_elemento = document.getElementById("apoio_texto")
                apoio_elemento.innerText = `Apoio ao aluno : ${(Number(lista[1])/2).toPrecision(1)}`

                //didatica
                didatica_elemento = document.getElementById("didatica_texto")
                didatica_elemento.innerText = `Didatica : ${(Number(lista[2])/2).toPrecision(1)}`


            }
     })
}

