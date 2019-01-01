from gevent.pywsgi import WSGIServer
from app import create_app


http_server = WSGIServer(('0.0.0.0', 5000), create_app())
print('Starting Server')
http_server.serve_forever()
