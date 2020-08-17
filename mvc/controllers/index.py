from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')
import web 

render = web.template.render("mvc/views/modulos/")

class Index():
    def GET(self):
        try:
            return render.index() 
        except Exception as e:
            return "Error" + str(e.args)