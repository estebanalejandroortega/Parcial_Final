from flask import jsonify, request
from src import app
from src.model.sesiones import Sesiones

@app.route('/asistencias/<int:id>', methods=['GET'])
def asistencia(id):
    modelo = Sesiones()
    sesion = modelo.sacar_sesion(str(id))
    sesion2 = {
        'id': sesion[0],
        'materia': sesion[1],
        'semestre': sesion[2],
        'fecha': str(sesion[3]),
        'hora_inicio': str(sesion[3]),
        'hora_finalizacion': str(sesion[3])
    }
    estudiantes = modelo.asistencia(str(id))
    estudiantes2 = []

    for estudiante in estudiantes:
        estudiantes2.append({
            'id': estudiante[0],
            'nombres': estudiante[1],
            'apellidos': estudiante[2],
            'celular': estudiante[3],
            'correo_electronico': estudiante[4],
            'semestre': estudiante[5],
            'asistencia': estudiante[6]
        })

    return jsonify({
        '.mensaje': 'Lista de asistencia',
        '.sesion': sesion2,
        'estudiantes': estudiantes2
    })

@app.route('/asistencias/<int:id_sesion>/<int:id_estu>', methods=['PUT'])
def editar_asistencia(id_estu, id_sesion):
    model = Sesiones()
    asistencia = request.json['asistencia']

    asistencia = {
        'id_sesion': str(id_sesion),
        'id_estudiante': str(id_estu),
        'asistencia': str(asistencia)   
    }
    model.editar_asistencia(asistencia)
    estudiante = model.asistencia_estudiante(str(id_sesion), str(id_estu))
    estudiante2 = {
        'id': estudiante[0],
        'nombres': estudiante[1],
        'apellidos': estudiante[2],
        'celular': estudiante[3],
        'correo_electronico': estudiante[4],
        'semestre': estudiante[5],
        'asistencia': estudiante[6]
    }

    return jsonify({
        '.mensaje': 'Se modifico la asistencia',
        'estudiante': estudiante2
    })