//FUNÇÃO PARA RECEBER O NOME DA PÁGINA ANTERIOR (CADASTRO)
document.addEventListener("DOMContentLoaded",function() {

    var reproduzirNome = localStorage.getItem("StorageNome");

    document.getElementById("NomeRecebido").innerText = reproduzirNome;

});
