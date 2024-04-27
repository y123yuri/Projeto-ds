
document.addEventListener("DOMContentLoaded",function() {

    var reproduzirEmail = localStorage.getItem("e-mail");


    document.getElementById("emailRecebido").innerText = reproduzirEmail;

});

function apagaEmail () {
    document.getElementById("emailRecebido").value = ' ';
}