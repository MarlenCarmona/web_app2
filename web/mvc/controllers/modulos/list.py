import web 
import app 
import mvc.models.personas as personas

model_personas = personas.Personas()


render=web.template.render('mvc/views/modulos')

class List1():

    def GET(self):
      try:
        result = model_personas.select()
        return render.list(result)
      except Exception as e:
        return "Error" + str(e.args)