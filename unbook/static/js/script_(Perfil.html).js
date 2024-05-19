
window.onload = () => {
    var editar_perfil = document.getElementById('edit_profile')
    editar_perfil.style.backgroundColor = '#0B4C9C';
    editar_perfil.style.color = 'whitesmoke';
}


function abrir_modal(id) {

    var others = document.querySelectorAll('.pages')
    others.forEach(element => {

        element.style.backgroundColor = '#f5f5f5';
        element.style.color = 'black';
    })

    var element = document.getElementById(id)
    element.style.backgroundColor = '#0B4C9C';
    element.style.color = 'whitesmoke';
    element.style.transition = "all ease 0.1s"

var others_boxes = document.querySelectorAll('.boxs')

    if(id === 'edit_profile'){
        others_boxes.forEach(element => {
            element.style.display = "none";
        })

      var Profile = document.getElementById('Profile')
      Profile.style.display = "flex";


    }

    else if(id === 'edit_senha'){
        
        others_boxes.forEach(element => {
            element.style.display = "none";
        })

      var Senha = document.getElementById('Senha')
      Senha.style.display = "flex";
    }



    else if(id === 'edit_foto'){
      
    }

}

document.addEventListener('click', (e) => {
    if (!e.target.closest('#boxes')) {
        console.log('eita')
        window.location.href = '/'
    }



})


var img = document.getElementById('img_user')
img.addEventListener('mouseover', (e) => {
    img.style.opacity = "0.5"
})

img.addEventListener('mouseout', (e) => {
    img.style.opacity = "1"
})









