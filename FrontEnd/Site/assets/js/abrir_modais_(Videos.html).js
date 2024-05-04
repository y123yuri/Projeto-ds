var fundo_blur = document.getElementById('fundo_blur');
var modal = document.getElementById('modal_upload');

function abrir_modal () {

    fundo_blur.style.display = 'block';

    modal.classList.add('abrir');
    modal.style.display = 'block'

}

function enviar() {
    var link_enviado = document.getElementById('poe_links').value;
    var nome_link = document.getElementById('queLinkéEsse').value;

if (link_enviado !== '' && nome_link !== '') {
    var scroll = document.getElementById('scroll')
    
    var nome = document.createElement('h2')
    nome.className = 'nomeURL'
    nome.innerText = (nome_link + ': ');
    
    var link = document.createElement('a')
    link.innerText = link_enviado;
    
    link.className = 'links';
    link.href =  link_enviado;
    link.target = '_blank';

    var pula_linha = document.createElement('hr')
    
    scroll.appendChild(nome);
    scroll.appendChild(link);
    scroll.appendChild(pula_linha);
    
    link_enviado.value = '';
    nome.value = '';
    
    fechar_modal();
} else {
    alert('Tem que ter um link ai dentro man')
}
    
}

document.addEventListener('click', function(e) {
    if(e.target === fundo_blur) {
        fundo_blur.style.display = 'none';
        modal.style.display = 'none';
    } 
})

function fechar_modal() {
    fundo_blur.style.display = 'none';
        modal.style.display = 'none';
}