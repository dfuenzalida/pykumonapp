from google.appengine.api import datastore
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

from controllers.base_controller import BaseController
from models.Alumno import Alumno

import os

class IndexController(BaseController):
    def get(self):
        alumnos = datastore.Query("Alumno", _namespace=None).Get(100)
        self.render('index', {'alumnos': alumnos, 'numeros': range(10) })
        
        
class AddAlumnoController(BaseController):
    def get(self):
        alumno = Alumno()
        alumno.nombre_completo = self.request.get("nombre_completo")
        alumno.email = self.request.get("email")
        alumno.telefono = self.request.get("telefono")
        alumno.colegio = self.request.get("colegio")
        alumno.put()
        self.redirect("/")

        
application = webapp.WSGIApplication(
    [('/', IndexController),
    ('/add', AddAlumnoController),
    ],
    debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
