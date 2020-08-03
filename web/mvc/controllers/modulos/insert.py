from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')
import web 
import web.models.personas as personas

model_personas = personas.Personas()
render = web.template.render("mvc/views/modulos/")

class Insert1():
    def GET(self):
        try:
            return render.insert() 
        except Exception as e:
            return "Error" + str(e.args)
    def POST(self):
      try:
            form = web.input()
            name = form.name
            primeroa = form.primero
            segundoa = form.segundo
            matricula = form.matricula
            edad = form.edad
            fecha = form.fecha
            genero = form.genero
            estado = form.estado
            model_personas.insert(name,primeroa,segundoa,matricula,edad,fecha,genero,estado)
            web.seeother('/list')
      except Exception as e:
        return "Error" + str(e.args)