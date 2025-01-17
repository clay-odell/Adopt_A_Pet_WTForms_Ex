from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def connect_db(app):
    """Connect to Database"""
    db.app = app
    db.init_app(app)

"""Models for Pet Adoption"""

class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=True, default='https://www.publicdomainpictures.net/pictures/150000/nahled/pet-silhouette-icons.jpg')
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def save(self):
        db.session.add(self)
        db.session.commit
