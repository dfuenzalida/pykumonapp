from google.appengine.ext.webapp import template

import os
import webapp2

class BaseController(webapp2.RequestHandler):

    def render(self, template_name, template_data):
        self.response.out.write(template.render(self.get_template(template_name), template_data))

    def get_template(self, view_name):
        return os.path.join(os.path.dirname(__file__),'../views/'+view_name+'.html')



