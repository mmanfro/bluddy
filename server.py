from waitress import serve
from bluddy.wsgi import application


serve(application, port=8001)