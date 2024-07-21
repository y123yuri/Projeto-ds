//CONSTANTES
const box = document.getElementById('box');
const campos = document.querySelectorAll('.required');
const spans = document.querySelectorAll('.spans_required');
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

//VERIFICAR TODOS OS CAMPOS E DEPOIS ENVIAR OS DADOS - FUNÇÃO PRINCIPAL
function verifica() {
    emailValidade();
    senhaValidade();
    refresh();
}
 
//DAR F5 NA PAGINA DEPOIS DE VERIFICAR
function refresh() {
    window.location.reload();
}

//VERIFICAR SENHA
function senhaValidade() {
    if (campos[1].value.length < 3) {
        console.log('SENHA INVALIDADA');
        setError(1);
    }
    else {
        console.log('VALIDADO A SENHA');
        removeError(1);
        goBackUnBook(1);
        contador++;
    }
}

//VERIFICAR EMAIL
function emailValidade() {
    if (emailRegex.test(campos[0].value)) {

        console.log('VALIDADO O EMAIL');
        removeError(0);
        goBackUnBook(0);
        contador++;
    }
    else {

        console.log('EMAIL INVALIDADO');
        setError(0);
    }
}


//FUNÇÃO IR PARA A PRÓXIMA PÁGINA , NO CASO A UNBOOK (PRINCIPAL)
function goBackUnBook(index) {

    console.log(contador);

    if (contador == 2) {
        window.location.href = "";
        contador = 0;
    }


}