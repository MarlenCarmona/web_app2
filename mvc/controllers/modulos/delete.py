from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')
import web 

import mvc.models.personas as personas
model_personas = personas.Personas()

render = web.template.render("mvc/views/modulos/")

class Delete1():
    def GET(self, id_usuario):
      try:
        result = model_personas.view(id_usuario)[0]
        return render.delete(result)
      except Exception as e:
        return "Error" + str(e.args)
    def POST(self, id_usuario):
      try:
        form = web.input()
        id_usuario = form.id_usuario
        result = model_personas.delete(id_usuario)
        web.seeother('/list')
      except Exception as e:
        print(e)
        return "Error"