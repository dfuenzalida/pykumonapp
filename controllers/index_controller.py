from google.appengine.api import datastore

from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

import models.Alumno

import jinja2
import os
import webapp2

class IndexController(webapp2.RequestHandler):
    def get(self):
        alumnos = datastore.Query("Alumno", _namespace=None).Get(100)
        self.render('index', {'alumnos': alumnos})
        
    def render(self, template_name, template_data):
        self.response.out.write(template.render(self.get_template(template_name), template_data))

    def get_template(self, view_name):
        return os.path.join(os.path.dirname(__file__),'../views/'+view_name+'.html')

application = webapp2.WSGIApplication([('/lista', IndexController)],
                              debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
