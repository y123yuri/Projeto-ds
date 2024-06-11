// window.onload = function () {
//     // colocando quant de likes
//     console.log("entrei!" +quant_likes.length)
//     for (i=0;i<quant_likes.length;i++){
//         console.log(`cont_link${i}`)
//         element = document.getElementById(`cont_link${i}`)
//         console.log(element)
//         element.innerText = `cont: ${quant_likes[i]}`
//          // numero de likes (oi)
        
//         elements = document.getElementById(`coracao${i}`);
//         console.log(elements) // coraçao botao
        
//         if (curtidas[i] === 1){
//             elements.style.color = "red";
//             elements.classList.add('heart');
//         } else{
//             elements.style.color = "grey";
//             elements.classList.remove('heart');  //AAAAAAAAAAAAAA RRRRRRRRRRRUUUUUUUUUUMMMMMMMMMMMAAAAAAAAAAARRRR
//         }
//     }
// }


var fundo_blur = document.getElementById('fundo_blur');
var modal = document.getElementById('modal_upload');

function abrir_modal () {

    fundo_blur.style.display = 'block';

    modal.classList.add('abrir');
    modal.style.display = 'block'

}

function enviar() {
    var link_enviado = document.getElementById('poe_links').value;
    var nome_link = document.getElementById('queLinkéEsse').value;

    if (link_enviado !== '' && nome_link !== '') {
        envia_link_back(nome_link, link_enviado);
        fechar_modal();
    } else {
        alert('Tem que ter um link ai dentro man');
    }
}

function envia_link_back(nome_link, link) {
    // Remover "https://" e "www." do link
    link = link.replace(/^(https?:\/\/)?(www\.)?/, '');

    console.log(nome_link, link);
    $.ajax({
        type: "POST",
        url: "../../../../resumo/",
        data: {
            csrfmiddlewaretoken: csrf_token,
            materia: codigo,
            professor: nome,
            link: link,
            titulo: nome_link,
        }, 
        success: function(response) {
            if (response === "erro") {
                console.log(response);
                console.log("link repetido piranha");
                deu_certo = false;
            } else {
                console.log(response);
                deu_certo = true;
            }
        },
        error: function(xhr, status, error) {
            console.error("Erro na requisição AJAX:", status, error);
        }
    })
    window.location.reload(true);
}


document.addEventListener('click', function(e) {
    if(e.target === fundo_blur) {
        fundo_blur.style.display = 'none';
        modal.style.display = 'none';
    } 
})

function fechar_modal() {
    fundo_blur.style.display = 'none';
        modal.style.display = 'none';
}