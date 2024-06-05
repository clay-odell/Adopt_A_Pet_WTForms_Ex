from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, FloatField 
from wtforms.validators import InputRequired, Optional, NumberRange, URL

class AddPetForm(FlaskForm):
    """Form For Adopting Pet"""
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')], validators=[InputRequired()])
    photo = StringField("Photo URL", validators=[Optional(strip_whitespace=True), URL()])
    age = FloatField('Age', validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField('Notes', validators=[Optional()])
