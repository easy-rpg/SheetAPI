from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField, IntegerField, FloatField, HiddenField, SelectMultipleField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, NumberRange
from wtforms_alchemy import ModelForm
from rpg.core.models import Usuario

class LoginForm(ModelForm, FlaskForm):
    class Meta:
        model = Usuario