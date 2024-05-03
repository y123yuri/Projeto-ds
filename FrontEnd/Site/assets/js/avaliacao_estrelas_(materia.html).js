//CÓDIGO TALVEZ VAI SER DESCARTADO , MAS NÃO ELIMINAR POIS É POSSÍVEL APROVEITAR CÓDIGO 

//PINTAR AS ESTRELAS

function seleciona(name, indice) {
    var stars = document.querySelectorAll('li[name=' + name + ']');

    for (var i = 0; i < stars.length; i++) {
        if (i <= indice)
            stars[i].classList.add("destaque");
        else
            stars[i].classList.remove("destaque");
    }
}

//ESTRELAS DA CATEGORIA DIFICULDADE

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

//ESTRELAS DA CATEGORIA MONITORIA

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

//ESTRELAS DA CATEGORIA DUVIDAS

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

//CONTEUDO PARA QUE O CÓDIGO FUNCIONE

// <div id="box1">

// <h1 class="CampoFalado1"> Avaliação </h1>

// <div class="avaliacao">

//     <h2 class="CampoFalado2"> Dificuldade </h2>
//     <ul id="Dificuldade">
        
//         <li name="star_Dificuldade" class="destaque"></li>
//         <li name="star_Dificuldade" class="star"></li>
//         <li name="star_Dificuldade" class="star"></li>
//         <li name="star_Dificuldade" class="star"></li>
//         <li name="star_Dificuldade" class="star"></li>

//     </ul>
//     <h2 class="notas" id="nota_Dificuldade"></h2>



//     <h2 class="CampoFalado2"> Monitoria </h2>
//     <ul id="Monitoria">
//         <li name="star_Monitoria" class="destaque"></li>
//         <li name="star_Monitoria" class="star"></li>
//         <li name="star_Monitoria" class="star"></li>
//         <li name="star_Monitoria" class="star"></li>
//         <li name="star_Monitoria" class="star"></li>
//     </ul>
//     <h2 class="notas" id="nota_Monitoria"></h2>



//     <h2 class="CampoFalado2"> Dúvidas </h2>
//     <ul id="Duvidas">
//         <li name="star_Duvidas" class="destaque"></li>
//         <li name="star_Duvidas" class="star"></li>
//         <li name="star_Duvidas" class="star"></li>
//         <li name="star_Duvidas" class="star"></li>
//         <li name="star_Duvidas" class="star"></li>
//     </ul>
//     <h2 class="notas" id="nota_Duvidas"></h2>
// </div>


// <h2 id="Postar"> Fazer Avaliação</h2>


// </div>

// .avaliacao ul {
//     list-style: none;
//     padding: 0;
//     position: relative;
// }

// .avaliacao li {
//     display: inline-block;
//     text-shadow: 0 0 1px #ffd000;
// }

// .star::before {
//     cursor: pointer;
//     content: '\2606';
//     color: #ffd000;
//     font-size: 2.5em;
// }

// .destaque::before {
//     content: '\2605';
//     color: #ffd000;
//     font-size: 3em;
//     cursor: pointer;
//     z-index: 999;
// }

// .star:hover::before {
//     content: "\2605";
// }
