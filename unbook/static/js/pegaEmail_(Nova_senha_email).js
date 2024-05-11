//CONSTANTES
const box = document.getElementById('box');
const campos = document.querySelectorAll('.required');
const spans = document.querySelectorAll('.spanEmail');
const emailRegex = /^\d{9}@aluno\.unb\.br$/;

//CONTADOR
let contador = 1;

//GERAR SPAMS
function setError(index) {
    campos[index].style.border = '2px solid #e63636';
    spans[index].style.display = 'block';
}

//REMOVER SPAMS
function removeError(index) {
    campos[index].style.border = '';
    spans[index].style.display = 'none';
}

//VERIFICA A FUNÇÃO EMAIL - FUNÇÃO PRINCIPAL
function verifica() {
emailValidade();
}

//VERIFICAR EMAIL
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

//FUNÇÃO IR PARA PROXIMA PÁGINA, NO CASO NOVA SENHA CONFIRMA (O EMAIL)
function gotonextpage (index) {

    console.log(contador);

    if (contador == 2) {
        window.location.href = "nova_senha_confirma.html";
        contador = 0;
    } 
    
}

//ENVIAR O EMAIL PARA A PRÓXIMA PÁGINA (NOVA SENHA CONFIRMA)
function reproduzirEmail() {

    var pegaEmail = document.getElementById('campoEscritaEmail').value;
    localStorage.setItem("e-mail",pegaEmail);

    window.location.href = "nova_senha_confirma.html";

}