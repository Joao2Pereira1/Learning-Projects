# ⚽ Sports Registration Web Application

## Overview

The **Sports Registration Web Application** is a web-based system developed with **Flask** that allows users to register for sports activities through a simple interface. Registration data is stored in a **MySQL** database, enabling users to browse all registrants or search for specific participants.

The project demonstrates the integration of Flask routing, HTML templates, form validation, and relational database management.

---

# Features

- Register participants for sports activities
- Choose from a predefined list of sports
- Store registrations in a MySQL database
- Display all registered participants
- Search participants by name
- Validate user input before storing data
- Informative pages (Home and About)

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Backend logic |
| Flask | Web framework |
| MySQL | Data storage |
| mysql-connector-python | MySQL database connector |
| HTML | User interface |
| Jinja2 | Dynamic page rendering |
| Logging | Debugging and error tracking |

---

# Available Sports

The application provides a predefined list of sports stored in the `SPORTS` variable.

Example:

- Football
- Basketball
- Volleyball
- Tennis
- Swimming

---

# Routes

## `GET /`

Displays the application's home page.

**Template**

- `home.html`

---

## `GET /register`

Displays the registration form.

**Template**

- `register.html`

---

## `POST /register`

Processes the submitted registration form.

### Responsibilities

- Validates the participant's name
- Validates the selected sport
- Stores valid registrations in the database
- Displays a success or failure page

**Templates**

- `register_done.html`
- `register_failed.html`

---

## `GET /list`

Retrieves every registered participant from the database.

**Template**

- `list.html`

---

## `POST /search`

Searches for participants using the provided name.

**Template**

- `search.html`

---

## `GET /about`

Displays information about the project.

**Template**

- `about.html`

---

# Main Functions

| Function | Description |
|----------|-------------|
| `home()` | Renders the application's home page. |
| `register()` | Displays the registration form. |
| `register_done()` | Processes and validates registration requests. |
| `register_list()` | Retrieves and displays all registrants. |
| `search()` | Searches registrants by name. |
| `about()` | Displays project information. |

---

# Database

The application uses a **MySQL** database.

## Database

```text
sport
```

## Table

```text
registrants
```

### Schema

| Column | Type | Description |
|---------|------|-------------|
| `id` *(optional)* | INT | Primary key |
| `name` | VARCHAR | Participant name |
| `sport` | VARCHAR | Selected sport |

---

# Database Connection

The application establishes a connection using `mysql.connector`.

## Main Objects

| Variable | Description |
|----------|-------------|
| `connection` | Connection object to the MySQL server |
| `db` | Cursor used to execute SQL statements |

---

# Input Validation

Before inserting data into the database, the application verifies that:

- The participant's name is not empty.
- The selected sport exists in the predefined sports list.
- Invalid submissions are rejected.

---

# Error Handling

The application includes basic error handling for:

- Invalid form submissions
- Database connection issues
- SQL execution errors

Logging is used to assist with debugging and monitoring application behavior.

---

# Requirements

- Python 3.10+
- Flask
- mysql-connector-python
- MySQL Server

Install the required packages:

```bash
pip install flask mysql-connector-python
```

---

# Running the Application

Start the Flask server:

```bash
python app.py
```

Then open your browser and visit:

```text
http://localhost:5000
```

---

# License

This project is distributed under the MIT License.
