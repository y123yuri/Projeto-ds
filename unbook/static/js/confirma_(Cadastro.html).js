//CONSTANTES
const box = document.getElementById('form');
const campos = document.querySelectorAll('.required');
const spans = document.querySelectorAll('.spans_required');
const emailRegex = /^\d{9}@aluno\.unb\.br$/;

//VARIAVEIS
var etapaNome = false;
var etapaEmail = false;
var etapaSenha = false;
var etapaConfirmaSenha = false;

//ACIONAR OS SPAMS
function setError(index) {
    campos[index].style.border = '2px solid #e63636';
    spans[index].style.display = 'block';
}

//DESATIVAR OS SPANS
function removeError(index) {
    campos[index].style.border = '2px solid transparent';
    spans[index].style.display = 'none';
}

//VERIFICAR TODOS OS CAMPOS E DEPOIS ENVIAR OS DADOS - FUNÇÃO PRINCIPAL

function verifica() {
    console.log('cheguei')
    nomeValidade();
    emailValidade();
    senhaValidade();
    confirmasenhaValidade();
}

//VERIFICAR NOME (TALVEZ COM ERRO - ANALISAR)
function nomeValidade() {
    if (campos[0].value.length < 3) {
        console.log('O NOME TA PEQUENO');
        setError(0);
    }
    else if (campos[0].value.length > 3) {
        console.log('VALIDADO O NOME');
        removeError(0);
        etapaNome = true;
    }
}

//VERIFICAR EMAIL
function emailValidade() {
    if (emailRegex.test(campos[1].value)) {

        console.log('VALIDADO O EMAIL');
        removeError(1);
        etapaEmail = true;
    }
    else {

        console.log('EMAIL NÃO VALIDO');
        setError(1);
    }
}

//VERIFICAR SENHA
function senhaValidade() {
    if (campos[2].value.length < 2) {
        console.log('SENHA FRACA');
        setError(2);
    }
    else {
        console.log('VALIDADO A SENHA');
        removeError(2);
        etapaSenha = true;
    }
}

//VERIFICAR SE A SENHA É A MESMA DA DE CIMA
function confirmasenhaValidade() {
    if (campos[2].value == campos[3].value && campos[3].value.length >= 2) {
        console.log('A SENHA É A MESMA');
        removeError(3);
        etapaConfirmaSenha = true;
    }
    else {
        console.log('SENHA TA DIFERENTE');
        setError(3);
    }
}

//FUNÇÃO PARA PASSAR O NOME DO USUÁRIO PARA PROXIMA PÁGINA (CADASTRO_SUCESSO)
function reproduzirNome() {

    var pegaNome = document.getElementById('CampoNome').value;
    localStorage.setItem("StorageNome", pegaNome);

}

if (etapaNome && etapaEmail && etapaSenha && etapaConfirmaSenha) {

    console.log('Todos os campos verificados');
    loading();
}

//FUNÇÃO DE CARREGAMENTO PARA ENVIO DOS DADOS
function loading() {
    const progress = document.querySelector('.progress');

    let count = 1;
    let x = 16;

    const loading = setInterval(animate, 60);

    function animate() {
        if (count === 100 && x === 400) {
            clearInterval(loading);
            window.location.href = "/login"
        } else {
            x += 4;
            count++;

            progress.style.display = 'block';
            progress.style.width = `${x}px`;
            progress.style.window = '${count}%';
        }
    }
}