from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    return Response('Hello World!')

def bye_world(request):
    return Response('Bye!')

config = Configurator()

config.add_route('hello', '/')
config.add_view(hello_world, route_name='hello')

config.add_route('newHandler', '/bye')
config.add_view(bye_world, route_name='newHandler')

app = config.make_wsgi_app()

if __name__ == '__main__':
    server = make_server('127.0.0.1', 8080, app)
    server.serve_forever()

