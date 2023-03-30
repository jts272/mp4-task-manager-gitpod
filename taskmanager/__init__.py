# Initialize taskmanager/ as a package with this file.
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

# 'routes' is last as it relies on 'app' and 'db'.
# 'noqa' prevents linting errors and formatters forcing this import to
# the top of the file.
from taskmanager import routes  # noqa
