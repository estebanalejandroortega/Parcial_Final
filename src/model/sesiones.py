from src.config.db import DB

class Sesiones:
    def sacar_sesiones(self):
        cursor = DB.cursor()
        cursor.execute("SELECT sesiones.id, espacios_academicos.nombre, espacios_academicos.semestre, sesiones.fecha, sesiones.hora_inicio, sesiones.hora_finalizacion FROM sesiones INNER JOIN espacios_academicos ON espacios_academicos.id=sesiones.id_esp_academico")
        sesiones = cursor.fetchall()
        cursor.close()

        return sesiones
    
    def sacar_sesion(self, id):
        cursor = DB.cursor()
        cursor.execute("SELECT sesiones.id, espacios_academicos.nombre, espacios_academicos.semestre, sesiones.fecha, sesiones.hora_inicio, sesiones.hora_finalizacion FROM sesiones INNER JOIN espacios_academicos ON espacios_academicos.id=sesiones.id_esp_academico WHERE sesiones.id="+id+";")
        sesion = cursor.fetchone()
        cursor.close()

        return sesion
    
    def crear_sesion(self, sesion):
        cursor = DB.cursor()
        consulta = "INSERT INTO sesiones (id_esp_academico,fecha,hora_inicio,hora_finalizacion)"
        consulta += "VALUES ('"+sesion['id_esp_academico']+"','"+sesion['fecha']+"','"+sesion['h_inicio']+"','"+sesion['h_finializacion']+"')"
        cursor.execute(consulta)
        cursor.close()
    
    def editar_sesion(self, sesion):
        cursor = DB.cursor()
        consulta = "UPDATE sesiones SET id_esp_academico='"+sesion['id_esp_academico']+"',fecha='"+sesion['fecha']+"',hora_inicio='"+sesion['h_inicio']+"',hora_finalizacion='"+sesion['h_finializacion']+"' WHERE id="+sesion['id']
        cursor.execute(consulta)
        cursor.close()
    
    def eliminar_sesion(self, id):
        cursor = DB.cursor()
        cursor.execute("DELETE FROM sesiones WHERE id=?", (id,))
        cursor.close()
    
    def asistencia(self, id):
        cursor = DB.cursor()
        cursor.execute("SELECT estudiantes.*, if(sesiones_estudiantes.asistencia=1, 'asistio', 'no asistio') AS 'asistencia' FROM estudiantes LEFT JOIN sesiones_estudiantes ON sesiones_estudiantes.id_estudiante = estudiantes.id AND sesiones_estudiantes.id_sesion="+id)
        estudiantes = cursor.fetchall()
        cursor.close()

        return estudiantes
    
    def editar_asistencia(self, asistencia):
        cursor = DB.cursor()
        cursor.execute("UPDATE sesiones_estudiantes SET asistencia="+asistencia['asistencia']+" WHERE id_sesion="+asistencia['id_sesion']+" AND id_estudiante="+asistencia['id_estudiante'])
        cursor.close()
    
    def asistencia_estudiante(self, id_sesion, id_estudiante):
        cursor = DB.cursor()
        cursor.execute("SELECT estudiantes.*, if(sesiones_estudiantes.asistencia=1, 'asistio', 'no asistio') AS 'asistencia' FROM estudiantes LEFT JOIN sesiones_estudiantes ON sesiones_estudiantes.id_estudiante = estudiantes.id AND sesiones_estudiantes.id_sesion="+id_sesion+" WHERE estudiantes.id="+id_estudiante)
        estudiante = cursor.fetchone()
        cursor.close()

        return estudiante
    
    def crear_asistencia(self, id_sesion, id_estudiante):
        cursor = DB.cursor()
        consulta = "INSERT INTO sesiones_estudiantes (id_sesion, id_estudiante) VALUES ('"+id_sesion+"', '"+id_estudiante+"')"
        cursor.execute(consulta)
        cursor.close()