from flask import jsonify, request
from src import app
from src.model.materias import Materias

@app.route('/materias', methods=['GET'])
def listar_materias():
    modelo = Materias()
    materias = modelo.sacar_materias()
    materias2 = []

    for materia in materias:
        materias2.append({
            'id': materia[0],
            'nombre': materia[1],
            'semestre': materia[2]
        })

    return jsonify({
        '.mensaje': 'Lista de materias',
        'materias': materias2
    })

@app.route('/materias', methods=['POST'])
def crear_materia():
    modelo = Materias()

    nombre = request.json['nombre']
    semestre = request.json['semestre']

    materia = {
        'nombre': nombre,
        'semestre': semestre
    }

    modelo.crear_materia(materia)

    return jsonify({
        '.mensaje': 'Se creo una nueva materia.',
    })

@app.route('/materias/<int:id>', methods=['PUT'])
def editar_materia(id):
    modelo = Materias()

    nombre = request.json['nombre']
    semestre = request.json['semestre']

    materia = {
        'id': str(id),
        'nombre': nombre,
        'semestre': semestre
    }

    modelo.editar_materia(materia)

    return jsonify({
        '.mensaje': 'Se edito una materia',
        'materia': materia
    })

@app.route('/materias/<int:id>', methods=['DELETE'])
def eliminar_materia(id):
    modelo = Materias()
    modelo.eliminar_materia(id)

    return jsonify({
        '.mensaje': 'Se elimino una materia'
    })