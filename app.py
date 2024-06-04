from flask import Flask, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, Pet




app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:01302@localhost/pet_adoption"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

debug = DebugToolbarExtension(app)

with app.app_context():
    connect_db(app)
    db.create_all()


@app.route('/')
def show_pets():
    pets = Pet.query.all()
    return render_template('pet_list_home.html', pets=pets)