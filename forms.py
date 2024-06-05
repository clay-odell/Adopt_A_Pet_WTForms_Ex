from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, FloatField
from wtforms.validators import InputRequired, Optional

class AddPetForm(FlaskForm):
    """Form For Adopting Pet"""
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", validators=[InputRequired()],choices=[('cat', 'Cat'), ('dog', 'Dog'), ('mouse', 'Mouse'), ('horse', 'Horse'), ('gerbil', 'Gerbil'), ('gp', 'Guinea Pig'), ('llama', 'Llama'), ('hamster', 'Hamster'), ('bird', 'Bird')])
    photo = StringField("Photo URL", validators=[Optional()])
    age = FloatField('Age', validators=[Optional()])
    notes = TextAreaField('Notes', validators=[Optional()])
