from flask import jsonify, request
from src import app
from src.model.estudiantes import Estudiante

@app.route('/estudiantes', methods=['GET'])
def listar_estudiantes():
    modelo = Estudiante()
    estudiantes = modelo.sacar_estudiantes()
    estudiantes2 = []

    for estudiante in estudiantes:
        estudiantes2.append({
            'id': estudiante[0],
            'nombres': estudiante[1],
            'apellidos': estudiante[2],
            'celular': estudiante[3],
            'correo_electronico': estudiante[4],
            'semestre': estudiante[5]
        })

    return jsonify({
        '.mensaje': 'Lista de estudiantes',
        'estudiantes': estudiantes2
    })

@app.route('/estudiantes', methods=['POST'])
def crear_estudiante():
    modelo = Estudiante()

    nombres = request.json['nombres']
    apellidos = request.json['apellidos']
    celular = request.json['celular']
    correo_electronico = request.json['correo_electronico']
    semestre = request.json['semestre']

    estudiante = {
        'nombres': nombres,
        'apellidos': apellidos,
        'celular': celular,
        'correo_electronico': correo_electronico,
        'semestre': semestre
    }

    modelo.crear_estudiante(estudiante)

    return jsonify({
        '.mensaje': 'Se creo un estudiante',
    })

@app.route('/estudiantes/<int:id>', methods=['PUT'])
def editar_estudiante(id):
    modelo = Estudiante()
    
    nombres = request.json['nombres']
    apellidos = request.json['apellidos']
    celular = request.json['celular']
    correo_electronico = request.json['correo_electronico']
    semestre = request.json['semestre']

    estudiante = {
        'id': str(id),
        'nombres': nombres,
        'apellidos': apellidos,
        'celular': celular,
        'correo_electronico': correo_electronico,
        'semestre': semestre
    }

    modelo.editar_estudiante(estudiante)

    return jsonify({
        '.mensaje': 'Se edito un estudiante',
        'estudiantes': estudiante
    })

@app.route('/estudiantes/<int:id>', methods=['DELETE'])
def eliminar_estudiante(id):
    modelo = Estudiante()
    modelo.eliminar_estudiante(id)

    return jsonify({
        '.mensaje': 'Se elimino un estudiante'
    })