function register() {
	// pegar username e password
	let username = document.getElementById("new_username").value;
	let password = document.getElementById("new_password").value;

	if (isEmpty(username) || isEmpty(password)) {
		alert("Username and password cannot be empty.");
		return;
	}

	console.log(username, password);

	// isto envia os dados para app.py que vai registar
	// os dados se válidos na base de dados, senao retorna False
	$.get(
		"/register",
		{ user: username, passw: password },
		function (response) {
			registerConfirm(response);
		},
		"json" // data type
	);

	// Limpar campos de registo
	document.getElementById("new_username").value = "";
	document.getElementById("new_password").value = "";
}

function registerConfirm(response) {
	clearMessages(); // limpar conteudo anterior
	const div = document.getElementById("message");
	let message = document.createElement("p");

	console.log(response);

	// avisa ao utilizador se o registo foi sucedido ou nao
	message.textContent = response.message;
	div.appendChild(message);
}

function login() {
	// pegar username e password
	let username = document.getElementById("username").value;
	let password = document.getElementById("password").value;

	if (isEmpty(username) || isEmpty(password)) {
		alert("Username and password cannot be empty.");
		return;
	}

	// isto envia os dados para app.py que vai verificar se os dados inseridos
	// estao de acordo com os dados da base de dados e retornar True ou False
	$.get(
		"/login",
		{ user: username, passw: password },
		function (response) {
			loginConfirm(response);
		},
		"json"
	);

	// Limpar campos de registo
	document.getElementById("username").value = "";
	document.getElementById("password").value = "";
}

function loginConfirm(response) {
	clearMessages(); // limpar conteudo anterior
	const div = document.getElementById("message");
	let message = document.createElement("p");

	console.log("Login response:", response);

	// caso retorne true, redireciona-te para a pagina principal
	if (response.status == "ok") {
		window.location.href = "/intro"; // redireciona o navegador
	} else {
		message.textContent = response.message;
		div.appendChild(message);
	}
}

function clearMessages() {
	const div = document.getElementById("message");
	div.innerHTML = ""; // limpa mensagens anteriores
}

function isEmpty(str) {
	return !str || str.trim() === "";
}
