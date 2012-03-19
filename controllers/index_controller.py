from google.appengine.api import datastore
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

from controllers.base_controller import BaseController
import models.Alumno

import os
import webapp2

class IndexController(BaseController):
    def get(self):
        alumnos = datastore.Query("Alumno", _namespace=None).Get(100)
        self.render('index', {'alumnos': alumnos, 'numeros': range(10) })
        
application = webapp2.WSGIApplication([('/', IndexController)],
                              debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
