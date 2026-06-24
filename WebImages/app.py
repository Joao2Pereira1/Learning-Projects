# encoding=utf-8
#
# Example of a cherrypy application that serves images.
#
# To run: python3 app.py

import hashlib
import json
import os.path
import sqlite3 as sql
import time

import cherrypy  # type: ignore

from processing import process_image

#! ter ficheiros js e html com o mesmo nome, causa conflitos

# The absolute path to this file's base directory
baseDir = os.path.abspath(os.path.dirname(__file__))

# Dictionary with this application's static directories configuration
config = {
    "/": {"tools.staticdir.root": baseDir},
    "/html": {"tools.staticdir.on": True, "tools.staticdir.dir": "html"},
    "/js": {"tools.staticdir.on": True, "tools.staticdir.dir": "js"},
    "/css": {"tools.staticdir.on": True, "tools.staticdir.dir": "css"},
    "/images": {"tools.staticdir.on": True, "tools.staticdir.dir": "images"},
    "/uploads": {"tools.staticdir.on": True, "tools.staticdir.dir": "uploads"},
    "/processed": {"tools.staticdir.on": True, "tools.staticdir.dir": "processed"},
}


class Root:
    counter_file = "counter.txt"
    counter = 0

    def __init__(self):
        """a cada vez que o servidor é inicializado, para não haver ficheiros de imagens
        processadas com o mesmo nome, o que poderia substituir ficheiros ja existentes,
        guardei o counter num ficheiro de texto e assim o counter ao inicializar
        o servidor, se tiver 10 imagens, counter = 10, etc
        """

        # inicializa o counter lendo o ficheiro, se existir
        try:
            with open(self.counter_file, "r") as f:
                Root.counter = int(f.read().strip())
        except (FileNotFoundError, ValueError):
            Root.counter = 0

    def update_counter_file(self):
        with open(self.counter_file, "w") as f:
            f.write(str(Root.counter))

    @cherrypy.expose
    def index(self):
        """Retorna a pagina onde vai ser realizado o registo de um novo usuario ou login"""
        return open("html/register.html")

    @cherrypy.expose
    def intro(self):
        # Verifica se utilizador esta logged in na sessao atual
        if not cherrypy.session.get("logged_in"):
            raise cherrypy.HTTPRedirect("/")  # redireciona para o login
        return open("html/intro.html")

    @cherrypy.expose
    def register(self, user, passw):
        """Recebe os argumentos user e password do metodo register() em registering.js,
        com esses dados, cria um novo utilizador, caso não exista
        nenhum utilizador com esse nome
        """

        db = sql.connect("database.db")
        cursor = db.cursor()
        # inserir dados novos
        try:
            # verificar se já existe algum utilizador com esse nome
            result = cursor.execute("SELECT * FROM users WHERE username = ?", (user,))
            if result.fetchone():
                response = {"status": "error", "message": "Username já existe"}
            else:
                # inserir novo utilizador
                cursor.execute(
                    "INSERT INTO users (username, password) VALUES (?, ?)",
                    (user, passw),
                )
                db.commit()
                response = {"status": "ok", "message": "Registo feito com sucesso"}

        except Exception as e:
            response = {"status": "error", "message": str(e)}

        finally:
            db.close()

        cherrypy.response.headers["Content-Type"] = "application/json"

        return json.dumps(response).encode("utf-8")

    @cherrypy.expose
    def login(self, user, passw):
        """Verifica credenciais do utilizador que sao retornadas de login()
        em registering.js e cria sessão se válidas"""

        db = sql.connect("database.db")
        cursor = db.cursor()

        result = cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?", (user, passw)
        )
        row = cursor.fetchone()
        db.close()

        # usar sessoes de cherrypy para saber se o utilizador esta logged in
        if row:
            cherrypy.session["logged_in"] = True
            cherrypy.session["username"] = user
            response = {"status": "ok", "message": "Login feito com sucesso"}
        else:
            response = {"status": "error", "message": "Credenciais inválidas"}

        cherrypy.response.headers["Content-Type"] = "application/json"

        return json.dumps(response).encode("utf-8")

    @cherrypy.expose
    def logout(self):
        """Termina a sessão do utilizador"""
        cherrypy.session.clear()
        raise cherrypy.HTTPRedirect("/")  # redireciona para a página inicial

    @cherrypy.expose
    def upload(self, myFile, nameImg, authorImg):
        """Esta funcao recebe um ficheiro, nome da imagem e o autor que carregou a página da upload.html
        Depois guarda essa imagem na pasta uploads com o nome do ficheiro que é uma sintese do seu conteudo hsa256
        Por fim guarda os dados dessa imagem na base de dados na tabela imagens"""

        h = hashlib.sha256()

        filename = baseDir + "/uploads/" + myFile.filename
        fileout = open(filename, "wb")
        while True:
            data = myFile.file.read(8192)
            if not data:
                break
            fileout.write(data)
            h.update(data)
        fileout.close()

        # guarda a imagem carregada num ficheiro, cujo o nome
        # é um hash do conteudo do ficheiro no diretorio local "uploads"
        ext = myFile.filename.split(".")[-1]
        path = baseDir + "/uploads/" + h.hexdigest() + "." + ext
        os.rename(filename, path)

        # obtem a data
        datetime = time.strftime("date:%d-%m-%Y time:%H:%M:%S")

        # insere a informacao do ficheiro na tabela images
        # eventualmente inicializa a tabela de votos

        db = sql.connect("database.db")
        db.execute(
            "INSERT INTO images (name, author, path, datetime) VALUES (?, ?, ?, ?)",
            (nameImg, authorImg, path, datetime),
        )
        db.commit()
        db.close()

    @cherrypy.expose
    def list(self, id):
        """Recebe um id que é pesquisado na barra de navegacao da pagina gallery.html
        Depois  vai buscar as imagens com esse id na base de dados e com o resultado da
        base de dados, criar uma lista de dicionarios e essa lista é retornada para
        depois ser possivel inserir atraves de javascript informacoes da imagem,
        e até mesmo carregar a imagem"""

        db = sql.connect("database.db")
        cursor = db.cursor()

        if id == "all":
            result = cursor.execute("SELECT * FROM images")
        else:
            result = cursor.execute("SELECT * FROM images WHERE id = (?)", (id,))
        rows = result.fetchall()
        db.close()

        # gera result (list of dictionaries) de rows (list of tuples)
        result = []
        for row in rows:
            data = {
                "id": row[0],
                "name": row[1],
                "author": row[2],
                "path": row[3],
                "datetime": row[4],
            }
            result.append(data)

        # ordena o resultado pelo nome de imagem
        result.sort(key=lambda t: t["name"])

        cherrypy.response.headers["Content-Type"] = "application/json"
        return json.dumps({"images": result}).encode("utf-8")

    @cherrypy.expose
    def comments(self, idimg):
        """ """

        db = sql.connect("database.db")
        cursor = db.cursor()

        result = cursor.execute("SELECT * FROM images WHERE id = ?", (idimg,))
        row = result.fetchone()

        if not row:
            cherrypy.response.status = 404
            return json.dumps({"error": "Imagem não encontrada"}).encode("utf-8")

        imageinfo = {
            "id": row[0],
            "name": row[1],
            "author": row[2],
            "path": row[3],
            "datetime": row[4],
        }

        result = cursor.execute(
            "SELECT user,comment FROM comments WHERE idimg = ?", (idimg,)
        )
        comment_rows = result.fetchall()
        comments = []
        for row in comment_rows:
            comments.append(f"Nome: {row[0]} Comentário: {row[1]}")

        result = cursor.execute(
            "SELECT ups, downs FROM votes WHERE idimg = ?", (idimg,)
        )
        vote_row = result.fetchone()

        if vote_row:
            thumbs_up, thumbs_down = vote_row
        else:
            thumbs_up, thumbs_down = 0, 0

        db.close()

        imagevotes = {"thumbs_up": thumbs_up, "thumbs_down": thumbs_down}

        cherrypy.response.headers["Content-Type"] = "application/json"
        return json.dumps(
            {"image": imageinfo, "comments": comments, "votes": imagevotes}
        ).encode("utf-8")

    @cherrypy.expose
    def newcomment(self, idimag, username, newcomment):
        """Insere um novo comentario na base dados com os dados inseridos em image.html"""

        db = sql.connect("database.db")
        cursor = db.cursor()
        datetime = time.strftime("date:%d-%m-%Y time:%H:%M:%S")

        print("Recebido:")
        print("idimag =", idimag)
        print("username =", username)
        print("newcomment =", newcomment)

        cursor.execute(
            "INSERT INTO comments (idimg, [user], comment, datetime) VALUES (?, ?, ?, ?)",
            (idimag, username, newcomment, datetime),
        )
        db.commit()
        db.close()

    @cherrypy.expose
    def upvote(self, idimag):
        """quando clicamos numa imagem da galeria, somos redirecionados para image.html,
        onde podemos dar likes/deslikes e esses dados vao ser guardados na base de dados
        e tambem enviados via json para depois o javascript mostrar os likes em image.html
        """

        db = sql.connect("database.db")
        cursor = db.cursor()

        result = cursor.execute("SELECT ups FROM votes WHERE id = ?", (idimag,))
        up_votes = result.fetchone()

        if up_votes:
            current = up_votes[0]
            new_value = current + 1
            cursor.execute("UPDATE votes SET ups = ? WHERE id = ?", (new_value, idimag))
            db.commit()

        result = cursor.execute("SELECT ups, downs FROM votes WHERE id = ?", (idimag,))
        votes = result.fetchone()
        db.close()

        cherrypy.response.headers["Content-Type"] = "application/json"
        return json.dumps({"ups": votes[0], "downs": votes[1]}).encode("utf-8")

    # Increment Down votes
    @cherrypy.expose
    def downvote(self, idimag):
        db = sql.connect("database.db")
        cursor = db.cursor()

        result = cursor.execute("SELECT downs FROM votes WHERE id = ?", (idimag,))
        down_votes = result.fetchone()

        if down_votes:
            current = down_votes[0]
            new_value = current + 1
            cursor.execute(
                "UPDATE votes SET downs = ? WHERE id = ?", (new_value, idimag)
            )
            db.commit()

        # pegar o total atualizado para retornar como JSON
        result = cursor.execute("SELECT ups, downs FROM votes WHERE id = ?", (idimag,))
        votes = result.fetchone()
        db.close()

        cherrypy.response.headers["Content-Type"] = "application/json"
        return json.dumps({"ups": votes[0], "downs": votes[1]}).encode("utf-8")

    @cherrypy.expose
    def imageproc(self, path, algorithm):
        """Recebe path e algorithm da página process.html, aplica o algoritmo à imagem
        e guarda-a com um nome único baseado num contador persistente."""

        filename = os.path.basename(path)
        input_path = os.path.join("uploads", filename)

        # Aplica o algoritmo de processamento de imagem (função externa)
        image_bytes = process_image(input_path, algorithm)

        # Nome do novo ficheiro
        output_filename = f"img{Root.counter}.png"
        output_path = os.path.join("processed", output_filename)

        # Guarda a imagem
        with open(output_path, "wb") as f:
            f.write(image_bytes)

        # Atualiza o counter e salva no ficheiro
        Root.counter += 1
        self.update_counter_file()

        # Envia o path em JSON
        cherrypy.response.headers["Content-Type"] = "application/json"
        return json.dumps({"processed_path": f"/processed/{output_filename}"}).encode(
            "utf-8"
        )


if __name__ == "__main__":
    # sessoes ativas com limite de 60 minutos
    cherrypy.config.update(
        {
            "tools.sessions.on": True,
            "tools.sessions.timeout": 60,  # minutos
            "server.socket_host": "127.0.0.1",
            "server.socket_port": 8080,
        }
    )

    cherrypy.quickstart(Root(), "/", config)
