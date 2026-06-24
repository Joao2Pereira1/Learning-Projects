"""
This is a web application for registering at a sport.
Think of it as a website for a school where
u can register yourself to a sport and also see which
sport your friend selected to help u choose.
The application is built using Flask and MySQL.

Author: João Pereira
"""

# TODO to improve this in the future in the chat page
# TODO u can use the name registered, and if not registered ask to register

import logging  # logs in case something happens to be easier to debug

import mysql.connector as mysql  # manage data
from flask import Flask, render_template, request  # framework modules
from flask_socketio import SocketIO, emit  # for web sockets

import credentials  # credentials
from fun_fact_generator import generate_fun_fact  # fun fact generator

# < CONFIGS

# * Logging configuration
logging.basicConfig(
    level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s"
)

# * connection with mysql to work with the database
MYSQL_HOST = "localhost"
try:
    connection = mysql.connect(
        host=MYSQL_HOST, user=credentials.DB_USER, password=credentials.DB_PASS
    )
except mysql.Error as e:
    raise mysql.DatabaseError(f"Failed to connect to database: {e}")

# < APP

SPORTS = ["Football", "Basketball", "Tennis"]  # stores the sports options

app = Flask(__name__)  #  create app

# * set up sockets
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app, cors_allowed_origins="*")


# < Sockets


# *  event that emits message on chat when called
@socketio.on("message")
def handle_message(data):
    # emit the message to all connected clients by having broadcast = True
    print("Message: ", data)
    print(data["user_name"], data["msg"])
    if data:
        emit(
            "message", {"name": data["user_name"], "data": data["msg"]}, broadcast=True
        )  # display message to all users
    else:
        print("No data received.")


# < ROUTES


@app.route("/")
def home():
    """
    Displays page with links to access the other pages like register, list, etc

    Returns:
        html: template (home)
    """
    return render_template(("home.html"))


@app.route("/about")
def about():
    """
    Displays a info message

    Returns:
        html : template (about)
    """
    return render_template(("about.html"))


@app.route("/register")
def register():
    """
    Displays page to make the register (name, sport)

    Returns:
        html: template (register)
    """
    return render_template(("register.html"))


@app.route("/register", methods=["POST"])
def register_done():
    """
    Registers a user for a sport by inserting their name and chosen sport
    into a database table, handling various error cases.

    Returns:
        html: A template indicating whether the registration was successful or not

    Raises:
        mysql.Error: If there is an error inserting the data into the database
    """

    name = request.form.get("name")
    sport = request.form.get("sport")

    if not name:
        return render_template(("register_failed.html"), message="it's missing name.")
    if not sport:
        return render_template(("register_failed.html"), message="it's missing sport.")
    if sport not in SPORTS:
        return render_template(
            ("register_failed.html"), message="it's an invalid sport."
        )

    database = connection.cursor()  # object to perform  SQL operations
    try:
        with database as db:
            insert = "INSERT INTO sport.registrants (name, sport) VALUES (%s, %s)"
            db.execute(
                insert, (name, sport)
            )  # methods run the SQL query and return the result
            connection.commit()  # commit changes to database
    except mysql.Error as e:
        error_message = f"Database error: {e.errno} - {e.msg}"
        logging.error(error_message)
        return render_template(
            ("register_failed.html"), message="it's a database error."
        )
    finally:
        db.close()  # close the cursor for security even if occurs exception

    return render_template(("register_done.html"))


@app.route("/list", methods=["GET"])
def register_list():
    """
    It will return a page with all members and this page
    has a forms to search for a member name

    Returns:
        html: template table with all registrants

    Raises:
        mysql.Error: If there is an error getting the data into the database
    """

    database = connection.cursor()  # object to perform  SQL operations
    try:
        with database as db:
            search = "SELECT * FROM sport.registrants"
            db.execute(search)
            registrants = db.fetchall()  # Fetches all rows of a query result set.
            return render_template(("members_list.html"), registrants=registrants)
    except mysql.Error as e:
        error_message = f"Database error: {e.errno} - {e.msg}"
        logging.error(error_message)
        return "Something went wrong with database."
    finally:
        db.close()  # close the cursor for security even if occurs exception


@app.route("/search", methods=["POST"])
def search():
    """
    It will return a page with all members that match the search

    Returns:
        html: template with a table where name = name inserted in search box

    Raises:
        mysql.Error: If there is an error getting the data into the database
    """
    name = request.form.get("name")  # variable for the search box

    if name:
        database = connection.cursor()  # object to perform  SQL operations
        try:
            with database as db:
                query = "SELECT * FROM sport.registrants WHERE name = %s"
                db.execute(query, (name,))
                result = database.fetchall()
                return render_template("search_result.html", result=result)
        except mysql.Error as e:
            error_message = f"Database error: {e.errno} - {e.msg}"
            logging.error(error_message)
            return "Something went wrong with database."
        finally:
            db.close()  # close the cursor for security even if occurs exception
    else:
        return "Missing name"


# TODO U SHOULD HAVE A STUDENTS DATABASE SO THAT ONLY STUDENTS COULD REGISTER
# TODO AND ONLY ONE TIME TRY DO THAT JUST FOR EXAMPLE

# TODO ADD A LOGIN PAGE AND TRY TO USE SESSION TO KEEP USER LOGGED IN SEARCH MORE ABOUT THAT


@app.route("/chat")
def chat():
    # TODO AUTHENTICATION GET USERNAME TO THEN DISPLAY MESSAGE WITH USER NAME
    return render_template("chat.html")


@app.route("/fun_fact")
def fun_fact():
    useless_fact = generate_fun_fact()
    html_content = "<p>Fun Fact: {}</p>".format(useless_fact)
    return html_content


if __name__ == "__main__":
    # * to connect through multiple devices u need to put your ipv4 address
    socketio.run(app, host="localhost:5000")
    connection.close()
