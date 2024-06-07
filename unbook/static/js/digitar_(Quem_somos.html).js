
const texto = document.getElementById('primeiro')
Digitar(texto)

function Digitar(elemento) {
const textoArray = elemento.innerHTML.split('');
elemento.innerHTML = '';
textoArray.forEach((letra, i) => {
    setTimeout(() => {elemento.innerHTML += letra;} , 60 * i)
});
}

var h2Elements = document.querySelectorAll('h2');
// Índice do <h2> atual
var currentIndex = 0;
var button = document.getElementById('button_prox')


function proximo() {
    // Esconde o <h2> atual
    h2Elements[currentIndex].style.display = 'none';
    
    // Incrementa o índice para o próximo <h2>
    currentIndex++;
    var indice = document.getElementById('contador')
    indice.textContent = currentIndex + ' de 7'

    if (currentIndex === 7){
        button.textContent = 'Voltar';
        button.addEventListener('click', () => {
            window.location.href = "../"
            currentIndex = 0;
        })
        
    }
    
    // Mostra o próximo <h2>
    Digitar(h2Elements[currentIndex])
    h2Elements[currentIndex].style.display = 'block';
}

document.getElementById('titlao').addEventListener('click', ()=> {
    window.scrollBy({top: 750, behavior: 'smooth' })
})