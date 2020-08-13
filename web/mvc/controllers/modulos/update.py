from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')
import web 

import web.models.personas as personas
model_personas = personas.Personas()

render = web.template.render("mvc/views/modulos/")

class Update1():
    def GET(self, matricula):
      try:
        result = model_personas.view(matricula)[0]
        return render.update(result)
      except Exception as e:
        return "Error" + str(e.args)
    def POST(self, matricula):
        try:
            form = web.input()
            id_usuario = form.id_usuario
            nombre = form.nombre
            primerapellido = form.primerapellido
            segundoapellido = form.segundoapellido
            edad = form.edad
            fechanacimiento = form.fechanacimiento
            genero = form.genero
            estado = form.estado
            model_personas.insert(id_usuario,nombre,primerapellido,segundoapellido,edad,fechanacimiento,genero,estado)
            web.seeother('/list')
        except Exception as e:
            print(e)
            return render.insert()