# Flask-SQLAlchemy 'db' var contains all column types (Integer, Float,
# String, etc.), which we can access with dot notation.
from taskmanager import db


class Category(db.Model):
    # Schema for the Category model:
    id = db.Column(db.Integer, primary_key=True)
    # Specify string length, uniqueness and required state.
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    # Link to the Task table:
    tasks = db.relationship(
        # Establish bidirectional relationship with the backref to itself.
        # 'lazy' will identify any linked task when we query the database.
        "Task", backref="category", cascade="all, delete", lazy=True)

    # Represent the class objects as a string:
    def __repr__(self):
        return self.category_name


class Task(db.Model):
    # Schema for the Task model:
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    # Allow longer strings to be used with db.Text:
    task_description = db.Column(db.Text, unique=True, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    # Note lowercase dot notation to point to the FK.
    # Cascade ensures any other tasks with the same category are deleted
    # to avoid throwing an error.
    # See 'one-to-many' relationship. E.g. 10 Tasks, 2 Categories.
    # Deleting a category will take associated tasks with it.
    category_id = db.Column(db.Integer, db.ForeignKey(
        "category.id", ondelete="CASCADE"), nullable=False)

    # Represent the class objects as a string:
    def __repr__(self):
        return f"#{self.id} - Task: {self.task_name} | Urgent:{self.is_urgent}"
