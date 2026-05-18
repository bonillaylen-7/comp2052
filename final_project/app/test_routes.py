from flask import Blueprint, request, jsonify
from app.models import db, Evento
from datetime import datetime

# Blueprint solo con endpoints de prueba para eventos
main = Blueprint('main', __name__)

@main.route('/') # Ambas rutas llevan al mismo lugar
@main.route('/dashboard')
def index():
    """
    Página de inicio pública (home).
    """
    return '<h1>Corriendo en Modo de Prueba.</h1>'

@main.route('/eventos', methods=['GET'])
def listar_eventos():
    """
    Retorna una lista de eventos (JSON).
    """
    eventos = Evento.query.all()
    data = [
        {'id': e.id, 'nombre': e.nombre, 'ubicacion': e.ubicacion,
         'fecha_hora': str(e.fecha_hora), 'capacidad': e.capacidad,
         'descripcion': e.descripcion, 'organizador_id': e.organizador_id}
        for e in eventos
    ]
    return jsonify(data), 200

@main.route('/eventos/<int:id>', methods=['GET'])
def listar_un_evento(id):
    """
    Retorna un solo evento por su ID (JSON).
    """
    e = Evento.query.get_or_404(id)
    data = {
        'id': e.id,
        'nombre': e.nombre,
        'ubicacion': e.ubicacion,
        'fecha_hora': str(e.fecha_hora),
        'capacidad': e.capacidad,
        'descripcion': e.descripcion,
        'organizador_id': e.organizador_id
    }
    return jsonify(data), 200

@main.route('/eventos', methods=['POST'])
def crear_evento():
    """
    Crea un evento sin validación.
    Espera JSON con 'nombre', 'ubicacion', 'fecha_hora', 'capacidad', 'descripcion', 'organizador_id'.
    """
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No input data provided'}), 400
    evento = Evento(
        nombre=data.get('nombre'),
        ubicacion=data.get('ubicacion'),
        fecha_hora=datetime.strptime(data.get('fecha_hora'), '%Y-%m-%d %H:%M'),
        capacidad=data.get('capacidad'),
        descripcion=data.get('descripcion'),
        organizador_id=data.get('organizador_id')
    )
    db.session.add(evento)
    db.session.commit()
    return jsonify({'message': 'Evento creado', 'id': evento.id}), 201

@main.route('/eventos/<int:id>', methods=['PUT'])
def actualizar_evento(id):
    """
    Actualiza un evento sin validación de usuario o permisos.
    """
    e = Evento.query.get_or_404(id)
    data = request.get_json()
    e.nombre = data.get('nombre', e.nombre)
    e.ubicacion = data.get('ubicacion', e.ubicacion)
    if data.get('fecha_hora'):
        e.fecha_hora = datetime.strptime(data.get('fecha_hora'), '%Y-%m-%d %H:%M')
    e.capacidad = data.get('capacidad', e.capacidad)
    e.descripcion = data.get('descripcion', e.descripcion)
    db.session.commit()
    return jsonify({'message': 'Evento actualizado', 'id': e.id}), 200

@main.route('/eventos/<int:id>', methods=['DELETE'])
def eliminar_evento(id):
    """
    Elimina un evento sin validación de permisos.
    """
    e = Evento.query.get_or_404(id)
    db.session.delete(e)
    db.session.commit()
    return jsonify({'message': 'Evento eliminado', 'id': e.id}), 200