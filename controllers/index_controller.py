from google.appengine.api import datastore

import models.Alumno

import jinja2
import os
import webapp2

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
    def get(self):
        # alumnos = Alumno.all()
        alumnos = datastore.Query("Alumno", _namespace=None).Get(100)

        values = {
            'alumnos': alumnos,
        }

        # template = env.get_template("../index.html")
        # self.response.out.write(template.render(values))
        # render(self, 'index.html', values)
        
    def render(self, template_name, template_data):
        self.response.out.write(template.render(get_template(template_name), template_data))

    def get_template(view_name):
        return os.path.join(os.path.dirname(__file__),'../'+view_name+'.html')

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)

