
var perguntas = document.getElementById('perguntas');
var Professor = document.getElementById('janela_professor');
var pesquisa = document.getElementById('perguntas');

var Materia = document.getElementById('janela_materia');
var Materia2 = document.getElementById('janela_materia2');
var SearchBar = document.getElementById('searchbar');

function abrirModal_Professor() {
    
    perguntas.style.display = 'none';
    Professor.classList.add('abrir');    

}

function abrirModal_Materia() {
    
    perguntas.style.display = 'none';
    Materia.classList.add('abrir');     

}

function abrirModal_Materia2(){
    
    Materia2.classList.add('abrir'); 
    Materia.classList.remove('abrir');
    console.log('opa') 
    
}

document.addEventListener('click', e => {
    if (!e.target.classList.contains('barra_pesquisa') && !e.target.classList.contains('botoes') && !e.target.classList.contains('CampoProcura') && !e.target.closest('.CampoProcura ul') && !e.target.closest('.janela_materia2') ) {
        fecharModal();
    }
});

function fecharModal() {
    perguntas.style.display = 'block';
    Materia.classList.remove('abrir');
    Professor.classList.remove('abrir');
    Materia2.classList.remove('abrir');

    SearchBar.value = '';
}

//abrir proxima janela

function reproduzirMateria(materias) {

    var reproduzir = materias.textContent

    document.getElementById('CampoFalado2').textContent = reproduzir;
}