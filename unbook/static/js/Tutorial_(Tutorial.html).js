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
    
            }, 10000)
            
        }, 2000);

        
        function Digitar(elemento) {
            const textoArray = elemento.innerHTML.split('');
            elemento.innerHTML = '';
            textoArray.forEach((letra, i) => {
                setTimeout(() => { elemento.innerHTML += letra; }, 60 * i)
            });
        }

    });
});

function fechar() {
    document.getElementById('azulzao').style.display = "none"
    document.getElementById('tutorial').style.display = "block"



}
