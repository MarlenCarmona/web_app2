from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')
import web

urls = (
    '/', 'mvc.controllers.modulos.index.Index1',
    '/modulos_delete', 'mvc.controllers.modulos.delete.Delete1',
    '/modulos_insert', 'mvc.controllers.modulos.insert.Insert1',
    '/modulos_update', 'mvc.controllers.modulos.update.Update1',
    '/modulos_view', 'mvc.controllers.modulos.view.View1',
    '/modulos_list', 'mvc.controllers.modulos.list.List1'
)
app = web.application(urls, globals())
if __name__ == "__main__":
    app.run()