from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')
import web 
import web.mvc.models.personas as personas

model_personas = personas.Personas()
render = web.template.render("mvc/views/modulos/")

class View1():
    def GET(self, matricula):
      try:
        result = model_personas.view(matricula)[0]
        return render.view(result)
      except Exception as e:
        return "Error" + str(e.args)