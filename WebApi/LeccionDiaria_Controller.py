from flask import Flask, Blueprint, request, jsonify, make_response, json, abort
from Domain.LeccionDiaria_Domain import LeccionDiaria_Domain
from Entities.entities import leccion_diaria
from Response.response import *
import datetime
from settings import create_app, ENVIROMMENT_NAME


app = create_app(ENVIROMMENT_NAME)
Context = app.config["CONTEXT_FACTORY"](app, False)

LeccionDiaria_Controller = Blueprint("LeccionDiaria_Controller", __name__)
_leccionDiaria_Domain = LeccionDiaria_Domain(Context=Context)


def get_from_request(received):
    current_date_and_time = datetime.datetime.now()
    hours = 2
    hours_added = datetime.timedelta(hours = hours)

    if received['id'] == 0:
        received['id']=None
        
    item = leccion_diaria(
        LeccionDiariaID=received['id'] if 'id' in received else None,
        ContenidoID=received['idLesson'] if 'idLesson' in received else None,
        NumeroDia=received['idDay'] if 'idDay' in received else None,
        Titulo=received['dayTitle'] if 'dayTitle' in received else None,
        Fecha=received['date'] if 'date' in received else None,
        TextoLeccion=received['lessonText'] if 'lessonText' in received else None,
        FechaCreacion=current_date_and_time,
        CreadoPor=received['createdBy'] if 'createdBy' in received else None,
        IsVigente=1
    )
    return item


def set_false_vigente(received):
    item = leccion_diaria(
        LeccionDiariaID=received['id'] if 'id' in received else None
    )
    return item

@LeccionDiaria_Controller.route("api/v1.0/LeccionDiaria", methods=['GET'])
def get_by_contenido():
    contenido = request.args.get('contenido')
    return jsonify(
        _leccionDiaria_Domain.get_by_contenido(contenido)
    )

@LeccionDiaria_Controller.route('api/v1.0/LeccionDiaria/<id>/', methods=['GET'])
def get_by_id(id):
    return jsonify(_leccionDiaria_Domain.get_by_id(id))

@LeccionDiaria_Controller.route('api/v1.0/LeccionDiaria/create', methods=['POST'])
def post_create():
    received = request.json
    leccion= get_from_request(received)
    return jsonify(
        _leccionDiaria_Domain.insert(leccion)
    )

@LeccionDiaria_Controller.route('api/v1.0/LeccionDiaria/inactive', methods=['PATCH'])
def vigente():
    received = request.json
    if 'id' not in received:
        return json_response(success=False, message='Debe proporcionar el identificador')
    item = set_false_vigente(received)
    return jsonify(
        _leccionDiaria_Domain.vigente(item)
    )

@LeccionDiaria_Controller.route('api/v1.0/LeccionDiaria/update', methods=['PUT'])
def update():
    received = request.json
    if 'id' not in received:
        return json_response(success=False, message='Debe proporcionar minimo el identificador')
    item = get_from_request(received)
    return jsonify(
        _leccionDiaria_Domain.update(item)
    )


