
const texto = document.getElementById('primeiro')
Digitar(texto)

function Digitar(elemento) {
const textoArray = elemento.innerHTML.split('');
elemento.innerHTML = '';
textoArray.forEach((letra, i) => {
    setTimeout(() => {elemento.innerHTML += letra;} , 25 * i)
});
}

var pElements = document.querySelectorAll('p');
// Índice do <h2> atual
var currentIndex = 0;
var button = document.getElementById('prox')


function proximo() {
    // Esconde o <h2> atual
    pElements[currentIndex].style.display = 'none';
    
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
    Digitar(pElements[currentIndex])
    pElements[currentIndex].style.display = 'block';
}

