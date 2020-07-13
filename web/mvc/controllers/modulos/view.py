from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')
import web 

render = web.template.render("mvc/views/modulos/")

class View1():
    def GET(self):
        try:
            return render.view() 
        except Exception as e:
            return "Error" + str(e.args)
    def POST(self):
      try:
        form = web.input()
        print(type(form))
        print(form)
      except Exception as e:
        return "Error" + str(e.args)