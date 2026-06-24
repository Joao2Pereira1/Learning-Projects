Comunicação Web: Python, JavaScript e HTML

---

## Objetivo do Projeto

Este projeto é fundamental para compreender como diferentes tecnologias web comunicam entre si:

-   Python e JavaScript
-   JavaScript e HTML

A comunicação ocorre normalmente num sistema cliente-servidor, onde:

-   Python (CherryPy) atua como servidor
-   JavaScript atua como cliente (executado no navegador)

---

## Comunicação Python ↔ JavaScript via CherryPy

O CherryPy permite criar APIs no servidor, acessadas via AJAX/jQuery pelo cliente.

### Exemplo

#### Servidor Python com CherryPy

```python
import cherrypy
import json

class WebService:
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_data(self):
        data = {'name': 'João', 'age': 25}
        return data

cherrypy.quickstart(WebService(), '/')
```

#### Cliente JavaScript com jQuery

```javascript
$.ajax({
	url: "/get_data",
	type: "GET",
	dataType: "json",
	success: function (response) {
		console.log("Dados recebidos:", response);
		document.getElementById("output").innerText =
			"Nome: " + response.name + ", Idade: " + response.age;
	},
});
```

```javascript
$.ajax() is the most configurable one, where you get fine grained control over HTTP headers and such. You're also able to get direct access to the XHR-object using this method. Slightly more fine-grained error-handling is also provided. Can therefore be more complicated and often unecessary, but sometimes very useful. You have to deal with the returned data yourself with a callback.

$.get() is just a shorthand for $.ajax() but abstracts some of the configurations away, setting reasonable default values for what it hides from you. Returns the data to a callback. It only allows GET-requests so is accompanied by the $.post() function for similar abstraction, only for POST

.load() is similar to $.get() but adds functionality which allows you to define where in the document the returned data is to be inserted. Therefore really only usable when the call only will result in HTML. It is called slightly differently than the other, global, calls, as it is a method tied to a particular jQuery-wrapped DOM element. Therefore, one would do: $('#divWantingContent').load(...)

It should be noted that all $.get(), $.post(), .load() are all just wrappers for $.ajax() as it's called internally.

More details in the Ajax-documentation of jQuery: http://api.jquery.com/category/ajax/
```

#### HTML

```html
<!DOCTYPE html>
<html>
	<head>
		<title>Exemplo CherryPy + jQuery</title>
		<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
	</head>
	<body>
		<h1>Dados do Servidor:</h1>
		<div id="output"></div>

		<script src="script.js"></script>
	</body>
</html>
```

---

## Comunicação HTML ↔ Servidor via Formulário

Outra forma de comunicação é o envio de dados via formulário:

```html
<form action="/action_page.php" method="get">
	<label for="fname">First name:</label>
	<input type="text" id="fname" name="fname" /><br /><br />
	<label for="lname">Last name:</label>
	<input type="text" id="lname" name="lname" /><br /><br />
	<input type="submit" value="Submit" />
</form>
```

---

## Outras Formas Comuns de Comunicação Web

### 1. Fetch API (JavaScript moderno)

```javascript
fetch("/get_data")
	.then((response) => response.json())
	.then((data) => {
		console.log(data);
	});
```

### 2. WebSockets (Comunicação bidirecional em tempo real)

#### Servidor Python

```python
import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        await websocket.send("Recebido: " + message)

start_server = websockets.serve(echo, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
```

#### Cliente JavaScript

```javascript
let socket = new WebSocket("ws://localhost:8765");

socket.onopen = function () {
	socket.send("Olá servidor");
};

socket.onmessage = function (event) {
	console.log("Resposta: " + event.data);
};
```

### 3. REST APIs com JSON

-   Servidor Python expõe endpoints RESTful
-   Cliente JavaScript consome via HTTP

### 4. GraphQL

Permite ao cliente pedir apenas os dados necessários via uma única requisição flexível.

---

## Tabela Resumo

| Tecnologia      | Usado para                | Comunicação      |
| --------------- | ------------------------- | ---------------- |
| Formulário HTML | Submissão de dados        | HTTP GET/POST    |
| AJAX (jQuery)   | Pedidos assíncronos       | HTTP (REST/JSON) |
| Fetch API       | Moderno AJAX              | HTTP (REST/JSON) |
| WebSockets      | Comunicação em tempo real | TCP bidirecional |
| REST API        | Comunicação estruturada   | HTTP (JSON)      |
| GraphQL         | Consultas personalizadas  | HTTP (JSON)      |
