from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Fault(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    date_reported = db.Column(db.Date, nullable=False)
    resolved = db.Column(db.Boolean, default=False)
