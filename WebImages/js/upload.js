// Image UpLoad Javascript
let file;

function updatePhoto(event) {
	let reader = new FileReader();
	reader.onload = function (event) {
		//Create an imagem
		let img = new Image();
		img.onload = function () {
			//Put image on screen
			const canvas = $("#photo")[0];
			const ctx = canvas.getContext("2d");
			ctx.drawImage(img, 0, 0, img.width, img.height, 0, 0, 550, 450);
		};
		img.src = event.target.result;
	};

	file = event.target.files[0];
	//Obtain the file
	reader.readAsDataURL(file);
}

function uploadImage() {
	if (file != null) {
		sendFile(file);
		//Release the resources allocated to the selected image
		window.URL.revokeObjectURL(picURL);
	} else alert("Missing image!");
}

function sendFile(file) {
	let data = new FormData();
	data.append("myFile", file);

	// ! podes usar jQuery ou podes usar document.getElementById()

	//Obtain nameImg and authorImg and fill the form
	let name = $("#nameImg").val();
	let author = $("#authorImg").val();

	if (name == "" || author == "") alert("Missing name and/or author!");
	else {
		// Adiciona os campos ao FormData
		data.append("nameImg", name);
		data.append("authorImg", author);

		/* faz uma requisição POST para /upload, o que, na tua aplicação CherryPy, chama o método upload(...) da classe Root, que:
		-Lê e salva o ficheiro;
		-Gera o nome usando hash SHA-256;
		-Guarda o caminho no banco de dados, com nome, autor e data/hora. */
		//! diferente de acessar pagina upload, porque quando clicas no menu para acessar upload, apenas retorna upload.html
		let xhr = new XMLHttpRequest();
		xhr.open("POST", "/upload");

		xhr.upload.addEventListener("progress", updateProgress(this), false);
		xhr.send(data);
	}
}

function updateProgress(evt) {
	if (evt.loaded == evt.total) alert("Okay");
}
