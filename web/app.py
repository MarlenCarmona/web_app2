from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')
import web

urls = (
    '/', 'mvc.controllers.index.Index1',
    '/delete', 'mvc.controllers.delete.Delete1',
    '/insert', 'mvc.controllers.insert.Insert1',
    '/update', 'mvc.controllers.update.Update1',
    '/view', 'mvc.controllers.view.View1',
    '/list', 'mvc.controllers.list.List1'
)
app = web.application(urls, globals())
if __name__ == "__main__":
    app.run()