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

    $.ajax({
        type: "POST",
        url: "pesquisa_prof/",
        data: {
            csrfmiddlewaretoken: csrf_token,
            termo_pesquisa: input
        },
        success: function (response) {
            console.log(response)
            lista_obj = response.split(";")
            lista_resultado = []

            for (i = 0; i < lista_obj.length; i++) {
                lista_resultado.push(lista_obj[i].split(','))
            };//percorrer todos e separar em arrays

            var ul_professores = document.getElementById('list_professores');
            ul_professores.innerHTML = '';

            for (i = 0; i < lista_resultado.length; i++) {
                //percorrer todos e conferir se é igual ao da barra de pesquisa

                var imagem_professor = document.createElement('img');
                imagem_professor.src = lista_resultado[i][1];

                imagem_professor.width = "50"
                imagem_professor.height = "50"
                imagem_professor.style.borderRadius = "10px";
                imagem_professor.style.position = "absolute";
                imagem_professor.style.left = "-3em"
                imagem_professor.style.top = "-0.5em"
                imagem_professor.style.marginBottom = "2em"

                var professor_li = document.createElement("li");

                professor_li.style.position = "relative"
                professor_li.style.left = "2em"
                professor_li.style.marginBottom = "2em"

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


                ul_professores.appendChild(professor_li);
                professor_li.appendChild(imagem_professor);
                professor_li.appendChild(link_professor);
            }


        }
    })
}


function pesquisa_materia(csrf_token) {
    let input = document.getElementById('searchbar_materia').value
    input = input.toUpperCase()

    $.ajax({
        type: "POST",
        url: "pesquisa_materia/",
        data: {
            csrfmiddlewaretoken: csrf_token,
            termo_pesquisa_materias: input
        },
        success: function (response) {
            console.log(response)
            lista_obj_materia = response.split(";")
            lista_resultado_materia = []


            for (i = 0; i < lista_obj_materia.length; i++) {
                lista_resultado_materia.push(lista_obj_materia[i].split(','))
            }; //percorrer todos e separar em arrays

            var ul_materias = document.getElementById('list_materias');
            ul_materias.innerHTML = '';


            for (let i = 0; i < lista_obj_materia.length; i++) {
                //percorrer todos e conferir se é igual ao da barra de pesquisa

                var materias = document.createElement("li")

                materias.style.position = "relative"
                materias.style.left = "-0.5em"
                materias.style.marginBottom = "1.5em"

                var link_materias = document.createElement("a")
                link_materias.textContent = lista_resultado_materia[i][1];
                link_materias.addEventListener('click', function(e) {
                    e.preventDefault();
                    abrirModal_Materia2(lista_resultado_materia[i][1]);
                    
                    var sla = "sla"
                    console.log(sla)
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

                ul_materias.appendChild(materias);
                materias.appendChild(link_materias);
            }

        }

    })
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
function abrirModal_Materia2(textoMateria){
    
    Materia2.classList.add('abrir'); 
    Materia.classList.remove('abrir');
    
    var CampoFalado2 = document.getElementById('nome_materia');
    console.log(CampoFalado2)
    CampoFalado2.innerText = textoMateria;
    console.log('esse' + textoMateria)
}

//FUNÇÃO PARA FECHAR CASO CLIQUE FORA DO MODAL
document.addEventListener('click', e => {
    if (!e.target.classList.contains('barra_pesquisa') && !e.target.classList.contains('botoes') && !e.target.classList.contains('CampoProcura') && !e.target.closest('.CampoProcura ul') && !e.target.closest('.janela_materia2') && 
    !e.target.closest('.CampoProcura #list_professores li') && !e.target.classList.contains('list')) {

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
    localStorage.setItem("materia",materia)
}

//PASSAR PROFESSOR PARA PÁGINA Materia.html
function reproduzirProfessor(element, num) {

    var professor_pega = document.getElementById('professor_' + num).textContent;
    localStorage.setItem("professor", professor_pega)
}