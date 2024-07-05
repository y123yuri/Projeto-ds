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
                setTimeout(() => { elemento.innerHTML += letra; }, 35 * i)
            });
        }

    });
});

function fechar() {
    document.getElementById('azulzao').style.display = "none"
    document.getElementById('tutorial').style.display = "flex"
}

var videos = document.querySelectorAll('.video-container video');
        var titulo = document.getElementById('titulo');
        var titulos = [
            "Página inicial",
            "Login e cadastro",
            "Perfil",
            "Pesquisar por professor",
            "Página professor",
            "Pesquisar por matéria",
            "Depositar ou acessar arquivos",
            "Avaliações",
            "Calendário",
            "Comentar",
            "Denunciar comentário"
        ];

        function proximo_video() {
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
            titulo.textContent = titulos[nextVideoIndex];
        }

        function video_anterior() {
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

            // Exibe o vídeo anterior ou o último se já estiver no primeiro
            var prevVideoIndex = (currentVideoIndex - 1 + videos.length) % videos.length;
            videos[prevVideoIndex].style.display = 'block';

            // Atualiza o título conforme o vídeo exibido
            titulo.textContent = titulos[prevVideoIndex];
        }