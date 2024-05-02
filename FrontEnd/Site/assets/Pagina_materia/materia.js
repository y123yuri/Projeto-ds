document.addEventListener("DOMContentLoaded", function () {

    var reproduzirMateria = localStorage.getItem("materia");


    document.getElementById("Materia").innerText = reproduzirMateria;

});

var biblioteca = document.getElementById('modal_da_biblioteca')

function abrir_modal_biblioteca() {
    var sla = window.getComputedStyle(biblioteca);
    const display = sla.getPropertyValue('display');

    if (display === 'none') {
        biblioteca.style.display = 'block';
        biblioteca.classList.add('abrir');
    }
    else if (display === 'block') {
        biblioteca.style.display = 'none';
    }
}