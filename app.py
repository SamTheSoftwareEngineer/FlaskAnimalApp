"""Flask application for adopt app."""

from flask import Flask, url_for, render_template, redirect, flash, jsonify

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

"""Defines the routes for the application."""

@app.route('/')
def list_of_pets():
    """Shows a list of pets."""
    pets = Pet.query.all()
    return render_template('list.html', pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Adds a pet."""
    
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
        flash(f"{name} added!")
        
        return redirect(url_for('list_of_pets'))
    
    else:
        """"Shows the form to add a pet."""
        return render_template('add.html', form=form)
    
@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edits a pet."""
    
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        
        db.session.commit()
        flash(f"{pet.name} updated!")
        
        return redirect(url_for('list_of_pets'))
    
    else:
        # failed; re-present form for editing 
        return render_template('edit.html', form=form, pet=pet)
    
@app.route("/api/pets/<int:pet_id>", methods=["GET"])
def api_get_pet(pet_id):
    """Gets pet info from the database in JSON."""
    
    pet = Pet.query.get_or_404(pet_id)
    info = {"name": pet.name, "age": pet.age}
    
    return jsonify(info)