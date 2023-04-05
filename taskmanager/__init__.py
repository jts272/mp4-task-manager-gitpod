# Initialize taskmanager/ as a package with this file.
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

# Conditional for deployment:
if os.environ.get("DEVELOPMENT"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    # Create new 'DATABASE_URL' var
    uri = os.environ.get("DATABASE_URL")
    # Further condition to change the URL for SQLAlchemy compatibility
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    # Then point to the 'uri' var with correct URL requirements
    app.config["SQLALCHEMY_DATABASE_URI"] = uri

db = SQLAlchemy(app)

# 'routes' is last as it relies on 'app' and 'db'.
# 'noqa' prevents linting errors and formatters forcing this import to
# the top of the file.
from taskmanager import routes  # noqa
