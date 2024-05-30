
window.onload = () => {
    var editar_perfil = document.getElementById('edit_profile')
    editar_perfil.style.backgroundColor = '#0B4C9C';
    editar_perfil.style.color = 'whitesmoke';
}


function abrir_modal(id) {

    var others = document.querySelectorAll('.pages')
    others.forEach(element => {

        element.style.backgroundColor = '#f5f5f5';
        element.style.color = 'black';
    })

    var element = document.getElementById(id)
    element.style.backgroundColor = '#0B4C9C';
    element.style.color = 'whitesmoke';
    element.style.transition = "all ease 0.1s"

    var others_boxes = document.querySelectorAll('.boxs')

    if (id === 'edit_profile') {
        others_boxes.forEach(element => {
            element.style.display = "none";
        })

        var Profile = document.getElementById('Profile')
        Profile.style.display = "flex";


    }

    else if (id === 'edit_senha') {

        others_boxes.forEach(element => {
            element.style.display = "none";
        })

        var Senha = document.getElementById('Senha')
        Senha.style.display = "flex";
    }



    else if (id === 'estatistica') {
        others_boxes.forEach(element => {
            element.style.display = "none";
        })

        var Senha = document.getElementById('Estatistica')
        Senha.style.display = "flex";
    }

}

// document.addEventListener('click', (e) => {
//     if (!e.target.closest('#boxes') && !e.target.closest('#modal_imgs')) {
//         console.log('eita')
//         window.location.href = '/'
//     }


//se clicar na tela ele vai pra tela inicial
// })

var img = document.getElementById('img_user');
var modal_img = document.getElementById('modal_imgs');

img.addEventListener('mouseover', (e) => {
    img.style.border = "solid 5px #0B4C9C";
    img.style.filter = "brightness(70%)";
});

img.addEventListener('mouseout', (e) => {
    img.style.border = "none";
    img.style.filter = "none";
});

img.addEventListener('click', (e) => {
    modal_img.style.display = "flex";
    e.stopPropagation(); // Impede que o clique no img feche o modal
});

document.addEventListener('click', (e) => {
    if (!modal_img.contains(e.target) && e.target !== img) {
        modal_img.style.display = "none";
    }
});

function escolha_img(id) {
    var escolhida = document.getElementById(id);
    var user_img = document.getElementById('img_user');
    var computedStyle = getComputedStyle(escolhida);
    user_img.style.backgroundColor = computedStyle.backgroundColor;

    modal_img.style.display = "none";
}








var fzr_avaliacao = document.getElementById('atualizar');
var fundoblur = document.getElementById('fundo_blur');
var modal = document.getElementById('modal_avaliacao');
var scroll_x = document.getElementById('scroll_modal');

fzr_avaliacao.addEventListener('click', () => {
    fundoblur.style.display = "block";
    fundoblur.classList.add('abrir');
    modal.style.display = "flex";
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
    scroll_x.scrollBy({ left: 720, behavior: "smooth" })
});

var voltar1 = document.getElementById('back_button_1').addEventListener('click', (e) => {
    e.preventDefault()
    scroll_x.scrollBy({ left: -720, behavior: "smooth" })
});

var proximo2 = document.getElementById('prox_button_2').addEventListener('click', (e) => {
    e.preventDefault()
    scroll_x.scrollBy({ left: 720, behavior: "smooth" })
});

var voltar2 = document.getElementById('back_button_2').addEventListener('click', (e) => {
    e.preventDefault()
    scroll_x.scrollBy({ left: -720, behavior: "smooth" })
});

var proximo3 = document.getElementById('prox_button_3').addEventListener('click', (e) => {
    e.preventDefault()
    fundoblur.style.display = "none";
    modal.style.display = "none";
});








