from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SampleTable(db.Model):
    __tablename__ = 'sample_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
