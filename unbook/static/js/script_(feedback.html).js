function enviar_feedback(){
    const titulo = document.getElementById("titulo").value
    const corpo = document.getElementById("corpo").value
    $.ajax({
        type: "POST",
        url: "../enviar_feedback",
        data: {
            csrfmiddlewaretoken: csrf_token,
            titulo: titulo,
            corpo: corpo
        },
        success: function (response) {
            console.log(response);
            alert("Feedback enviado com sucesso! Muito obrigado!.")
        }
    })
}