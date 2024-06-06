document.addEventListener("DOMContentLoaded", function () {

    setInterval(() => {
        var help = document.getElementById('help')
        help.style.display = "block"
        help.style.animation = "pisca 1s infinite"
    }, 4000)

    document.getElementById('textbutton').addEventListener('click', function (e) {
        const azulzao = this.parentElement;
        const circulo = document.createElement('div');
        const diametro = Math.max(azulzao.clientWidth, azulzao.clientHeight);
        const raio = diametro / 2;

        circulo.style.backgroundColor = "#0C36A1";
        circulo.style.width = circulo.style.height = `${diametro}px`;
        circulo.style.left = `${e.clientX - azulzao.offsetLeft - raio}px`;
        circulo.style.top = `${e.clientY - azulzao.offsetTop - raio}px`;
        circulo.style.position = "absolute";
        circulo.style.borderRadius = "50%";
        circulo.style.transition = "transform 1s ease-out";
        circulo.style.transform = "scale(0)";
        circulo.style.zIndex = 2;
        circulo.classList.add('blusao');

        azulzao.appendChild(circulo);

        // Ocultar o blur após 2 segundos
        setTimeout(() => {
            document.getElementById('blur').style.display = "none";
            document.getElementById('azulzao').style.display = "block"
            const texto = document.getElementById('text_azul')
            Digitar(texto)

            setTimeout(()=> {
                const button = document.getElementById('button_prosseguir')
                button.style.animation = "surgir 0.3s ease"
                button.style.display = "block";
    
            }, 10000) //mudar dps para 10000
            
        }, 2000);

        
        function Digitar(elemento) {
            const textoArray = elemento.innerHTML.split('');
            elemento.innerHTML = '';
            textoArray.forEach((letra, i) => {
                setTimeout(() => { elemento.innerHTML += letra; }, 40 * i)
            });
        }

    });
});

function fechar() {
    document.getElementById('azulzao').style.display = "none"
    document.getElementById('tutorial').style.display = "flex"
}
function proximo_video() {
    var videos = document.querySelectorAll('.video-container video');
    var titulo = document.getElementById('titulo');

    // Encontra o vídeo atualmente exibido
    var currentVideoIndex;
    for (var i = 0; i < videos.length; i++) {
        if (videos[i].style.display !== 'none') {
            currentVideoIndex = i;
            break;
        }
    }

    // Oculta o vídeo atual
    videos[currentVideoIndex].style.display = 'none';

    // Exibe o próximo vídeo ou o primeiro se já estiver no último
    var nextVideoIndex = (currentVideoIndex + 1) % videos.length;
    videos[nextVideoIndex].style.display = 'block';

    // Atualiza o título conforme o vídeo exibido
    if (nextVideoIndex === 0) {
        titulo.textContent = "Página inicial";
    } else if (nextVideoIndex === 1) {
        titulo.textContent = "Login e cadastro";
    } else if (nextVideoIndex === 2) {
        titulo.textContent = "Pesquisar";
    } else if (nextVideoIndex === 3) {
        titulo.textContent = "Matéria e professor";
    } 
}