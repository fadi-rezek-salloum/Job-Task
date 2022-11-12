# Job Task Quick Start

## Installation

First, install Docker.

Next, install Postgresql.

Finally, clone this repo:

    $ git clone https://github.com/fadi-rezek-salloum/Job-Task.git JobTask
    $ cd JobTask

## Configure the project

First, migrate the database in order to apply the created scheme:
    $ docker-compose exec web python manage.py migrate

Next, create a super user using this command:
    $ docker-compose exec web python manage.py createsuperuser

Next, Build the Docker image:

    $ docker-compose up -d --build .

Finally, Run the Docker image:

    $ docker-compose up

Thus, you could access the django localhost on port 8000 (http://localhost:8000)

## Django Routes

1. Create a normal user (registration): http://localhost:8000/accounts/register/ .
2. Create a new note: http://localhost:8000/notes/create/ .
3. List all notes: http://localhost:8000/notes/ .
4. Review a note: http://localhost:8000/notes/details/<pk>/ (pk = primary key of any note which is an integer).
5. Delete a note: http://localhost:8000/notes/delete/<pk>/ (pk = primary key of any note which is an integer).