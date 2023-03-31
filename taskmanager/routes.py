from flask import render_template
from taskmanager import app, db
# Generate the database from our package (schema for Postgres).
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")


# Supply http methods as we are submitting a form in this view
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    return render_template("add_category.html")
