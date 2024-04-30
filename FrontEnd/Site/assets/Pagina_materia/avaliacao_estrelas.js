//PINTAR

function seleciona(name, indice) {
    var stars = document.querySelectorAll('li[name=' + name + ']');

    for (var i = 0; i < stars.length; i++) {
        if (i <= indice)
            stars[i].classList.add("destaque");
        else
            stars[i].classList.remove("destaque");
    }
}

//DIFICULDADE

var starsClickedDificuldade = document.querySelectorAll('li[name=star_Dificuldade]');

for (var i = 0; i < starsClickedDificuldade.length; i++) {
    (function (name, i) {
        starsClickedDificuldade[i].addEventListener('click', function (e) {

            var categoriaId = e.target.closest('ul').id;
            console.log('Atualizando contagem para a categoria ' + categoriaId + '...');

            seleciona(name, i, categoriaId);

            var tantos_de_5 = i + 1;
            var showValue = document.getElementById('nota_' + categoriaId);
            showValue.innerHTML = (tantos_de_5 + ' de 5')
            console.log(showValue)


        });
    })(starsClickedDificuldade[i].getAttribute("name"), i);
}

// MONITORIA

var starsClickedMonitoria = document.querySelectorAll('li[name=star_Monitoria]');

for (var i = 0; i < starsClickedMonitoria.length; i++) {
    (function (name, i) {
        starsClickedMonitoria[i].addEventListener('click', function (e) {

            var categoriaId = e.target.closest('ul').id;
            console.log('Atualizando contagem para a categoria ' + categoriaId + '...');

            seleciona(name, i, categoriaId);

            var tantos_de_5 = i + 1;
            var showValue = document.getElementById('nota_' + categoriaId);
            showValue.innerHTML = (tantos_de_5 + ' de 5')
            console.log(showValue)


        });
    })(starsClickedMonitoria[i].getAttribute("name"), i);
}

//DUVIDAS

var starsClickedDuvidas = document.querySelectorAll('li[name=star_Duvidas]');

for (var i = 0; i < starsClickedDuvidas.length; i++) {
    (function (name, i) {
        starsClickedDuvidas[i].addEventListener('click', function (e) {

            var categoriaId = e.target.closest('ul').id;
            console.log('Atualizando contagem para a categoria ' + categoriaId + '...');

            seleciona(name, i, categoriaId);

            var tantos_de_5 = i + 1;
            var showValue = document.getElementById('nota_' + categoriaId);
            showValue.innerHTML = (tantos_de_5 + ' de 5')
            console.log(showValue)


        });
    })(starsClickedDuvidas[i].getAttribute("name"), i);
}

