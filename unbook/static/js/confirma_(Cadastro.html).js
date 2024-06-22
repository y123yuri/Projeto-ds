//CONSTANTES
const box = document.getElementById('form');
const campos = document.querySelectorAll('.required');
const spans = document.querySelectorAll('.spans_required');
const emailRegex = /^\d{9}@aluno\.unb\.br$/;

//VARIAVEIS

var etapaNomeCompleto = false;
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

document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form'); // Selecionar o formulário

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevenir o envio padrão do formulário
        verifica();
    });
});

function verifica() {
    console.log('cheguei');
    nomeConfirmaValidade();
    nomeValidade();
    emailValidade();
    senhaValidade();
    confirmasenhaValidade();

    if (etapaNomeCompleto && etapaNome && etapaEmail && etapaSenha && etapaConfirmaSenha) {
        console.log('aaaaaaaa' + etapaConfirmaSenha)
        console.log('Todos os campos verificados');
        // enviarFormulario();
    }
}



function enviarFormulario() {
    const formData = new FormData(document.querySelector('form'));

    fetch('sucesso/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value // Inclua o CSRF token
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = "sucesso/";
        } else {
            console.log('Erro:', data.error);
        }
    })
    .catch(error => console.error('Erro:', error));
}

// As funções de validação e as funções auxiliares (nomeValidade, emailValidade, etc.) permanecem as mesmas


//VERIFICAR NOME (TALVEZ COM ERRO - ANALISAR)
function nomeConfirmaValidade() {
    if (campos[0].value.length < 3) { 
        console.log('O NOME TA PEQUENO');
        setError(0);
    }
    else if (campos[0].value.length >= 3) {
        console.log('VALIDADO O NOME');
        removeError(0);
        etapaNomeCompleto = true;
    }
}

function nomeValidade() {
    if (campos[1].value.length < 3 || campos[1].value.length > 12 || campos[1].value.includes(' ') || campos[1].value.includes('.')) {
        
        console.log('O NOME NÃO ESTÁ DENTRO DAS DIRETRIZES');
        setError(1);
    }
    else if (campos[1].value.length > 3 && campos[1].value.length <= 12) {
        console.log('VALIDADO O NOME');
        removeError(1);
        etapaNome = true;
    }
}

//VERIFICAR EMAIL
function emailValidade() {
    if (emailRegex.test(campos[2].value)) {

        console.log('VALIDADO O EMAIL');
        removeError(2);
        etapaEmail = true;
    }
    else {

        console.log('EMAIL NÃO VALIDO');
        setError(2);
    }
}

//VERIFICAR SENHA
function senhaValidade() {
    if (campos[3].value.length < 2) {
        console.log('SENHA FRACA');
        setError(3);
    }
    else {
        console.log('VALIDADO A SENHA');
        removeError(3);
        etapaSenha = true;
    }
}

//VERIFICAR SE A SENHA É A MESMA DA DE CIMA
function confirmasenhaValidade() {
    if (campos[3].value == campos[4].value && campos[4].value.length >= 2) {
        console.log('A SENHA É A MESMA');
        removeError(4);
        etapaConfirmaSenha = true;
    }
    else {
        console.log('SENHA TA DIFERENTE');
        setError(4);
    }
}

//FUNÇÃO PARA PASSAR O NOME DO USUÁRIO PARA PROXIMA PÁGINA (CADASTRO_SUCESSO)
function reproduzirNome() {

    var pegaNome = document.getElementById('CampoNome').value;
    localStorage.setItem("StorageNome", pegaNome);

}

function abrir_termos(){
    var blur = document.getElementById('fundo_blur')
    blur.style.display = "flex"

    var termos = document.getElementById('ler_termos')
    termos.style.display = "flex"

    blur.addEventListener('click',(e)=> {
    if(e.target.contains(blur)){
        e.preventDefault()
        blur.style.display = "none"
        termos.style.display = "none"
    }
    })

    document.querySelector('#ler_termos button').addEventListener('click', (e)=> {
        blur.style.display = "none"
        termos.style.display = "none"
    })
}

function toggleSubmit() {
    var check = document.getElementById('check_termos');
    var submit = document.getElementById('submit');
    if (check.checked) {
        submit.disabled = false;
        submit.style.backgroundColor = "#0b4c9c"; // azul
    } else {
        submit.disabled = true;
        submit.style.backgroundColor = "#000000cc"; // cinzinha
    }
}

window.onload = function() {
    var check = document.getElementById('check_termos');
    check.addEventListener('change', toggleSubmit);
    toggleSubmit();
}