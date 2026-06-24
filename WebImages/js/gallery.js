// quando o documento/pagina esta toda carregada, mostrar todas as imagens
$(document).ready(function () {
	imagesList("all");
});

function imagesList(id) {
	let idimag;
	if (id == "all") {
		idimag = "all";
	} else {
		idimag = $("#authorImg").val();
		if (idimag == "") {
			idimag = "all";
		}
	}
	// busca resposta do metodo list do cherrypy e mostra as imagens
	$.get(
		"/list",
		{ id: idimag },
		function (response) {
			showImages(response);
		},
		"json" // data type
	);
}

//! tambem podes usar JQuery: Ex ->  let paragraph = $("<p>").text("Image Information:" + image);
function showImages(response) {
	// response.images é uma lista de dicionários com informacao das imagens, row[3] tem o image path
	$("#showimages").html("");

	for (let i = 0; i < response.images.length; i++) {
		const div = document.getElementById("showimages");

		// html code para mostrar imagem e ao clicar na imagem, mostrar os seus comentarios
		const img = document.createElement("img");

		// obter relative path
		const absolute_path = response.images[i]["path"];
		const filename = absolute_path.split("/").pop();
		const relative_path = "../uploads/" + filename;
		img.src = relative_path;
		img.width = 550;
		img.height = 450;

		// obter id e show image comments
		const imageId = response.images[i]["id"];
		img.onclick = function () {
			showImageComments(imageId);
		};

		div.appendChild(img);

		// html code para mostrar informacao da imagem
		const paragraph = document.createElement("p");
		const name = response.images[i]["name"];
		const author = response.images[i]["author"];
		const datetime = response.images[i]["datetime"];
		paragraph.innerText =
			"Nome: " + name + " | Autor: " + author + " | Data: " + datetime;
		div.appendChild(paragraph);
	}
}

function showImageComments(id) {
	window.open("../html/image.html?id=" + id, "_blank");
}
