import web 
import app 

import mvc.models.personas as personas

model_personas = personas.Personas()

render=web.template.render('mvc/views/modulos')

class View1():

    def GET(self, id_usuario):
      try:
        result = model_personas.view(id_usuario)[0]
        return render.view(result)
      except Exception as e:
        return "Error" + str(e.args)