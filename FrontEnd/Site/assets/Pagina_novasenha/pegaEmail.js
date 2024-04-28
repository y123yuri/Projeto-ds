
const box = document.getElementById('box');
const campos = document.querySelectorAll('.required');
const spans = document.querySelectorAll('.spanEmail');
const emailRegex = /^\d{9}@aluno\.unb\.br$/;
let contador = 1;

function setError(index) {
    campos[index].style.border = '2px solid #e63636';
    spans[index].style.display = 'block';
}

function removeError(index) {
    campos[index].style.border = '';
    spans[index].style.display = 'none';
}

function verifica() {
emailValidade();
}

function emailValidade() {
    if (emailRegex.test(campos[0].value)) {

        console.log('VALIDADO O EMAIL');
        removeError(0);
        reproduzirEmail(0);
        gotonextpage(0);
        contador++;
    }
    else {
       
        console.log('DEUERRADO O EMAIL');
        setError(0);
    }
}

function gotonextpage (index) {

    console.log(contador);

    if (contador == 2) {
        window.location.href = "nova_senha_confirma.html";
        contador = 0;
    } 
    
}
function reproduzirEmail() {

    var pegaEmail = document.getElementById('campoEscritaEmail').value;
    localStorage.setItem("e-mail",pegaEmail);

    window.location.href = "nova_senha_confirma.html";

}