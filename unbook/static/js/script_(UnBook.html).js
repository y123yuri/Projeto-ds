// VARIAVEIS
var perguntas = document.getElementById('perguntas');
var Professor = document.getElementById('janela_professor');
var pesquisa = document.getElementById('perguntas');
var Materia = document.getElementById('janela_materia');
var Materia2 = document.getElementById('janela_materia2');
var SearchBar = document.getElementById('searchbar');

//FUNÇÃO DA BARRA DE PESQUISA

function pesquisa_prof(csrf_token) {
    let input = document.getElementById("searchbar_prof").value
    input = input.toUpperCase()
    if (input.length > 2) {
        $.ajax({
            type: "POST",
            url: "pesquisa_prof/",
            data: {
                csrfmiddlewaretoken: csrf_token,
                termo_pesquisa: input
            },
            success: function (response) {
                lista_obj = response.split(";")
                lista_resultado = []
                for (i = 0; i < lista_obj.length; i++) {
                    lista_resultado.push(lista_obj[i].split(','))
                };//percorrer todos e separar em arrays

                var ul_professores = document.getElementById('list_professores');
                ul_professores.style.display = "flex"
                ul_professores.style.flexDirection = "column"
                ul_professores.style.position = "relative"
                ul_professores.style.padding = "0.5em 2em"
                ul_professores.innerHTML = '';

                if(window.matchMedia("(max-width:764px)").matches) {
                    ul_professores.style.padding = "0.5em 1em"

                }
                
                
                for (i = 0; i < lista_resultado.length; i++) {
                    //percorrer todos e conferir se é igual ao da barra de pesquisa
                
                    
                    var professor_li = document.createElement("li");
                    
                    professor_li.style.position = "relative"
                    professor_li.style.marginBottom = "1em"
                    professor_li.style.display = "flex"
                    professor_li.style.flexDirection = "row"
                    professor_li.style.alignItems = "center";
                    
                    var imagem_professor = document.createElement('img');
                    imagem_professor.src = lista_resultado[i][1];

                    imagem_professor.width = "10%"
                    imagem_professor.height = "10%"
                    imagem_professor.style.borderRadius = "5px";
                    imagem_professor.style.display = "block";
                    imagem_professor.style.marginRight = "1em";
                    

                    var link_professor = document.createElement("a")
                    link_professor.href = 'professor/' + lista_resultado[i][0];
                    link_professor.textContent = lista_resultado[i][0];
                    link_professor.classList.add("lista_professores");

                    link_professor.addEventListener("mouseenter", function () {
                        // Adicionar a classe 'hover' quando o mouse entrar no link
                        this.style.color = "#008940";
                        this.style.textShadow = "0 0 2px #008940"
                        this.style.transition = "all 0.3s ease"
                    });

                    link_professor.addEventListener("mouseleave", function () {
                        // Remover a classe 'hover' quando o mouse sair do link
                        this.style.color = "black";
                        this.style.textShadow = "none"
                    });

                    link_professor.style.color = "black";
                    link_professor.style.textDecoration = "none";
                    link_professor.style.display = "block";

                    
                    if(window.matchMedia("(max-width:764px)").matches) {
                        link_professor.style.fontSize = "0.80em";

                    }

                    
                    ul_professores.appendChild(professor_li);
                    professor_li.appendChild(imagem_professor);
                    professor_li.appendChild(link_professor);
                }
            }
        })
    }

}


function pesquisa_materia(csrf_token) {
    let input = document.getElementById('searchbar_materia').value
    input = input.toUpperCase()

    let CampoProcura = document.querySelector('.CampoProcura')
    CampoProcura.style.display = "block"

    $.ajax({
        type: "POST",
        url: "pesquisa_materia/",
        data: {
            csrfmiddlewaretoken: csrf_token,
            termo_pesquisa_materias: input
        },
        success: function (response) {
            lista_obj_materia = response.split(";")
            lista_resultado_materia = []


            for (i = 0; i < lista_obj_materia.length; i++) {
                lista_resultado_materia.push(lista_obj_materia[i].split(','))
            }; //percorrer todos e separar em arrays

            var ul_materias = document.getElementById('list_materias');
            ul_materias.style.padding = '0.5em 1em';
            ul_materias.style.textAlign = "left"
            ul_materias.innerHTML = '';


            for (let i = 0; i < lista_obj_materia.length; i++) {
                //percorrer todos e conferir se é igual ao da barra de pesquisa
                var semestre = document.getElementById("semestre").value

                var materias = document.createElement("li")

        
                    materias.style.position = "relative"
                    materias.style.marginBottom = "1.5em"
                    materias.style.marginLeft = "1em"
        
                    if(window.matchMedia("(max-width:764px)").matches) {
                        materias.style.position = "relative"
                        materias.style.margin = "auto"
                        materias.style.marginBottom = "0.5em"
                        materias.style.textAlign = "left"
                    }


                var link_materias = document.createElement("a")
                link_materias.textContent = lista_resultado_materia[i][1] + " (" + lista_resultado_materia[i][0] + ")";
                link_materias.addEventListener('click', function (e) {
                    e.preventDefault();
                    abrirModal_Materia2(lista_resultado_materia[i][1]);
                    abrir_turmas(lista_resultado_materia[i][0], csrf_token);


                })


                link_materias.addEventListener("mouseenter", function () {
                    // Adicionar a classe 'hover' quando o mouse entrar no link
                    this.style.color = "#008940";
                    this.style.textShadow = "0 0 2px #008940"
                    this.style.transition = "all 0.3s ease"
                });

                link_materias.addEventListener("mouseleave", function () {
                    // Remover a classe 'hover' quando o mouse sair do link
                    this.style.color = "black";
                    this.style.textShadow = "none"
                });


                link_materias.style.color = "black";
                link_materias.style.textDecoration = "none";

                if(window.matchMedia("(max-width:764px)").matches) {
                    link_materias.style.fontSize = "0.75em";
                    link_materias.style.left = "1em";
                }


                ul_materias.appendChild(materias);
                materias.appendChild(link_materias);
            }

        }

    })
}
turmas = []
function abrir_turmas(materia_codigo, csrf_token) {
    var semestre = document.getElementById("semestre").value
    console.log(`semestre: ${semestre}`)
    $.ajax({
        type: "POST",
        url: "pesquisa_turma/",
        data: {
            csrfmiddlewaretoken: csrf_token,
            codigo: materia_codigo
        },
        success: function (response) {
            lista_obj_turma = response.split(";")
            lista_resultado_turma = []
            for (i = 0; i < lista_obj_turma.length; i++) {
                lista_resultado_turma.push(lista_obj_turma[i].split(','))
            }; //percorrer todos e separar em arrays [foto, nome_prof, turno, codigo, semestre]
            turmas = lista_resultado_turma
            console.log(turmas)
            coloca_turma()
            
    }
    })

}

function coloca_turma(){
    console.log("oi")
    scroll_div = document.getElementById('scroll')
    scroll_div.innerHTML = ""
    semestre = document.getElementById("semestre").value
    if(window.matchMedia("(max-width:764px)").matches) {
        professor = `display: block;

        position: relative;
        width: auto;
        height: auto;
        align-items: center;
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 25px;
        box-shadow: 0 0 10px black;
        margin: 1em;
        padding: 1em 1em;
        text-decoration: none;
    
        transition: all 0.3s ease-in-out;`

        classe_professores = `display: inline-block;
        
        position: relative;
        top: -1.5em;
        margin-left: 4em;
        
        font-weight: 600;
        font-size: 0.80em;
        color: black;
        text-align:center;
        padding: 0 0.5em;
        width:90%;`

        box_style = `"display: inline-block;
        cursor: pointer;
        justify-content: center;
        align-items: center;
        background-color: #008940;
        width: 5em;
        height: 2.5em;"`
        
        box_img = `"display: block;
            
            width: 3em;
            height: 3em;
            position: relative;
            top: 0.8em;"`
    } else if(window.matchMedia("(min-width:765px)").matches) {
        professor = `display: block;

        position: relative;
        width: auto;
        height: auto;
        align-items: center;
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 25px;
        box-shadow: 0 0 10px black;
        margin: 1em;
        padding: 1em 1em;
        text-decoration: none;
        
        transition: all 0.3s ease-in-out;`
        
        classe_professores = `display: inline-block;
        
        position: relative;
        top: -1.8em;
        margin-left: 4em;
        font-size:4em;
        font-weight: 600;
        font-size: 1.2em;
        color: black;
        text-align:center;
        width:90%;`
        box_style = `"display: inline-block;
        cursor: pointer;
        justify-content: center;
        align-items: center;
        background-color: #008940;
        width: 5em;
        height: 5em;"`
        box_img = `"display: block;
        width: 5em;
        height: 5em;
        position: relative;
        top: 0.8em;
        left: 0.8em;"`
    }

    for (let i = 0; i < turmas.length; i++) {
        
        ancora = document.createElement("a")
        texto = document.createElement("p")
        texto.textContent = `${turmas[i][1]}`
        texto.style = classe_professores


        ancora.innerHTML = `<img style=${box_img} src="${turmas[i][0]}">`
        ancora.appendChild(texto)


        ancora.href = `../materia/${semestre}/${turmas[i][3]}/${turmas[i][1]}`
        ancora.style = professor
        ancora.style.box_shadow = 0
        ancora.addEventListener("mouseenter", function () {
            // Adicionar a classe 'hover' quando o mouse entrar no link
            this.style.transform = "scale(1.01)"
        });

        ancora.addEventListener("mouseleave", function () {
            // Remover a classe 'hover' quando o mouse sair do link
            this.style.transform = "scale(1)"
        });

        if (semestre === turmas[i][4]){
            console.log(`${semestre}, ${turmas[i][4]}`)
            scroll_div.appendChild(ancora)
        }

    }
    

if (scroll_div.innerHTML == ""){
    console.log("tem ninguem :(")
    ancora = document.createElement("a")
    texto = document.createElement("p")
    texto.textContent = "SEM PROFESSORES NESSE SEMESTRE"
    ancora.innerHTML = `<img style=${box_img} src="static/image/dog-sad.gif">`
    ancora.appendChild(texto)
    ancora.style = professor
    texto.style = classe_professores
    scroll_div.appendChild(ancora)
    }
}


//FUNÇÕES PARA ABRIR MODAIS
function abrirModal_Professor() {

    perguntas.style.display = 'none';
    Professor.classList.add('abrir');

}

function abrirModal_Materia() {

    perguntas.style.display = 'none';
    Materia.classList.add('abrir');

}

//FUNÇÕES PARA ABRIR SEGUNDOS MODAIS 
function abrirModal_Materia2(textoMateria) {

    Materia2.classList.add('abrir');
    Materia.classList.remove('abrir');

    var CampoFalado2 = document.getElementById('nome_materia');
    CampoFalado2.innerText = textoMateria;
}


//FUNÇÃO PARA FECHAR CASO CLIQUE FORA DO MODAL
document.addEventListener('click', e => {
    if (!e.target.classList.contains('barra_pesquisa') && !e.target.classList.contains('botoes') && !e.target.classList.contains('CampoProcura') && !e.target.closest('.CampoProcura ul') && !e.target.closest('.janela_materia2') &&
        !e.target.closest('.CampoProcura #list_professores li') && !e.target.classList.contains('list')) {
        var input1 = document.getElementById('searchbar_prof')
        var input2 = document.getElementById('searchbar_materia')
        input1.value = '';
        input2.value = '';
        fecharModal();
    }
});

//FUNÇÃO PARA FECHAR MODAIS
function fecharModal() {
    perguntas.style.display = 'block';
    Materia.classList.remove('abrir');
    Professor.classList.remove('abrir');
    Materia2.classList.remove('abrir');
}

//ABRIR NO PROXIMO MODAL OS DADOS DO ANTIGO 

//PASSAR MATERIA PARA SEGUNDO MODAL
function reproduzirMateria(materias) {

    var reproduzir_materia = materias.textContent;
    document.getElementById('CampoFalado2').textContent = reproduzir_materia;

    //PASSAR MATERIA PARA PÁGINA Materia.html
    var materia = reproduzir_materia;
    localStorage.setItem("materia", materia)
}

//PASSAR PROFESSOR PARA PÁGINA Materia.html
function reproduzirProfessor(element, num) {

    var professor_pega = document.getElementById('professor_' + num).textContent;
    localStorage.setItem("professor", professor_pega)
}