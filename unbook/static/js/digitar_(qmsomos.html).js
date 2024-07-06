
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

document.addEventListener("DOMContentLoaded", function() {
    const scrollContainer = document.querySelector('.scroll');
    const nextButton = document.getElementById('next');
    const backButton = document.getElementById('back');
    const equipe = document.querySelector('.equipe')

    if(window.matchMedia("(max-width:767px)").matches) {
        nextButton.addEventListener('click', () => {
            scrollContainer.scrollBy({ left: 325, behavior: 'smooth' });
        });
    
        backButton.addEventListener('click', () => {
            scrollContainer.scrollBy({ left: -325, behavior: 'smooth' });
        });
    
        scrollContainer.addEventListener('scroll', () => {
            const scrollLeft = scrollContainer.scrollLeft;
    
            if (scrollLeft === 0) {
                equipe.textContent = 'Líderes';
            } else if (scrollLeft >= 325 && scrollLeft < 350) {
                equipe.textContent = 'Front-End';
            } else if (scrollLeft >= 360) {
                equipe.textContent = 'Back-End';
            }
        });
    } else {

        nextButton.addEventListener('click', () => {
            scrollContainer.scrollBy({ left: 930, behavior: 'smooth' });
        });
    
        backButton.addEventListener('click', () => {
            scrollContainer.scrollBy({ left: -930, behavior: 'smooth' });
        });
    
        scrollContainer.addEventListener('scroll', () => {
            const scrollLeft = scrollContainer.scrollLeft;
    
            if (scrollLeft === 0) {
                equipe.textContent = 'Líderes';
            } else if (scrollLeft >= 930 && scrollLeft < 1780) {
                equipe.textContent = 'Front-End';
            } else if (scrollLeft >= 1850) {
                equipe.textContent = 'Back-End';
            }
        });
    }

});
