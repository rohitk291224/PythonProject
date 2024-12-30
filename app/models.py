# Python/PythonProject/app/models.py
from app import db
class Tour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    def __repr__(self):
        return f'<Tour {self.name}>'