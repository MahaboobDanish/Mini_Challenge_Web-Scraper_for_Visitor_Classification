from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ClassificationResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    questions = db.Column(db.JSON, nullable=False)  # Store questions as JSON
    options = db.Column(db.JSON, nullable=False)    # Store options as JSON
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class UserSelection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    classification_id = db.Column(db.Integer, db.ForeignKey('classification_result.id'), nullable=False)
    selected_options = db.Column(db.JSON, nullable=False)
    submitted_at = db.Column(db.DateTime, default=db.func.current_timestamp())
