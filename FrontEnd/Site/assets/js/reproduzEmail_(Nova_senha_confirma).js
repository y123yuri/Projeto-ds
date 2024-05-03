//RECEBE O EMAIL DA PÁGINA ANTERIOR (NOVA SENHA EMAIL)
document.addEventListener("DOMContentLoaded",function() {

    var reproduzirEmail = localStorage.getItem("e-mail");


    document.getElementById("emailRecebido").innerText = reproduzirEmail;

});

//RESETA EMAIL (ANÁLISE)
function apagaEmail () {
    document.getElementById("emailRecebido").value = ' ';
}