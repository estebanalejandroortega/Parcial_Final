from src.config.db import DB

class Estudiante:
    def sacar_estudiantes(self):
        cursor = DB.cursor()
        cursor.execute("SELECT * FROM estudiantes")
        estudiantes = cursor.fetchall()
        cursor.close()

        return estudiantes
    
    def crear_estudiante(self, estudiante):
        cursor = DB.cursor()
        consulta = "INSERT INTO estudiantes (nombres,apellidos,celular,correo_electronico,semestre)"
        consulta += "VALUES ('"+estudiante['nombres']+"','"+estudiante['apellidos']+"','"+estudiante['celular']+"','"+estudiante['correo_electronico']+"','"+estudiante['semestre']+"')"
        cursor.execute(consulta)
        cursor.close()
    
    def editar_estudiante(self, estudiante):
        cursor = DB.cursor()
        consulta = "UPDATE estudiantes SET nombres='"+estudiante['nombres']+"',apellidos='"+estudiante['apellidos']+"',celular='"+estudiante['celular']+"',correo_electronico='"+estudiante['correo_electronico']+"',semestre='"+estudiante['semestre']+"' WHERE id="+estudiante['id']
        cursor.execute(consulta)
        cursor.close()
    
    def eliminar_estudiante(self, id):
        cursor = DB.cursor()
        cursor.execute("DELETE FROM estudiantes WHERE id=?", (id,))
        cursor.close()