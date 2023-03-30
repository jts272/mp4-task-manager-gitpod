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