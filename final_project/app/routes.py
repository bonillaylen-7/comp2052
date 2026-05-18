from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app.forms import EventoForm, ChangePasswordForm
from app.models import db, Evento, User
from datetime import datetime

# Blueprint principal
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/cambiar-password', methods=['GET', 'POST'])
@login_required
def cambiar_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if not current_user.check_password(form.old_password.data):
            flash('La contraseña actual es incorrecta.')
            return render_template('cambiar_password.html', form=form)
        current_user.set_password(form.new_password.data)
        db.session.commit()
        flash('Contraseña actualizada exitosamente.')
        return redirect(url_for('main.dashboard'))
    return render_template('cambiar_password.html', form=form)

@main.route('/dashboard')
@login_required
def dashboard():
    if current_user.role.name == 'Participante':
        eventos = Evento.query.all()
    else:
        eventos = Evento.query.filter_by(organizador_id=current_user.id).all()
    return render_template('dashboard.html', eventos=eventos)

@main.route('/eventos', methods=['GET', 'POST'])
@login_required
def eventos():
    form = EventoForm()
    if form.validate_on_submit():
        evento = Evento(
            nombre=form.nombre.data,
            ubicacion=form.ubicacion.data,
            fecha_hora=datetime.strptime(form.fecha_hora.data, '%Y-%m-%d %H:%M'),
            capacidad=int(form.capacidad.data),
            descripcion=form.descripcion.data,
            organizador_id=current_user.id
        )
        db.session.add(evento)
        db.session.commit()
        flash('Evento creado exitosamente.')
        return redirect(url_for('main.dashboard'))
    return render_template('evento_form.html', form=form)

@main.route('/eventos/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def editar_evento(id):
    evento = Evento.query.get_or_404(id)
    if current_user.role.name not in ['Admin', 'Organizador'] or (
        evento.organizador_id != current_user.id and current_user.role.name != 'Admin'):
        flash('No tienes permiso para editar este evento.')
        return redirect(url_for('main.dashboard'))
    form = EventoForm(obj=evento)
    if form.validate_on_submit():
        evento.nombre = form.nombre.data
        evento.ubicacion = form.ubicacion.data
        evento.fecha_hora = datetime.strptime(form.fecha_hora.data, '%Y-%m-%d %H:%M')
        evento.capacidad = int(form.capacidad.data)
        evento.descripcion = form.descripcion.data
        db.session.commit()
        flash('Evento actualizado exitosamente.')
        return redirect(url_for('main.dashboard'))
    form.fecha_hora.data = evento.fecha_hora.strftime('%Y-%m-%d %H:%M')
    return render_template('evento_form.html', form=form, editar=True)

@main.route('/eventos/<int:id>/eliminar', methods=['POST'])
@login_required
def eliminar_evento(id):
    evento = Evento.query.get_or_404(id)
    if current_user.role.name not in ['Admin', 'Organizador'] or (
        evento.organizador_id != current_user.id and current_user.role.name != 'Admin'):
        flash('No tienes permiso para eliminar este evento.')
        return redirect(url_for('main.dashboard'))
    db.session.delete(evento)
    db.session.commit()
    flash('Evento eliminado exitosamente.')
    return redirect(url_for('main.dashboard'))

@main.route('/usuarios')
@login_required
def listar_usuarios():
    if current_user.role.name != 'Admin':
        flash('No tienes permiso para ver esta página.')
        return redirect(url_for('main.dashboard'))
    usuarios = User.query.join(User.role).all()
    return render_template('usuarios.html', usuarios=usuarios)