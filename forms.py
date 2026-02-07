from wtforms import Form
from wtforms import StringField, PasswordField, EmailField, BooleanField, IntegerField,RadioField

from wtforms import validators


class UserForm(Form):
    matricula=IntegerField("Matricula", [
        validators.DataRequired(message='El campo es requerido')
    ])
    nombre=StringField("Nombre", [
        validators.DataRequired(message='El campo es requerido')
    ])
    apellido=StringField("Apellido", [
        validators.DataRequired(message='El campo es requerido')
    ])
    correo=EmailField("Correo", [
        validators.Email(message='Ingrese correo valido')
    ])
    


class CinepolisForm(Form):
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El nombre es requerido"),
    ])

    compradores = IntegerField("Cantidad Compradores", [
        validators.DataRequired(message="La cantidad de compradores es requerida"),
    ])

    cineco = RadioField(
        "Tarjeta Cineco",
        choices=[("si", "Si"), ("no", "No")],
        validators=[validators.DataRequired(message="Selecciona Si o No")]
    )

    boletos = IntegerField("Cantidad de Boletas", [
        validators.DataRequired(message="La cantidad de boletos es requerida"),
    ])
