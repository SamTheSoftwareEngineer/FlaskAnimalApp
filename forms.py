"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    """"Form for adding pets."""
    
    name = StringField(
        "Pet Name", 
        validators=[InputRequired()]
    )
    
    species = SelectField(
        "Species",
        choices = [("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],
    )
    
    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )
    
    age = IntegerField(
        "Age",
        validators=[Optional(), NumberRange(min=0, max=50)],
    )
    
    notes = TextAreaField(
        "comments about pet",
        validators=[Optional(), Length(min=0, max=250)],
    )
    
    class EditPetForm(FlaskForm):
        """Form for editing existing pets."""
        
        photo_url = StringField(
            "Photo URL",
            validators=[Optional(), URL()],
        )
        
        notes = TextAreaField(
            "comments about pet",
            validators=[Optional(), Length(min=0, max=250)],
        )
        
        available = BooleanField("Available?")
        