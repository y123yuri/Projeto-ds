
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
    alert('avaliacao enviada com sucesso!')
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
}

document.querySelector('#comentar').addEventListener('keydown', function (event) {
    if (event.keyCode === 13) {
        postar_comentario();
    }
}); // quando apertar ENTER no teclado ele envia o comentário

//FUNÇÃO PARA POSTAR O COMENTARIO ESCRITO
function postar_comentario() {

    var conteudo = document.getElementById("comentar").value.trim();
    console.log(conteudo)

    if (conteudo !== "") {

        var comentarioBox = document.createElement('div');
        comentarioBox.id = "@anônimo (coloquei no js direto)"

        var comentarioH2 = document.createElement('h2');
        comentarioH2.className = "usuarios";
        comentarioH2.innerText = '@Anônimo';

        var comentarioH3 = document.createElement('h3');
        comentarioH3.className = "comentarios";
        comentarioH3.innerText = conteudo;

        var comentarioH3responder = document.createElement('h3');
        comentarioH3responder.className = "curtidas";

        var comentarioLinkResponder = document.createElement('a');
        comentarioLinkResponder.onclick = "like(comentarioLinkResponder)"
        comentarioLinkResponder.innerText = "Gostei";


        var like = document.createElement('i');
        like.className = "fa-solid fa-heart"
        // comentarioLinkResponder.onclick = responderComentario();

        comentarioH3responder.appendChild(comentarioLinkResponder);
        comentarioH3responder.appendChild(like);

        comentarioBox.appendChild(comentarioH2);
        comentarioBox.appendChild(comentarioH3);
        comentarioBox.appendChild(comentarioH3responder);

        var scroll = document.getElementById('scroll');
        scroll.appendChild(comentarioBox);

        comentarioBox.scrollIntoView({ behavior: "smooth" });
        document.getElementById('comentar').value = ' ';
    }

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


function like(element) {
    console.log('oa')

    document.querySelectorAll('.like').forEach(item => {
        item.addEventListener('click', function (e) {

            if (e.target === item) {

                var like = document.querySelectorAll('.like')
                if (like.style.color === "red") {
                    like.style.color = "grey";
                }
                else {
                    like.style.color = "red";
                    like.classList.add('heart');
                    element.style.color = "red";
                }
            }


        });
    });




}

