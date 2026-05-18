from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length

# Formulario para login de usuario
class LoginForm(FlaskForm):
    email = StringField('Correo Electrónico', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')

# Formulario para registrar un nuevo usuario
class RegisterForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired()])
    email = StringField('Correo Electrónico', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar Contraseña', validators=[DataRequired(), EqualTo('password')])
    
    role = SelectField(
        'Rol',
        choices=[('Participante', 'Participante'), ('Organizador', 'Organizador'), ('Admin', 'Admin')],
        validators=[DataRequired()]
    )

    submit = SubmitField('Registrarse')

# Formulario para cambiar la contraseña del usuario
class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Contraseña Actual', validators=[DataRequired()])
    new_password = PasswordField('Nueva Contraseña', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirmar Nueva Contraseña', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Actualizar Contraseña')

# Formulario para crear o editar un evento
class EventoForm(FlaskForm):
    nombre = StringField('Nombre del evento', validators=[DataRequired()])
    ubicacion = StringField('Ubicación', validators=[DataRequired()])
    fecha_hora = StringField('Fecha y hora (YYYY-MM-DD HH:MM)', validators=[DataRequired()])
    capacidad = StringField('Capacidad', validators=[DataRequired()])
    descripcion = TextAreaField('Descripción', validators=[DataRequired()])
    submit = SubmitField('Guardar')