from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')
import web 

render = web.template.render("mvc/views/modulos/")

class List1():
    def GET(self):
        try:
            return render.list() 
        except Exception as e:
            return "Error" + str(e.args)
    def POST(self):
      try:
        form = web.input()
        print(type(form))
        print(form)
      except Exception as e:
        return "Error" + str(e.args)