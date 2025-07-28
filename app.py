from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from settings import create_app, ENVIROMMENT_NAME
from flask import Flask, redirect
from Response.response import *


from WebApi.EscuelaSabatica_Controller import EscuelaSabatica_Controller
from WebApi.Contenido_Controller import Contenido_Controller
from WebApi.LeccionDiaria_Controller import LeccionDiaria_Controller

app = create_app(ENVIROMMENT_NAME)
db = SQLAlchemy(app)

Context = app.config["CONTEXT_FACTORY"](app)
Context.setup()

cors = CORS(app)


app.register_blueprint(EscuelaSabatica_Controller, url_prefix="")
app.register_blueprint(Contenido_Controller, url_prefix="")
app.register_blueprint(LeccionDiaria_Controller, url_prefix="")

SWAGGER_URL = '/api'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "ES7-WebServices"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run()