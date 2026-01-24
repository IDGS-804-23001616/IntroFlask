from wtforms import Form
from wtforms import StringField, PasswordField, EmailField, BooleanField, IntegerField
from wtforms import validators

class UserForm(Form):
    matricula = IntegerField(
        'Matricula',
        [validators.DataRequired(message="campo requerido papa")]
    )

    nombre = StringField(
        'Nombre',
        [validators.DataRequired(message="campo requerido papa")]
    )

    apellido = StringField(
        'Apellido',
        [validators.DataRequired(message="campo requerido papa")]
    )

    correo = EmailField(
        'Correo',
        [validators.DataRequired(message="campo requerido papa")]
    )
