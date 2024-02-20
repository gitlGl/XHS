#异步网络服务器使用例子，wsgi协议
import uvicorn
class App:
    def __init__(self):
        self.routes = {}
    def route(self, path):
        def decorator(fn):
            self.routes[path] = fn
            return fn
        return decorator

    async def __call__(self, scope, receive, send):
        path = scope['path']
        handler = self.routes.get(path,None)
        if handler is not None:
                await handler(scope, receive, send)
                return
        await send({
            'type': 'http.response.start',
            'status': 404,
            'headers': [(b'content-type', b'text/plain')],
        })
        await send({
            'type': 'http.response.body',
            'body': b'Not Found',
        })

app = App()
@app.route('/')#"/"与该函数的绑定关系会被保存在app中的字典中
async def handle_home(scope, receive, send):
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [(b'content-type', b'text/plain')],
    })
    await send({
        'type': 'http.response.body',
        'body': b'Hello, World!',
    })
if __name__ == '__main__':
    #网络请求到来后uvicorn服务器会调用app()(调用call函数)
    uvicorn.run(app, host='localhost', port=8000)


#bottle使用例子
from bottle import route, run, template
@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)