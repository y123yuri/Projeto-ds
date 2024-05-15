
// Objeto para armazenar as avaliações de cada categoria
let avaliacoes = {
    'Dificuldade': '',
    'Monitoria': '',
    'Dúvidas': ''
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

// Função para reiniciar as avaliações
function reiniciarAvaliacoes() {
    avaliacoes = {
        'Dificuldade': '',
        'Monitoria': '',
        'Dúvidas': ''
    };
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
            console_print(avaliacoes);
        }
    });
});

function console_print(avaliacoes) {
    
    var materia = document.getElementById('Materia').textContent;

    var professor = document.getElementById('Prof_js').textContent

    console.log( '\n' + 'Gerando avaliacao para materia: \n\n' + materia + '\nregida por ' + professor  + ' : \n\n' )

    for (let categoria in avaliacoes) {
        console.log(categoria + ': ' + avaliacoes[categoria] + ' estrelas de 5;');
    }
}

