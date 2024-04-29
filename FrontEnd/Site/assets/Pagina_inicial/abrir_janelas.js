
var perguntas = document.getElementById('perguntas');
var Professor = document.getElementById('janela_professor');
var Materia = document.getElementById('janela_materia');
var pesquisa = document.getElementById('perguntas');

function abrirModal_Professor() {
    
    perguntas.style.display = 'none';
    Professor.classList.add('abrir');    

}

function abrirModal_Materia() {
    
    perguntas.style.display = 'none';
    Materia.classList.add('abrir');     

}

document.addEventListener('click', e => {
    if (!e.target.classList.contains('barra_pesquisa') && !e.target.classList.contains('botoes') && !e.target.classList.contains('CampoProcura') && !e.target.closest('.CampoProcura ul') ) {
        fecharModal();
    }
});

function fecharModal() {
    perguntas.style.display = 'block';
    Materia.classList.remove('abrir');
    Professor.classList.remove('abrir');
}