
var fzr_avaliacao = document.getElementById('Fazer_avaliacao');
var fundoblur = document.getElementById('fundo_blur');
var modal = document.getElementById('modal_avaliacao');
var scroll_x = document.getElementById('scroll_modal');

fzr_avaliacao.addEventListener('click', () => {
    fundoblur.style.display = "block";
    fundoblur.classList.add('abrir');
    modal.style.display = "block";
    modal.classList.add('abrir');
    scroll_x.scrollLeft = 0;
});

fundoblur.addEventListener('click', (e) => {
    if (e.target === fundoblur) {
        fundoblur.style.display = "none";
        modal.style.display = "none";
    }
});

modal.addEventListener('click', (e) => {
    e.stopPropagation(); // Impede que o clique no modal se propague para o fundo_blur
});



// FUNÇÃO PARA RODAR SCROLL



var proximo1 = document.getElementById('prox_button_1').addEventListener('click', (e) => {
    e.preventDefault()
    scroll_x.scrollBy({ left: 540, behavior: "smooth" })
});

var voltar1 = document.getElementById('back_button_1').addEventListener('click', (e) => {
    e.preventDefault()
    scroll_x.scrollBy({ left: -540, behavior: "smooth" })
});

var proximo2 = document.getElementById('prox_button_2').addEventListener('click', (e) => {
    e.preventDefault()
    scroll_x.scrollBy({ left: 540, behavior: "smooth" })
});

var voltar2 = document.getElementById('back_button_2').addEventListener('click', (e) => {
    e.preventDefault()
    scroll_x.scrollBy({ left: -540, behavior: "smooth" })
});

var proximo3 = document.getElementById('prox_button_3').addEventListener('click', (e) => {
    e.preventDefault()
    scroll_x.scrollBy({ left: 540, behavior: "smooth" })
});

var voltar3 = document.getElementById('back_button_3').addEventListener('click', (e) => {
    e.preventDefault()
    scroll_x.scrollBy({ left: -540, behavior: "smooth" })
});

var proximo4 = document.getElementById('prox_button_4').addEventListener('click', (e) => {
    e.preventDefault()
    fundoblur.style.display = "none";
    modal.style.display = "none";
});




//FUNÇÃO PARA TER O ID IGUAL AO NOME DO USUÁRIO
window.onload = function () {
    var h2Elements = document.querySelectorAll('.usuarios'); // Seleciona o elemento h2 dentro de scroll na página

    if (h2Elements.length >= 0) {
        for (let i = 0; i < h2Elements.length; i++) {
            var h2Element = h2Elements[i];

            var h2Text = h2Element.textContent.trim(); // Obtém o texto dentro do h2 e remove espaços em branco desnecessários
            h2Element.id = h2Text;
        }
    } else {
        console.error('nenhum elemento h2 foi encontrado')
    }

    // criar calendário
    
    for (var i=0;i<globalThis.lista_turno_django.length;i++){
        dia = document.getElementById(globalThis.lista_turno_django[i])
        dia.style.backgroundColor = "#81E28B"
    }

    // pintar estrela

    pintar_estrela_tela(nota_didatica/2, "didatica")
    pintar_estrela_tela(nota_apoio/2, "apoio")
    pintar_estrela_tela(nota_dificuldade/2, "dificuldade")

    // colocando quant de likes

    for (i=0;i<quant_likes.length;i++){
        element = document.getElementById(`like${i}`)
        element.innerText = `${quant_likes[i]}`
        element = document.getElementById(`coracao${i}`)
        if (curtidas[i] === "True"){
            element.style.color = "red";
            element.classList.add('heart');
        } else{
            element.style.color = "grey";
            element.classList.remove('heart');
        }
    }
}

function pintar_estrela_tela(nota, categoria){
    cont_nota =0.5
    while(cont_nota<=5){
        id = `estrela_${cont_nota}_${categoria}`
        estrela = document.getElementById(id)
        estrela.style.color = '#777D89'
        cont_nota +=0.5
    }

    cont_nota =0.5
    while (cont_nota<=nota){
        id = `estrela_${cont_nota}_${categoria}`
        estrela = document.getElementById(id)
        estrela.style.color = '#ffd000'
        cont_nota +=0.5
    }
}

document.querySelector('#comentar').addEventListener('keydown', function (event) {
    if (event.keyCode === 13) {
        postar_comentario();
    }
}); // quando apertar ENTER no teclado ele envia o comentário

function like(element, pk) {
    id = element.id
    id = id.replace("coracao", "")
    contador = document.getElementById(`like${id}`)
    num = Number(contador.innerText)
    
    if (element.style.color === "red") {
        element.style.color = "grey";
        element.classList.remove('heart');
        contador.innerText = `${num-1}`
    } else {
        element.style.color = "red";
        element.classList.add('heart');
        contador.innerText = `${num+1}`
    }
    
    $.ajax({
        type: "POST",
        url: "../../../like/",
        data: {
            csrfmiddlewaretoken: csrf_token,
            comentario: pk,
            materia: codigo,
            professor: nome,
        }, 
        success: function (response)  {
            console.log("")
        }
    })
}


//FUNÇÃO PARA POSTAR O COMENTARIO ESCRITO
function postar_comentario() {

    var conteudo = document.getElementById("comentar").value.trim();
    console.log(conteudo)

    if (conteudo !== "") {

        var comentarioBox = document.createElement('div');
        comentarioBox.id = "@anônimo (coloquei no js direto)"

        var usuario = document.createElement('h2');
        usuario.className = "usuarios";
        var user = document.getElementById('User_js')
        usuario.innerText = '@' + user.textContent;


        var comentario = document.createElement('h3');
        comentario.className = "comentarios";
        comentario.innerText = conteudo;

        var espaco_curtidas = document.createElement('div');
        const curtidas_style = document.querySelector('.curtidas');
        if (curtidas_style) {
            const computedStyle = getComputedStyle(curtidas_style);

            espaco_curtidas.style.display = computedStyle.display;
            espaco_curtidas.style.flexDirection = computedStyle.flexDirection;
            espaco_curtidas.style.fontSize = computedStyle.fontSize;
            espaco_curtidas.style.color = computedStyle.color;
            espaco_curtidas.style.fontWeight = computedStyle.fontWeight;
            espaco_curtidas.style.marginLeft = computedStyle.marginLeft;
            // Adicione outros estilos que você quer copiar aqui
        }

        var Gostei = document.createElement('h3');
        Gostei.innerText = "Gostei";
        
        const gosteiEstilo = document.querySelector('.Gostei');
    if (gosteiEstilo) {
        const computedStyle = getComputedStyle(gosteiEstilo);
        Gostei.style.fontSize = computedStyle.fontSize;
        Gostei.style.color = computedStyle.color;
        Gostei.style.fontWeight = computedStyle.fontWeight;
        Gostei.style.marginLeft = computedStyle.marginLeft;
        Gostei.style.cursor = computedStyle.cursor;
        // Adicione outros estilos que você quer copiar aqui
    }

        var button_like = document.createElement('button')
        const like_style = document.querySelector('.like');
        button_like.type = "button" 
    if (like_style) {
        const computedStyle = getComputedStyle(like_style);
        button_like.style.fontFamily = computedStyle.fontFamily;
        button_like.style.color = computedStyle.color;
        button_like.style.fontSize = computedStyle.fontSize;
        button_like.style.marginLeft = computedStyle.marginLeft;
        button_like.style.cursor = computedStyle.cursor;
        button_like.style.border = computedStyle.border;
        button_like.style.background = computedStyle.background;
        button_like.style.outline = computedStyle.outline;


    }
        var like = document.createElement('i');
        like.style.marginLeft = "15px";
        like.style.color = "grey";
        like.className = "fa-solid fa-heart"
        like.style.fontFamily = "fontAwesome"
        like.style.cursor  = "pointer"
        like.onclick = function() {
        
                if (this.style.color === "red") {
                    this.style.color = "grey";
                    this.classList.remove('heart');
                } else {
                    this.style.color = "red";
                    this.classList.add('heart');
                }
            
        }
    
        button_like.appendChild(like)

        espaco_curtidas.appendChild(Gostei);
        espaco_curtidas.appendChild(like);

        comentarioBox.appendChild(usuario);
        comentarioBox.appendChild(comentario);
        comentarioBox.appendChild(espaco_curtidas);

        var scroll = document.getElementById('scroll');
        scroll.appendChild(comentarioBox);

        comentarioBox.scrollIntoView({ behavior: "smooth" });
        document.getElementById('comentar').value = ' ';

        
    }
    comentario_back(conteudo)
}

function comentario_back(conteudo){
    $.ajax({
        type: "POST",
        url: "../../../comentario/",
        data: {
            csrfmiddlewaretoken: csrf_token,
            comentario: conteudo,
            professor: nome,
            materia: codigo,
        }, 
        success: function (response)  {
            console.log("salvei, comentário")
        }
    })
}

// script.js
document.querySelectorAll('tbody th').forEach(item => {
    item.addEventListener('mouseover', function (e) {
        const modal = document.getElementById('modal_calendario');

        // Verifica se o mouse está sobre o elemento <th> do <tbody>
        if (e.target === item) {
            // Obtém o estilo computado do elemento
            const computedStyle = window.getComputedStyle(item);
            const backgroundColor = computedStyle.backgroundColor;

            // Verifica se o background color corresponde ao desejado
            if (backgroundColor === 'rgb(129, 226, 139)') {
                // Obtém a posição do elemento
                const itemRect = item.getBoundingClientRect();
                const itemID = item.id;

                var h2 = document.getElementById('horario');
                h2.textContent = itemID;

                // Calcula a posição do modal com base nas coordenadas do elemento
                const modalTop = itemRect.top + window.scrollY - 1080;
                const modalLeft = itemRect.left + window.scrollX - 10;

                // Define a posição do modal
                modal.style.top = `${modalTop}px`;
                modal.style.left = `${modalLeft}px`;

                // Exibe o modal
                modal.style.display = 'block';
            }
        }
    });

    item.addEventListener('mouseout', function () {
        const modal = document.getElementById('modal_calendario');
        modal.style.display = 'none';
    });
});

document.querySelectorAll('.button').forEach(button => {
    button.addEventListener('click', function() {

        // Primeiro, remover a classe 'not_selected' de todos os botões
        document.querySelectorAll('.button').forEach(btn => {
            btn.classList.remove('not_selected');
        });

        // Adicionar a classe 'not_selected' a todos os botões que não foram clicados
        document.querySelectorAll('.button').forEach(btn => {
            if (btn !== this) {
                btn.classList.add('not_selected');
            }
        });
    });
});





