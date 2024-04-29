
const box = document.getElementById('form');
const campos = document.querySelectorAll('.required');
const spans = document.querySelectorAll('.spans_required');
const emailRegex = /^\d{9}@aluno\.unb\.br$/;

var etapaNome = false;
var etapaEmail = false;
var etapaSenha = false;
var etapaConfirmaSenha = false;


function setError(index) {
    campos[index].style.border = '2px solid #e63636';
    spans[index].style.display = 'block';
}

function removeError(index) {
    campos[index].style.border = '';
    spans[index].style.display = 'none';
}

function verifica() {
    nomeValidade();
    emailValidade();
    senhaValidade();
    confirmasenhaValidade();
    Enviar();
}

function nomeValidade() {
    if (campos[0].value.length < 3) {
        console.log('O NOME TA PEQUENO');
        setError(0);
    }
    else {
        console.log('VALIDADO O NOME');
        removeError(1);
        etapaNome = true;
    }
}

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

function Enviar() {
    if (etapaNome && etapaEmail && etapaSenha && etapaConfirmaSenha) {

        console.log('chegou');
        const scriptURL = 'https://script.google.com/macros/s/AKfycbwXmMZ03YT3wQ4JZyLwjYIpg3sJPeARd1fepIhEOov3Kazg1QB-LIS1MJxXlv0slk7T/exec';
        const form = document.forms['contact-form'];

        fetch(scriptURL, { method: 'POST', body: new FormData(form) })
            .then(response => response.json())
            .then(data => {
                if (data.result === 'success') {
                    alert("Seu perfil foi cadastrado com sucesso!");
                    window.location.href = './cadastro_sucesso.html';
                } else {
                    throw new Error('Erro no envio dos dados!');
                }
            })
            .catch(error => console.error('Error!', error.message));
        reproduzirNome();
        goPost(form);
    }
}

function reproduzirNome() {

    var pegaNome = document.getElementById('CampoNome').value;
    localStorage.setItem("StorageNome", pegaNome);

}