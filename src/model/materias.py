from src.config.db import DB

class Materias:
    def sacar_materias(self):
        cursor = DB.cursor()
        cursor.execute("SELECT * FROM espacios_academicos")
        materias = cursor.fetchall()
        cursor.close()

        return materias
    
    def crear_materia(self, materia):
        cursor = DB.cursor()
        consulta = "INSERT INTO espacios_academicos (nombre,semestre)"
        consulta += "VALUES ('"+materia['nombre']+"','"+materia['semestre']+"')"
        cursor.execute(consulta)
        cursor.close()
    
    def editar_materia(self, materia):
        cursor = DB.cursor()
        consulta = "UPDATE espacios_academicos SET nombre='"+materia['nombre']+"',semestre='"+materia['semestre']+"' WHERE id="+materia['id']
        cursor.execute(consulta)
        cursor.close()
    
    def eliminar_materia(self, id):
        cursor = DB.cursor()
        cursor.execute("DELETE FROM espacios_academicos WHERE id=?", (id,))
        cursor.close()