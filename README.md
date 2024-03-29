# Task Manager - Flask and SQLAlchemy

## Initial setup

Gitpod full template

`pip3 install 'Flask-SQLAlchemy<3' psycopg2 sqlalchemy==1.4.46`

## Database setup

After schema definitions:

`set_pg`

`psql`

`CREATE DATABASE taskmanager;`

`\c taskmanager;` to connect to the database

`\q` to exit

### Generate and migrate Python models to the database

**If models are modified, changes must be migrated each time**

`python3` access Python shell

\>>>`from taskmanager import db`

\>>>`db.create_all()`

\>>>`exit()`

### Confirm existence of tables within the database

`psql -d taskmanager`

`\dt`

---

## Flask Setup

Create `static` dir

Use `{{ url_for }}` syntax to link to local styles and scripts. CDN links can be
used as normal.

## Getting data from the backend to the frontend

*R in CRUD*

1. Create the var in the `@app.route` of the view you wish to use to display the
given data. In general, this is a Python list made using the Flask/SQLAlchemy
`query` method on the imported model.
   - Querying the DB returns a 'Cursor Object' or 'QuerySet'. It is better to
   convert them to Python lists.
2. Pass this var into the `render_template()` e.g. `tasks=tasks`

## Supplying DB keys into URLs

1. When using the `{{ url_for }}` syntax to link to a page, the variable is made
here. E.g. `<a href="{{ url_for('edit_task', task_id=task.id) }}">Edit</a>`. The
dot notation part points to the actual `table.key`
2. Now this var can be supplied in the routes and function definition, e.g.
```
@app.route("edit_task/<int:task_id>)
def edit_task(task_id):
    #
```

## Prepopulating forms with pre-exisitng DB values

This is useful in instanced where the user wants to edit their submitted values

Within an input element's opening tag:

`value="{{ table.key }}"`

Supply this *inside* the tags for `<textarea>` elements

Remember to supply the relevant `strftime()` to match date format.

Conditional logic is used on checkboxes to see if the checkbox/switch inherits
the `checked` bool attribute from the DB.

For `<select>`, use conditional logic to check the category from the DB and add
the `selected` attribute *within* the for loop that displays each `<option>`

`{{- table.key -}}` will eliminate added whitespace in textareas with the minus
symbol.

## Deployment Considerations

Confirm actions on delete with modals

Current app routes aren't protected so any site visitor has full CRUD access

Using the backref and cascade deletes tasks associated with the deleted
category, preventing errors.

## Deployment Procedure

1. Sign up to ElephantSQL and link GitHub
2. Create instance and select datacenter
3. `pip freeze --local > requirements.txt`
4. Create `Procfile` for Heroku (No trailing empty line):
```
web: python run.py
```
5. See changes to `__init__.py` to conditionally setup the external database for
SQLAlchemy requirements
6. Create a new app in Heroku. The new `DATABASE_URL` var comes from the
ElephantSQL instance. Copy the contents of `env.py`, excluding the `DEVELOPMENT`
and `DB_URL` vars, when setting the config vars in Heroku (excluding quotation
marks)
```
"DATABASE_URL", "url_from_elephantsql"
"IP", "0.0.0.0"
"PORT", "5000"
"SECRET_KEY", "whatever_secret_key"
"DEBUG", "True"
```
**Debug is set *temporarily* in case of errors during deployment**

7. The database is ready, but empty. Deploying now will generate an error,
because the databse models have not yet been provided. In the Heroku dashboard,
run a `python3` terminal:
```
from taskmanager import db
db.create_all()
exit()
```
8. Link the GitHub repository and optionally enable automatic updates. The app
can now be fully deployed! Test functionality and enjoy!