from google.appengine.ext import db
import jinja2
import os
import webapp2

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Alumno(db.Model):
    nombre_completo = db.StringProperty()
    email = db.StringProperty()
    telefono = db.StringProperty()
    colegio = db.StringProperty()

    def __str__(self):
        return self.nombre_completo + "@" + self.colegio

class MainPage(webapp2.RequestHandler):
    def get(self):
        alumnos = Alumno.all()

        values = {
            'alumnos': alumnos,
        }

        template = env.get_template("index.html")
        self.response.out.write(template.render(values))

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)

