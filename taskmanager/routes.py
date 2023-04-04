# request used for form processing
# redirect and url_for used on form POST
from flask import render_template, request, redirect, url_for
from taskmanager import app, db
# Generate the database from our package (schema for Postgres).
from taskmanager.models import Category, Task


@app.route("/")
def home():
    # CRUD-R
    # Extract tasks from the database to show on homepage. Query the DB
    # and order by id. Uses the imported Task model. Convert to list.
    tasks = list(Task.query.order_by(Task.id).all())
    # Pass this list to the frontend template
    return render_template("tasks.html", tasks=tasks)


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


# Deletion handled in back end. New template unnecessary.
# Pass category_id vars into route and function
# Best practice to include a confirmation modal first in real deployment
# As it is in a loop, href="#modal{{ category.id }}"
# See https://youtu.be/EyTSAkZWHY4?t=290
# Also, authentication would be implemented so deletion is tied to the
# current user's records.
@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    # DB query
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))


# Supply http methods as we are submitting a form in this view
@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    # Extract all categories available so user can select a category for
    # their task
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        # Update POST method to reflect each of the field that will be
        # added from the form we will create
        task = Task(
            task_name=request.form.get("task_name"),
            task_description=request.form.get("task_description"),
            is_urgent=bool(True if request.form.get("is_urgent") else False),
            due_date=request.form.get("due_date"),
            category_id=request.form.get("category_id")
        )
        # Once form is submitted, add the new 'task' var to the DB
        # session.
        db.session.add(task)
        db.session.commit()
        # Redirect to the home() function after submitting
        return redirect(url_for("home"))

    # If not 'POST', show form to add task
    # Pass in var to display categories
    return render_template("add_task.html", categories=categories)


# CRUD - UPDATE
# Create task_id var so the function knows which particular task we want
# to edit, then pass it to the function
@app.route("/edit_task/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        task.task_name = request.form.get("task_name")
        task.task_description = request.form.get("task_description")
        task.is_urgent = bool(True if request.form.get("is_urgent") else False)
        task.due_date = request.form.get("due_date")
        task.category_id = request.form.get("category_id")
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit_task.html", task=task, categories=categories)
