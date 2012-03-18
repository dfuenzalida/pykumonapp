from google.appengine.api import datastore

import models.Alumno

import os
import webapp2

# mover a base_controller
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
        self.render('index.html', values)
        
    def render(self, template_name, template_data):
        # template = self.get_template(template_name)
        template = env.get_template(self.get_template("index"))
        self.response.out.write(template.render(template_data))

    def get_template(self, view_name):
        return os.path.join(os.path.dirname(__file__),'/views/' + view_name + '.html')

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)

