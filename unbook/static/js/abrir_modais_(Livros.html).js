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

window.onload = function () {
  // colocando quant de likes
  for (i = 0; i < quant_likes.length; i++) {
    var element = document.getElementById(`quant_likes${i}`);
    element.innerText = `${quant_likes[i]}`;
    element = document.getElementById(`curtir${i}`);

    if (curtidas[i] == 1) {
      console.log("ele curtiu");
      element.style = "color: red";
    } else {
      console.log("não curtiu :(");
      element.style = "color: grey";
    }
  }
}


var fundo_blur = document.getElementById("fundo_blur");
var modal = document.getElementById("modal_upload");

function abrir_modal() {
  fundo_blur.style.display = "block";

  modal.classList.add("abrir");
  modal.style.display = "block";
}

function enviar() {
  var link_enviado = document.getElementById("poe_links").value;
  var nome_link = document.getElementById("queLinkéEsse").value;

  if (link_enviado !== "" && nome_link !== "") {
    envia_link_back(nome_link, link_enviado);
    fechar_modal();

    // window.location.reload();
    // window.location.reload(true);
  } else {
    alert("Por favor, insira um nome ou um link.");
  }
}

var selec = document.getElementById("selec");
var selec_space = document.getElementById("selec_space");
selec.addEventListener("click", (e) => {
  selec.classList.toggle("open");
  selec_space.classList.toggle("open");

  if (!selec_space.contains(e.target) && !selec.contains(e.target)) {
    selec_space.classList.remove("open");
    selec_space.textContent = "Selecionar";
  }
});

function selec_selecionado(element) {
  selec.textContent = element.textContent;
  selec_space.classList.remove("open");
}

function envia_link_back(nome_link, link) {
  // Remover "https://" e "www." do link
  link = link.replace(/^(https?:\/\/)?(www\.)?/, "");

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
    success: function (response) {
      if (response === "erro") {
        console.log(response);
        console.log("link repetido");
        deu_certo = false;
      } else {
        console.log(response);
        deu_certo = true;
      }
    },
    error: function (xhr, status, error) {
      console.error("Erro na requisição AJAX:", status, error);
    },
  });
  // window.location.reload(true);
}

document.addEventListener("click", function (e) {
  if (e.target === fundo_blur) {
    fundo_blur.style.display = "none";
    modal.style.display = "none";
  }
});

function fechar_modal() {
  fundo_blur.style.display = "none";
  modal.style.display = "none";
}

function RetirarAlerta(element) {
  element.style.display = "none";
}


// curtir links
function curtir(id, id_elemento) {
  console.log(id_elemento);

  var elemento = document.getElementById(id_elemento);
  $.ajax({
    type: "POST",
    url: "../../../../curtir_resumo/",
    data: {
      csrfmiddlewaretoken: csrf_token,
      id_resumo: id,
    },
    success: function (response) {
      console.log(response);
      if (response === "add") {
        console.log("ola");
        // consertar o css
        if (elemento.id.startsWith("curtir")) {
            console.log("novo like");
            var texto = id_elemento.replace("curtir", "quant_likes");
            var element = document.getElementById(texto);
            element.innerText = `${Number(element.innerText)+1}`; 
            elemento.style.color = "red";
        } else if (elemento.classList.contains("bi-exclamation-triangle")) {
          elemento.classList.remove("bi-exclamation-triangle");
          elemento.classList.add("bi-exclamation-triangle-fill");
          elemento.style.color = "black";
        } else if (elemento.classList.contains("bi-trash")) {
          elemento.classList.remove("bi-trash");
          elemento.classList.add("bi-trash-fill");
          elemento.style.color = "black";
        }
        elemento.style.color = "red"; // Reapplies color if conditions above do not match
      } else {
        if (elemento.id.startsWith("curtir")) {
          var texto = id_elemento.replace("curtir", "quant_likes");
          var element = document.getElementById(texto);
          element.innerText = `${Number(element.innerText)-1}`;
        }
        
        elemento.style.color = "grey";
      }
    },
  });
}
