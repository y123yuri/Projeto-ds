//FUNÇÃO DA AVALIAÇÃO DAS ESTRELAS (EM PROGRESSO - NÃO MEXER AH NÃO SER QUE VC SAIBA OQ ESTÁ FZND)

let star = document.querySelectorAll('input');
let showValue = document.querySelector('#notas');

for (let i = 0; i < star.length; i++) {
	star[i].addEventListener('click', function() {
		i = this.value;

		showValue.innerHTML = i + " de 5";
	});
}