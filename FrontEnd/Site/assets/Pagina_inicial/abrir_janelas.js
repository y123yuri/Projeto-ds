function abrirModal(id) {
    var modal = document.getElementById(id);
    modal.style.display = "block";
}

// Função para fechar o modal com o ID específico
function fecharModal(id) {
    var modal = document.getElementById(id);
    modal.style.display = "none";
}

// Event listener para fechar o modal clicando fora dele
window.onclick = function(event) {
    var modais = document.getElementsByClassName('janela_pesquisa');
    for (var i = 0; i < modais.length; i++) {
        var modal = modais[i];
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
}

// Event listener para abrir os modais ao clicar nos botões
document.getElementById('professor').onclick = function() {
    abrirModal('janela_professor');
};
document.getElementById('materia').onclick = function() {
    abrirModal('janela_materia');
};