
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
var modal = document.getElementById('modal_atualizacao');
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

// FUNÇÃO PARA RODAR SCROLL NO CELULAR

if(window.matchMedia("(max-width:764px)").matches) {
    
    
var proximo1 = document.getElementById('prox_button_1').addEventListener('click', (e) => {
    e.preventDefault()
    scroll_x.scrollBy({ left: 760.5, behavior: "smooth" })
});

var voltar1 = document.getElementById('back_button_1').addEventListener('click', (e) => {
    e.preventDefault()
    scroll_x.scrollBy({ left: -760.5, behavior: "smooth" })
});

var proximo2 = document.getElementById('prox_button_2').addEventListener('click', (e) => {
    e.preventDefault()
    scroll_x.scrollBy({ left: 760.5, behavior: "smooth" })
});

var voltar2 = document.getElementById('back_button_2').addEventListener('click', (e) => {
    e.preventDefault()
    scroll_x.scrollBy({ left: -760.5, behavior: "smooth" })
});

var proximo3 = document.getElementById('prox_button_3').addEventListener('click', (e) => {
    e.preventDefault()
    scroll_x.scrollBy({ left: 760.5, behavior: "smooth" })
});

var voltar3 = document.getElementById('back_button_3').addEventListener('click', (e) => {
    e.preventDefault()
    scroll_x.scrollBy({ left: -760.5, behavior: "smooth" })
});

var proximo4 = document.getElementById('prox_button_4').addEventListener('click', (e) => {
    e.preventDefault()
    fundoblur.style.display = "none";
    modal.style.display = "none";
});

}
else {

// FUNÇÃO PARA RODAR SCROLL NO PC

var proximo1 = document.getElementById('prox_button_1').addEventListener('click', (e) => {
    e.preventDefault()
    scroll_x.scrollBy({ left: 738.5, behavior: "smooth" })
});

var voltar1 = document.getElementById('back_button_1').addEventListener('click', (e) => {
    e.preventDefault()
    scroll_x.scrollBy({ left: -738.5, behavior: "smooth" })
});

var proximo2 = document.getElementById('prox_button_2').addEventListener('click', (e) => {
    e.preventDefault()
    scroll_x.scrollBy({ left: 738.5, behavior: "smooth" })
});

var voltar2 = document.getElementById('back_button_2').addEventListener('click', (e) => {
    e.preventDefault()
    scroll_x.scrollBy({ left: -738.5, behavior: "smooth" })
});

var proximo3 = document.getElementById('prox_button_3').addEventListener('click', (e) => {
    e.preventDefault()
    scroll_x.scrollBy({ left: 738.5, behavior: "smooth" })
});

var voltar3 = document.getElementById('back_button_3').addEventListener('click', (e) => {
    e.preventDefault()
    scroll_x.scrollBy({ left: -738.5, behavior: "smooth" })
});

var proximo4 = document.getElementById('prox_button_4').addEventListener('click', (e) => {
    e.preventDefault()
    fundoblur.style.display = "none";
    modal.style.display = "none";
});
    
}






const button_drop = document.querySelector('.drop_button')
const menu = document.querySelector('#drop > .menu');
button_drop.addEventListener("click", (e)=> {
    
    menu.classList.toggle('open')
    button_drop.classList.toggle('open');

    if (!button_drop.contains(e.target) && !menu.contains(e.target)) {
        menu.classList.remove('open')
    }
})
function cursos_find(csrf_token) {
    let input = document.getElementById("input_cursos").value;
    input = input.toUpperCase();
    if (input.length > 2) {
        console.log(input.length + "; " + input);

        $.ajax({
            type: "POST",
            url: "usuario/",
            data: {
                csrfmiddlewaretoken: csrf_token,
                input_cursos: input
            },
            success: function(response) {
                let lista_obj = response.split(";");
                let lista_resultado = [];
                for (let i = 0; i < lista_obj.length; i++) {
                    lista_resultado.push(lista_obj[i].split(','));
                }

                var ul_cursos = document.getElementById('cursos');
                ul_cursos.style.display = "flex";
                ul_cursos.style.flexDirection = "column";
                ul_cursos.style.position = "relative";
                ul_cursos.style.padding = "0.5em 2em";
                ul_cursos.innerHTML = '';

                for (let i = 0; i < lista_resultado.length; i++) {
                    var curso = lista_resultado[i][0];
                    var pessoas = lista_resultado[i][1];

                    var li = document.createElement("li");
                    li.style.position = "relative";
                    li.style.marginBottom = "1em";
                    li.style.color = "black";
                    li.style.display = "flex";
                    li.style.flexDirection = "row";
                    li.style.cursor = "pointer";
                    li.style.alignItems = "center";

                    li.innerText = `${curso}`;

                    (function(curso, pessoas) {
                        li.addEventListener("mouseenter", function () {
                            this.style.color = "#008940";
                            this.style.textShadow = "0 0 2px #008940";
                            this.style.transition = "all 0.3s ease";
                        });

                        li.addEventListener("mouseleave", function () {
                            this.style.color = "black";
                            this.style.textShadow = "none";
                        });

                        li.addEventListener("click", function () {
                            ul_cursos.style.display = "none";
                            document.getElementById("input_cursos").value = curso;
                            // Chama a função enviarDados com o curso e o número de pessoas
                            enviarDados(curso);
                        });
                    })(curso, pessoas);

                    ul_cursos.appendChild(li);
                }
            },
            error: function(xhr, status, error) {
                console.error("Erro na requisição AJAX: " + status + ", " + error);
            }
        });
    }
}

function selecionado(semestre) {
    menu.classList.remove('open');
    const text_menu = document.getElementById("CampoFalado_menu");
    text_menu.textContent = semestre.textContent;
    // Chama a função enviarDados com o semestre
    enviarDados(null, semestre.textContent, null);
}


function enviarDados(curso, semestre, bio) {
    console.log('recebeu enviarDados');
    let csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value;

    $.ajax({
        type: "POST",
        url: "usuario/",
        data: {
            csrfmiddlewaretoken: csrf_token,
            curso: curso,
            semestre: semestre,
            bio: bio
        },
        success: function(response) {
            console.log("Dados enviados com sucesso:", response);
            if (response.status === 'success') {
                window.location.reload(true);
            }
        },
        error: function(xhr, status, error) {
            console.error("Erro na requisição AJAX:", status, error);
        }
    });
}

document.getElementById('prox_button_4').addEventListener('click', (e)=> {
    e.preventDefault();
    const curso = document.getElementById('input_cursos').value;
    const semestre = document.getElementById('CampoFalado_menu').innerText;
    const bio = document.getElementById('bio').value;
    
    enviarDados(curso, semestre, bio);
    window.location.reload(true);
});

