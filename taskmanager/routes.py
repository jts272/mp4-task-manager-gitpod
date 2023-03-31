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
    # all() method returns a cursor object.
    # Wrap the var to convert into a Python list with 'list()'
    categories = list(Category.query.order_by(Category.category_name).all())
    # Return the categories var defined above in the view
    # First 'categories' = used in the html template
    # Second 'categories' = the content of the Python var from this
    # function.

    return render_template("categories.html", categories=categories)


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


# The var we supply from clicking the 'Edit' button in
# edit_category.html is in angled brackets.
# We have casted it as 'int' as it is the Primary Key
@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
# Pass in the category_id var to the function
def edit_category(category_id):
    # Define 'category' for the edit button
    # We query the imported 'Category' model from the database
    category = Category.query.get_or_404(category_id)
    # POST:
    if request.method == "POST":
        # Change the category name in the DB to that of the form input
        category.category_name = request.form.get("category_name")
        # Update DB and redirect back to the rest of the categories
        db.session.commit()
        return redirect(url_for("categories"))
    # GET:
    # Make the 'category' var (Primary Key for loop instance) available
    return render_template("edit_category.html", category=category)
