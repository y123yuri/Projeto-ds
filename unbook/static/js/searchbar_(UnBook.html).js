//FUNÇÃO DA BARRA DE PESQUISA
function pesquisar() {

    let input = document.getElementById('searchbar').value
    input = input.toLowerCase()

    let x = document.getElementsByClassName('materias')



    // for (i = 0; i < x.length; i++){
    //     if (!x[i].innerHTML.toLowerCase().includes(input)) {
    //         x[i].style.display = 'none'
    //     }else {
    //         x[i].style.display = 'list-item'
    //     }
    // }

}

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
            };
            console.log(lista_resultado)

            var ul = document.getElementById('list_professores');
            ul.innerHTML = '';

            for (i = 0; i < lista_resultado.length; i++) {
                var professor_li = document.createElement("li");



                var imagem_professor = document.createElement('img');

                 

                imagem_professor.width = "50"
                imagem_professor.height = "50"
                imagem_professor.style.borderRadius = "10px";
                imagem_professor.style.position = "relative"
                imagem_professor.style.top = "-1.75em"

                imagem_professor.src = lista_resultado[i][1];
                professor_li.appendChild(imagem_professor);


                professor_li.textContent = lista_resultado[i][0];
                professor_li.style.position = "relative"
                professor_li.style.left = "3em"

                ul.appendChild(professor_li);
                ul.appendChild(imagem_professor);
            }


        }
    })
}




function pesquisa_materia(csrf_token) {
    let input = document.getElementById('searchbar_materia').value
    input = input.toUpperCase()
    console.log(input)
    $.ajax({
        type: "POST",
        url: "pesquisa_materia/",
        data: {
            csrfmiddlewaretoken: csrf_token,
            termo_pesquisa_materias: input
        },
        success: function (response) {
            console.log(input)
            console.log(response)
            lista_obj_materia = response.split(";")
            lista_resultado_materia = []
            for (i = 0; i < lista_obj_materia.length; i++) {
                lista_resultado_materia.push(lista_obj_materia[i].split(','))
            };
            console.log(lista_resultado_materia)
        }
    })
}