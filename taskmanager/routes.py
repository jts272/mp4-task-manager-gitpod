# request used for form processing
# redirect and url_for used on form POST
from flask import render_template, request, redirect, url_for
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
    if request.method == "POST":
        # New instance of the imported Category model
        # We supply the key the model is expecting ('category_name'),
        # then populate this var with the input from the form field with
        # matching name attr.
        category = Category(category_name=request.form.get("category_name"))
        # We can now add and commit this form data to the SQLAlchemy
        # database var of 'db', using the database sessionmaker instance
        db.session.add(category)
        db.session.commit()
        # Redirect to the categories() function using Flask imports
        return redirect(url_for("categories"))

    # Default 'GET' behaviour (pseudo-else condition):
    return render_template("add_category.html")
