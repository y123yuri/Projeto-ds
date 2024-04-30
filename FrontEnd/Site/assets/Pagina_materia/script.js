function reproduzirMateria2(materias) {
    console.log('vizinho tb')
    var reproduzir = materias.textContent

    document.getElementById('CampoFalado2').textContent = reproduzir;
}


var stars = document.querySelectorAll('.star-icon');

document.addEventListener('click', function (e) {
    var classStar = e.target.classList;
    
    if (!classStar.contains('ativo')) {
        stars.forEach(function (star) {
            star.classList.remove('ativo');
        });
        classStar.add('ativo');
        console.log(e.target.getAttribute('data-avaliacao'));
    }
});

