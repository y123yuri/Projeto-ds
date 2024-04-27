function handleSubmit() {

    console.log('opa');
    const name = document.querySelector('input[name=nome]').value;
    const email = document.querySelector('input[name=email]').value;
    const senha = document.querySelector('input[name=senha]').value;
    const senhaconfirm = document.querySelector('input[name=senhaconfirm]').value;


    fetch('https://api.sheetmonkey.io/form/w4f5wcsKYcNBHMjpxzR4Pw', {

        method:'post',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({name:name , email: email , senha:senha , confirmaSenha: senhaconfirm}),
    })
}