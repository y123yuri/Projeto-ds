
    const box = document.getElementById('box');
    const campos = document.querySelectorAll('.required');
    const spans = document.querySelectorAll('.spans_required');
    const emailRegex = /^\S+@\S+\.\S+$/;
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
    senhaValidade();
}

function senhaValidade(){
    if (campos[1].value.length < 8) {
        console.log('DEU ERRADO A SENHA');
        setError(1);
    }
    else {
        console.log('VALIDADO A SENHA');
        removeError(1);
        goBackUnBook(1);
        contador++;
    }
}

    function emailValidade() {
        if (emailRegex.test(campos[0].value)) {

            console.log('VALIDADO O EMAIL');
            removeError(0);
            goBackUnBook(0);
            contador++;
        }
        else {
           
            console.log('DEUERRADO O EMAIL');
            setError(0);
        }
    }

    function goBackUnBook (index) {
    
        console.log(contador);

        if (contador == 2) {
            window.location.href = "../pagina_inicial/UnBook.html";
            contador = 0;
        } 
        else {
            contador = 0;
            campos[index].value = '';
        }        

    }