let id;

$(document).ready(function () {
	const params = new URLSearchParams(window.location.search);
	id = params.get("id");
	imageComments();
});

function imageComments() {
	$.get("/comments", { idimg: id }, function (response) {
		showImageAndInfo(response);
	});
}

function showImageAndInfo(response) {
	const l_div = document.getElementById("imageinfo");
	const r_div = document.getElementById("comments");
	const upvotes = document.getElementById("thumbs_up");
	const downvotes = document.getElementById("thumbs_down");

	// limpa o conteudo anterior dos elementos
	l_div.innerHTML = "";
	r_div.innerHTML = "";
	upvotes.innerHTML = "";
	downvotes.innerHTML = "";

	console.log(response);

	// cria a imagem
	const img = document.createElement("img");
	const absolute_path = response.image["path"];
	const filename = absolute_path.split("/").pop();
	const relative_path = "../uploads/" + filename;
	img.src = relative_path;
	img.width = 550;
	img.height = 450;
	l_div.appendChild(img);

	// cria e exibe o parágrafo com nome, autor e data
	const infoParagraph = document.createElement("p");
	infoParagraph.innerText =
		"Nome: " +
		response.image.name +
		" | Autor: " +
		response.image.author +
		" | Data: " +
		response.image.datetime;
	l_div.appendChild(infoParagraph);

	// exibe os comentários, se houver, ou mostra mensagem alternativa
	const commentsParagraph = document.createElement("p");
	commentsParagraph.innerText = response.comments || "Sem comentários.";
	r_div.appendChild(commentsParagraph);

	// mostra o número de votos positivos
	const upVotesParagraph = document.createElement("p");
	upVotesParagraph.innerText = "Up Votes: " + response.votes.thumbs_up;
	upvotes.appendChild(upVotesParagraph);

	// mostra o número de votos negativos
	const downVotesParagraph = document.createElement("p");
	downVotesParagraph.innerText = "Down Votes: " + response.votes.thumbs_down;
	downvotes.appendChild(downVotesParagraph);
}

function newComment() {
	// Obtém o nome de utilizador e o texto do comentário inserido
	let user = document.getElementById("user").value;
	let comment = document.getElementById("comment").value;

	console.log(user, comment, id); // Debug

	// Verifica se os campos estão preenchidos
	if (user == "" || comment == "") alert("Missing comment and/or username!");
	else {
		// Envia os dados via POST para o servidor app.py, que irá armazenar na database
		$.post(
			"/newcomment",
			{ idimag: id, username: user, newcomment: comment },
			function () {
				// Atualiza os comentários após envio bem-sucedido
				imageComments();
			}
		);
	}

	// limpar conteudo anterior
	document.getElementById("user").value = "";
	document.getElementById("comment").value = "";
}

function upVote() {
	$.post("/upvote", { idimag: id }, function (response) {
		document.getElementById("thumbs_up").innerText = response.ups;
		document.getElementById("thumbs_down").innerText = response.downs;
	});
}

function downVote() {
	$.post("/downvote", { idimag: id }, function (response) {
		document.getElementById("thumbs_up").innerText = response.ups;
		document.getElementById("thumbs_down").innerText = response.downs;
	});
}
