Clone this repository

Install dependencies

``` shell
pipenv install -r requirements.txt --python=python3
```

This create a .venv environment for packages and corresponding Pipfile and Pipfile.lock

Setup your MongoDB Atlas Cluster0 using AWS /N. Virginia(us-east-1). user as Tom(or your name), password in database access and add your local computer's ip address into Atlas network access.

In your Cluster0, connect and connect your application using python driver and version 3.11 or later.
Add your connection string into application file("__init__.py"):

``` shell
mongodb+srv://Tom:<password>@cluster0.f29fg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
```

Get into your pipenv, seed your database, and run your flask app
``` shell
pipenv shell
flask run
```

IMPORTANT! If you add any python dependencies to your pipfiles, you'll need to regenerate your requirements.txt before deployment. You can do this by running:

``` shell
pipenv lock -r > requirements.txt
```