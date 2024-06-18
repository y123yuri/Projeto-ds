// Objeto para armazenar as avaliações de cada categoria
let avaliacoes = {
    'Dificuldade': '',
    'Monitoria': '',
    'Didatica': ''
};

// Variável para armazenar o valor de 'sim' ou 'não'
let element = null;

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

        let ShowValue = document.getElementById('notas_' + categoriaId);
        ShowValue.innerText = (value + ' de 5');

        // Atualiza o valor da avaliação para a categoria correspondente
        avaliacoes[categoriaId] = value;

        // Verifica se todas as categorias foram avaliadas
        if (VerificaAvaliacoes(avaliacoes) && element !== null) {
            console_print(avaliacoes, element);
        }
    });
});

// Adiciona ouvintes de evento para os botões "sim" e "não"
let sim = document.getElementById('sim');
sim.addEventListener('click', () => {
    element = 1;
    if (VerificaAvaliacoes(avaliacoes)) {
        console_print(avaliacoes, element);
    }
});

let nao = document.getElementById('nao');
nao.addEventListener('click', () => {
    element = 0;
    if (VerificaAvaliacoes(avaliacoes)) {
        console_print(avaliacoes, element);
    }
});

function console_print(avaliacoes, element) {
    console.log(avaliacoes);
    console.log(element);
}

// Configura o evento de clique do botão "prox_button_4" para enviar os dados para o backend
let button_finalizar = document.getElementById('prox_button_4');
button_finalizar.addEventListener('click', () => {
    let lista = [];

    for (let categoria in avaliacoes) {
        lista.push(avaliacoes[categoria]);
    }

    lista.push(element);

    enviar_para_back(lista);
});

function enviar_para_back(lista) {
    lista = lista.join(',');
    $.ajax({
        type: "POST",
        url: "../../../avaliacao/",
        data: {
            csrfmiddlewaretoken: csrf_token,
            avaliacao: lista,
            professor: nome,
            materia: codigo,
        },
        success: function (response) {
            lista = response.split(",");
            console.log(lista);

            let nota_dificuldade = (Number(lista[0]) / 2).toPrecision(2);
            let nota_apoio = (Number(lista[1]) / 2).toPrecision(2);
            let nota_didatica = (Number(lista[2]) / 2).toPrecision(2);

            pintar_estrela_tela(nota_dificuldade, "dificuldade");
            pintar_estrela_tela(nota_apoio, "apoio");
            pintar_estrela_tela(nota_didatica, "didatica");

            console.log(nota_apoio + ", " + nota_didatica + ", " + nota_dificuldade + ", " + avaliacao);

            let txt_didatica = document.getElementById("notas_didatica_media");
            txt_didatica.innerText = `${nota_didatica} de 5`;
            let txt_apoio = document.getElementById("notas_apoio_media");
            txt_apoio.innerText = `${nota_apoio} de 5`;
            let txt_dificuldade = document.getElementById("notas_dificuldade-media");
            txt_dificuldade.innerText = `${nota_dificuldade} de 5`;
        }
    });
}

document.addEventListener('DOMContentLoaded', () => {
    function pintarEstrelas(nota, categoria) {
        var estrelas = document.querySelectorAll('#' + categoria + ' input');
        for (var i = 0; i < estrelas.length; i++) {
            if (parseInt(estrelas[i].value) <= nota) {
                estrelas[i].checked = true;
            }
        }
    }
})

// Função para pintar as estrelas com base na avaliação
function pintarEstrelas(avaliacao, categoria) {
    var estrelas = document.querySelectorAll('#' + categoria + ' input');
    for (var i = 0; i < estrelas.length; i++) {
        if (parseFloat(estrelas[i].value) <= parseFloat(avaliacao)) {
            estrelas[i].checked = true;
        }
    }
}

// Pintando as estrelas para cada categoria
document.addEventListener('DOMContentLoaded', function() {
    // Recebendo os valores das notas do JavaScript
    var nota_dificuldade = parseFloat('{{ nota_dificuldade }}');
    var nota_apoio = parseFloat('{{ nota_apoio }}');
    var nota_didatica = parseFloat('{{ nota_didatica }}');

});


