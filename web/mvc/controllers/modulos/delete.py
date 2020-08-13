from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')
import web 

import web.models.personas as personas
model_personas = personas.Personas()

render = web.template.render("mvc/views/modulos/")

class Delete1():
    def GET(self, matricula):
      try:
        result = model_personas.view(matricula)[0]
        return render.delete(result)
      except Exception as e:
        return "Error" + str(e.args)
    def POST(self, matricula):
      try:
        form = web.input()
        matricula = form['matricula']
        result = model_personas.delete(matricula)
        web.seeother('/list')
      except Exception as e:
        print(e)
        return "Error"