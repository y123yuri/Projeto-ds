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
    alert("Tem que ter um link ai dentro man");
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
        console.log("link repetido piranha");
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

// Lista de domínios permitidos

const dominiosPermitidos = [
  "https://www.youtube.com/",
  "https://docs.google.com",
  "https://drive.google.com",
  "https://teams.microsoft.com",
];

// Função para verificar se o link é permitido
function isLinkPermitido(link) {
  let url;

  try {
    url = new URL(link);
  } catch (error) {
    return false; // URL inválida
  }

  return dominiosPermitidos.some((dominio) => url.hostname.endsWith(dominio));
}

// Função para lidar com o envio do formulário
function handleFormSubmit(event) {
  event.preventDefault();

  const linkInput = document.getElementById("linkInput");
  const link = linkInput.value.trim();

  if (isLinkPermitido(link)) {
    adicionarLinkPermitido(link);
    linkInput.value = ""; // Limpar o campo de entrada após adicionar
  } else {
    alert("Link não permitido!");
  }
}

// Função para adicionar o link permitido à lista na página
function adicionarLinkPermitido(link) {
  const linksList = document.getElementById("linksList");
  const newLinkItem = document.createElement("li");
  const linkElement = document.createElement("a");
  linkElement.href = link;
  linkElement.textContent = link;
  newLinkItem.appendChild(linkElement);
  linksList.appendChild(newLinkItem);
}

// Adicionar evento de submit ao formulário
const linkForm = document.getElementById("linkForm");
linkForm.addEventListener("submit", handleFormSubmit);
