document.addEventListener("DOMContentLoaded",function() {

    var reproduzirNome = localStorage.getItem("StorageNome");

    document.getElementById("NomeRecebido").innerText = reproduzirNome;

});
