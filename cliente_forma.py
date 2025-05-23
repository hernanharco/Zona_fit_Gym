from flask_wtf import FlaskForm
from wtforms import HiddenField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import StringField, SubmitField
from wtforms.validators import DataRequired


class ClienteForma(FlaskForm):
    id = HiddenField('id')
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    membresia = IntegerField('Membresia', validators=[DataRequired()])
    guardar = SubmitField('Guardar')
