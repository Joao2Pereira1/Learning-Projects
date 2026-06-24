# Flask Application for Sports Registration

This application allows users to register for sports and view a list of registrants.

## Modules

-   flask: framework for building web applications
-   logging: makes debugging easier
-   mysql.connector: manages data in a MySQL database

## Functions

-   home: renders the home page
-   register: renders the registration page
-   about: renders the about page
-   register_done: handles registration form submissions
-   register_list: lists all registrants
-   search: lists all registrants with the name inserted

## Variables

-   SPORTS: list of available sports
-   connection: connection to the MySQL database
-   db: cursor object for performing SQL operations

## API Endpoints

### GET /

The home page of the application. Renders the home.html template.

### GET /register

The registration page of the application. Renders the register.html template.

### POST /register

Handles the registration form submission. Validates the input data and inserts it into the database if valid. Renders the register_done.html template on success or register_failed.html template on failure.

### GET /about

The about page of the application. Renders the about.html template.

### GET /list

Displays a list of all registrants. Retrieves the data from the database and renders the list.html template.

### POST /search

Displays a list of the registrants with the name inserted. Retrieves the data from the database and renders the search.html template.

## Database Schema

The application uses a MySQL database with a single table `registrants` in the `sport` database. The table has two columns:

-   `name`: the name of the registrant
-   `sport`: the sport the registrant is registering for

## Code Organization

The code is organized into the following sections:

-   Routes: defines the API endpoints for the application
-   Database: defines the database schema and connections
-   Templates: defines the HTML templates for the application
