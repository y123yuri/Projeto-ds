
//FUNÇÃO PARA ABRIR MODAL DA BIBLIOTECA
var biblioteca = document.getElementById('modal_da_biblioteca')

function abrir_modal_biblioteca() {
    var sla = window.getComputedStyle(biblioteca);
    const display = sla.getPropertyValue('display');

    if (display === 'none') {
        biblioteca.style.display = 'block';
        biblioteca.classList.add('abrir');
    }
    else if (display === 'block') {
        biblioteca.style.display = 'none';
    }
}

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
        comentarioH3responder.className = "responder";

        var comentarioLinkResponder = document.createElement('a');
        comentarioLinkResponder.href = "#comentar";
        comentarioLinkResponder.innerText = "responder";
        // comentarioLinkResponder.onclick = responderComentario();

        comentarioH3responder.appendChild(comentarioLinkResponder);
        comentarioBox.appendChild(comentarioH2);
        comentarioBox.appendChild(comentarioH3);
        comentarioBox.appendChild(comentarioH3responder);
        
        var scroll = document.getElementById('scroll');
        scroll.appendChild(comentarioBox);

        comentarioBox.scrollIntoView({ behavior: "smooth" });
        document.getElementById('comentar').value = ' ';
    }

}

function responder_comentario() {
    console.log('em desenvolvimento')
}