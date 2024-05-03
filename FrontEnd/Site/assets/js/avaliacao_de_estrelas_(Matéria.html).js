// Seleciona todas as etiquetas de estrelas
let starLabels = document.querySelectorAll('.rating label');

// Adiciona um ouvinte de evento de clique a cada etiqueta de estrela
starLabels.forEach(function(label) {
    label.addEventListener('click', function() {
        // Obtém o valor da estrela clicada posição
        let value = this.previousElementSibling.value;

        // Obtém o ID da categoria
        let categoriaId = this.parentElement.id;
        console.log(categoriaId + ': ' + value + ' estrelas de 5')

       let ShowValue = document.getElementById('notas_' + categoriaId);
        ShowValue.innerHTML = (value + " de 5");
    });
});

function PostarAvaliacoes() {
    // mandar avaliações para o banco de dados
}

