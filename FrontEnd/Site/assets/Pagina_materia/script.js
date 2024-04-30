let star = document.querySelectorAll('li');

function atualizarContagem(categoriaId, estrelasAtivas) {
    console.log('Atualizando contagem para a categoria ' + categoriaId + '...');

    var categoria = document.getElementById(categoriaId);
    var totalEstrelas = categoria.querySelectorAll('.star-icon').length;
    var estrelasDeCinco = categoria.querySelectorAll('.star-icon[data-avaliacao="5"]').length;

    console.log("Categoria: " + categoriaId + ", " + estrelasAtivas + " estrelas de 5");
    expoeNaTela(categoriaId, estrelasAtivas);
}

var stars = document.querySelectorAll('.star-icon');

stars.forEach(function (star) {
    star.addEventListener('click', function (e) {
        var classStar = e.target.classList;

        if (!classStar.contains('ativo')) {
            stars.forEach(function (star) {
                star.classList.remove('ativo');
            });
            classStar.add('ativo');
            console.log('esse é o valor da estrelas ' + e.target.getAttribute('data-avaliacao'));

            var estrelasAtivas = e.target.getAttribute('data-avaliacao');

            var categoriaId = e.target.closest('.avaliacao').id;

            atualizarContagem(categoriaId, estrelasAtivas); // Atualiza a contagem ao clicar em uma estrela
        }
    });
});

function expoeNaTela(categoriaId, estrelasAtivas) {
    var showValue = document.getElementById('nota');
    showValue.innerHTML = estrelasAtivas + " de 5";
}