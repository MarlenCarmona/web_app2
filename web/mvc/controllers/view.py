from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')
import web 

render = web.template.render("mvc/views/")

class View1():
    def GET(self):
        try:
            return render.view() 
        except Exception as e:
            return "Error" + str(e.args)