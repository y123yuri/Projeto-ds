const dropArea = document.getElementById("label_file");
const input = document.getElementById("input_file");
const imgView = document.getElementById("imgView");

input.addEventListener("change", Upload_image);

function Upload_image() {
  input.files[0];
  let imgLink = URL.createObjectURL(input.files[0]);
  imgView.style.backgroundImage = `url(${imgLink})`;
  imgView.textContent = "";
}

dropArea.addEventListener("dragover", function (e) {
  e.preventDefault();
});

dropArea.addEventListener("drop", function (e) {
  e.preventDefault();
  input.files = e.dataTransfer.files;
  Upload_image();
});
