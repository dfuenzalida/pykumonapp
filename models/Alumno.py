from google.appengine.ext import db

class Alumno(db.Model):
    nombre_completo = db.StringProperty()
    email = db.StringProperty()
    telefono = db.StringProperty()
    colegio = db.StringProperty()

    def __str__(self):
        return self.nombre_completo + "@" + self.colegio

