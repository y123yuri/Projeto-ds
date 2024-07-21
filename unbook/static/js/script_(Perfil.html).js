
window.onload = () => {
    var editar_perfil = document.getElementById('edit_profile')
    editar_perfil.style.backgroundColor = '#0B4C9C';
    editar_perfil.style.color = 'whitesmoke';
}

$(document).ready(function() {
    $('#usernameForm').on('submit', function(event) {
        event.preventDefault();
        
        var csrfToken = $('[name=csrfmiddlewaretoken]').val();
        var newUsername = $('#username').val();

        $.ajax({
            type: 'POST',
            url: "username/",
            headers: { 'X-CSRFToken': csrfToken },
            data: JSON.stringify({ 'username': newUsername }),
            contentType: 'application/json',
            success: function(response) {
                if (response.status === 'success') {
                    alert('Username alterado com sucesso!');
                    window.location.reload();

                } else {
                    alert('Erro: Usuario já existente');
                }
            },
            error: function(response) {
                alert('Erro: ' + response.responseJSON.message);
            }
        });
    });
});

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

    else if (id === 'edit_Config') {

        others_boxes.forEach(element => {
            element.style.display = "none";
        })

        var Senha = document.getElementById('Config')
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

var modal_visib = document.getElementById('visib_modal')
var lampinha = document.getElementById('lampinha')
lampinha.addEventListener('mouseover', (e)=> {
    e.preventDefault()   
        modal_visib.style.display	= "flex"
});

lampinha.addEventListener('mouseout', (e)=> {
        modal_visib.style.display = "none"    
});   


// document.addEventListener('click', (e) => {
//     if (!e.target.closest('#boxes') && !e.target.closest('#modal_imgs')) {
//         console.log('eita')
//         window.location.href = '/'
//     }


//se clicar na tela ele vai pra tela inicial
// })
function certeza() {

        var modal_certeza = document.getElementById('modal_certeza')
        modal_certeza.style.display = 'flex'
        fundo_blur.style.display = 'block'

    fundo_blur.addEventListener('click', (e)=> {
        e.preventDefault()
        modal_certeza.style.display = 'none'
        fundo_blur.style.display = 'none'
    })

    var botao_nao = document.getElementById('nao_c').addEventListener('click', (e)=>{
        e.preventDefault()
        modal_certeza.style.display = 'none'
        fundo_blur.style.display = 'none'
    })
}




var img = document.getElementById('img_user');
var modal_img = document.getElementById('modal_imgs');

img.addEventListener('mouseover', (e) => {
    img.style.border = "solid 5px #0B4C9C";
    document.getElementById('edit').style.display = 'block'
    img.style.filter = "brightness(80%)";

});

img.addEventListener('mouseout', (e) => {
    img.style.border = "none";
    img.style.filter = "none";
    document.getElementById('edit').style.display = 'none'
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

function escolha_img(element, csrf_token) {
    // window.location.reload(true)
    var user_img = document.getElementById('img_img');
    
    // Remove existing children
    while (user_img.firstChild) {
        user_img.removeChild(user_img.firstChild);
    }

    atualizar_foto(element.id, csrf_token);

    // Add the edit icon
    var edit_icon = document.createElement('i');
    edit_icon.id = 'edit';
    edit_icon.className = 'bi bi-pencil-square';
    user_img.appendChild(edit_icon);

    // Close the modal (assuming modal_img is globally defined)
    modal_img.style.display = "none";
    window.location.reload(true)
    window.location.reload(true)
}

function atualizar_foto(foto_id, csrf_token) {
    $.ajax({
        type: "POST",
        url: "usuario/",
        data: {
            csrfmiddlewaretoken: csrf_token,
            foto: foto_id
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
    enviarDados(null, semestre.textContent, null, null);
}

// function setVisibilit(element) {
//     enviarDados(null, null, null, element);
// }

function enviarDados(curso, semestre, bio, visibilidade) {
    console.log('recebeu enviarDados');
    let csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value;

    $.ajax({
        type: "POST",
        url: "usuario/",
        data: {
            csrfmiddlewaretoken: csrf_token,
            curso: curso,
            semestre: semestre,
            bio: bio,
            visibilidade: visibilidade
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
    const visibilidade = document.getElementById('priv').value
    console.log(visibilidade)
    enviarDados(curso, semestre, bio, visibilidade);
    window.location.reload(true);
});


// aaaaaquiiiiiiiiii
function setVisibility(element, valor){

        // Primeiro, remover a classe 'not_selected' de todos os botões
        document.querySelectorAll('.perfil_visivel').forEach(btn => {
            btn.classList.remove('not_selected');
            btn.style.backgroundColor = "#81E28B"

            enviarDados(null, null, null, valor);
        });

        // Adicionar a classe 'not_selected' a todos os botões que não foram clicados
        document.querySelectorAll('.perfil_visivel').forEach(btn => {
            if (btn !== element) {
                btn.classList.add('not_selected');
                btn.style.backgroundColor = "whitesmoke"
            }
        });
    
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');


$(document).ready(function() {
    $('#sim_c').click(function(e) {
        e.preventDefault();

        $.ajax({
            url: "excluir_usuario/", // url ajax
            type: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function(response) {
                if (response.success) {
                    alert("Sua conta foi deletada com sucesso.");
                    window.location.href = "/";
                } else {
                    alert("Houve um erro ao deletar sua conta: " + response.error);
                }
            },
            error: function(xhr, errmsg, err) {
                alert("Houve um erro ao deletar sua conta: " + errmsg);
            }
        });
    });
});