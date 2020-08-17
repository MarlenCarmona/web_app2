import web 
import app 
import mvc.models.personas as personas

model_personas = personas.Personas()
render=web.template.render('mvc/views/modulos')

class Insert():

    def GET(self):
      try:
        return render.insert()
      except Exception as e:
        return "Error" + str(e.args)
    def POST(self):
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