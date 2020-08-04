from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')
import web

urls = (
    '/', 'mvc.controllers.modulos.index.Index1',
    '/delete', 'mvc.controllers.modulos.delete.Delete1',
    '/insert', 'mvc.controllers.modulos.insert.Insert',
    '/update', 'mvc.controllers.modulos.update.Update1',
    '/view/(.*)', 'mvc.controllers.modulos.view.View1',
    '/list', 'mvc.controllers.modulos.list.List1'
)
app = web.application(urls, globals())
if __name__ == "__main__":
    app.run()