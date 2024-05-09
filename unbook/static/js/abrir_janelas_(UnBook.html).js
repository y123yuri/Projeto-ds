
// VARIAVEIS
var perguntas = document.getElementById('perguntas');
var Professor = document.getElementById('janela_professor');
var pesquisa = document.getElementById('perguntas');
var Materia = document.getElementById('janela_materia');
var Materia2 = document.getElementById('janela_materia2');
var SearchBar = document.getElementById('searchbar');

//FUNÇÕES PARA ABRIR MODAIS
function abrirModal_Professor() {
    
    perguntas.style.display = 'none';
    Professor.classList.add('abrir');    

}

function abrirModal_Materia() {
    
    perguntas.style.display = 'none';
    Materia.classList.add('abrir');     

}

//FUNÇÕES PARA ABRIR SEGUNDOS MODAIS 
function abrirModal_Materia2(){
    
    Materia2.classList.add('abrir'); 
    Materia.classList.remove('abrir');
    console.log('opa') 
    
}

//FUNÇÃO PARA FECHAR CASO CLIQUE FORA DO MODAL
document.addEventListener('click', e => {
    if (!e.target.classList.contains('barra_pesquisa') && !e.target.classList.contains('botoes') && !e.target.classList.contains('CampoProcura') && !e.target.closest('.CampoProcura ul') && !e.target.closest('.janela_materia2') ) {
        fecharModal();
    }
});

//FUNÇÃO PARA FECHAR MODAIS
function fecharModal() {
    //perguntas.style.display = 'block';
    //Materia.classList.remove('abrir');
    //Professor.classList.remove('abrir');
    //Materia2.classList.remove('abrir');
//
    //SearchBar.value = '';
}

//ABRIR NO PROXIMO MODAL OS DADOS DO ANTIGO 

//PASSAR MATERIA PARA SEGUNDO MODAL
function reproduzirMateria(materias) {

    var reproduzir_materia = materias.textContent;
    document.getElementById('CampoFalado2').textContent = reproduzir_materia;

//PASSAR MATERIA PARA PÁGINA Materia.html
    var materia = reproduzir_materia;
    localStorage.setItem("materia",materia)
}

//PASSAR PROFESSOR PARA PÁGINA Materia.html
function reproduzirProfessor(element, num) {

    var professor_pega = document.getElementById('professor_' + num).textContent;
    localStorage.setItem("professor", professor_pega)
}