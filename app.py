from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, Pet
from forms import AddPetForm, EditPetForm




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

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Add A Pet Form and Handling"""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else: 
        return render_template('add_pet.html', form=form)
    
@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def show_and_edit_pet_profile(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm()
    form.photo_url.render_kw = {'placeholder': pet.photo_url}
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect(f'/{pet_id}')
    else:
        return render_template('pet_profile.html', pet=pet, form=form)

        