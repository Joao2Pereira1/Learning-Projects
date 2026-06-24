let idimag;
let originalRelativePath;

function displayImage(id) {
	idimag = $("#idImg").val();
	console.log(idimag);

	// busca resposta do metodo list do cherrypy
	$.get(
		"/list",
		{ id: idimag },
		function (response) {
			originalImage(response);
		},
		"json" // data type
	);
}

function originalImage(response) {
	console.log(response);
	const org_img = document.getElementById("originalImg");

	// remove a imagem anterior
	org_img.innerHTML = "";

	// mostra imagem original
	const img = document.createElement("img");
	const absolute_path = response.images[0]["path"];
	const filename = absolute_path.split("/").pop();
	originalRelativePath = "../uploads/" + filename;

	img.src = originalRelativePath;
	img.width = 550;
	img.height = 450;
	org_img.appendChild(img);
}

function displayProcessedImage() {
	// path vai ser obtido quando a imagem é mostrada relative_path
	const procAlgorithm = document.getElementById("algorithm-select").value;
	console.log(originalRelativePath);
	console.log(procAlgorithm);

	// busca resposta do metodo list do cherrypy
	$.get(
		"/imageproc",
		{ path: originalRelativePath, algorithm: procAlgorithm },
		function (response) {
			processedImage(response);
		},
		"json" // data type
	);
}

function processedImage(response) {
	const proc_img = document.getElementById("processedImg");
	proc_img.innerHTML = "";

	const img = document.createElement("img");
	const relative_path = response.processed_path;

	img.src = relative_path;
	img.width = 550;
	img.height = 450;
	proc_img.appendChild(img);
}
