document.addEventListener("DOMContentLoaded", function () {
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

        // Exibir o azulzao
        document.getElementById('azulzao').style.display = "flex";
        
        // Ocultar o blur após 2 segundos
        setTimeout(() => {
            document.getElementById('blur').style.display = "none";

        }, 2000);
    });
});
