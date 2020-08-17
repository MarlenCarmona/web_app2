import web 
import app 

import mvc.models.personas as personas

model_personas = personas.Personas()

render=web.template.render('mvc/views/modulos')

class Update1():
    def GET(self, id_usuario):
      try:
        result = model_personas.view(id_usuario)[0]
        #print(result)
        return render.update(result)
      except Exception as e:
        return "Error" + str(e.args)
    def POST(self, id_usuario):
        try:
            form = web.input()
            id_usuario = form.id_usuario
            nombre = form.nombre
            primer_apellido = form.primer_apellido
            segundo_apellido = form.segundo_apellido
            edad = form.edad
            fecha_nac = form.fecha_nac
            genero = form.genero
            estado = form.estado
            result = model_personas.update(id_usuario,nombre,primer_apellido,segundo_apellido,edad,fecha_nac,genero,estado)
            web.seeother('/list')
        except Exception as e:
            print(e)
            return "Error"
            