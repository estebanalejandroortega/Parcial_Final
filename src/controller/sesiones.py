from flask import jsonify, request
from src import app
from src.model.sesiones import Sesiones
from src.model.estudiantes import Estudiante

@app.route('/sesiones', methods=['GET'])
def listar_sesiones():
    modelo = Sesiones()
    sesiones = modelo.sacar_sesiones()
    sesiones2 = []

    for sesion in sesiones:
        fecha = str(sesion[3])
        h_inicio = str(sesion[4])
        h_fin = str(sesion[5])

        sesiones2.append({
            'id': sesion[0],
            'nombre_materia': sesion[1],
            'semestre': sesion[2],
            'fecha': fecha,
            'hora_inicio': h_inicio,
            'hora_finalizacion': h_fin
        })

    return jsonify({
        '.mensaje': 'Lista de Sesiones',
        'sesiones': sesiones2
    })

@app.route('/sesiones', methods=['POST'])
def crear_sesion():
    modelo = Sesiones()

    id_esp_academico = request.json['id_esp_academico']
    fecha = request.json['fecha']
    hora_inicio = request.json['hora_inicio']
    hora_finializacion = request.json['hora_finializacion']

    sesion = {
        'id_esp_academico': str(id_esp_academico),
        'fecha': fecha,
        'h_inicio': hora_inicio,
        'h_finializacion': hora_finializacion
    }

    modelo.crear_sesion(sesion)

    sesiones = modelo.sacar_sesiones()
    modelo2 = Estudiante()
    estudiantes = modelo2.sacar_estudiantes()
    id_sesion = sesiones[len(sesiones)-1][0]

    for estudiante in estudiantes:
        id_estudiante = estudiante[0]
        modelo.crear_asistencia(str(id_sesion), str(id_estudiante))
        

    return jsonify({
        '.mensaje': 'Se creo una nueva sesion'
    })

@app.route('/sesiones/<int:id>', methods=['PUT'])
def editar_sesion(id):
    modelo = Sesiones()

    id_esp_academico = request.json['id_esp_academico']
    fecha = request.json['fecha']
    hora_inicio = request.json['hora_inicio']
    hora_finializacion = request.json['hora_finializacion']

    sesion = {
        'id': str(id),
        'id_esp_academico': str(id_esp_academico),
        'fecha': fecha,
        'h_inicio': hora_inicio,
        'h_finializacion': hora_finializacion
    }

    modelo.editar_sesion(sesion)

    return jsonify({
        '.mensaje': 'Se edito una nueva sesion'
    })

@app.route('/sesiones/<int:id>', methods=['DELETE'])
def eliminar_sesion(id):
    modelo = Sesiones()
    modelo.eliminar_sesion(id)

    return jsonify({
        '.mensaje': 'Se elimino una sesion'
    })