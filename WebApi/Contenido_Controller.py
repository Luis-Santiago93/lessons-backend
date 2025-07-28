from flask import Flask, Blueprint, request, jsonify, make_response, json, abort
from Domain.Contenido_Domain import Contenido_Domain
from Entities.entities import contenido
from Response.response import *
import datetime
from settings import create_app, ENVIROMMENT_NAME


app = create_app(ENVIROMMENT_NAME)
Context = app.config["CONTEXT_FACTORY"](app, False)

Contenido_Controller = Blueprint("Contenido_Controller", __name__)
_contenido_Domain = Contenido_Domain(Context=Context)


def get_from_request(received):
    current_date_and_time = datetime.datetime.now()
    hours = 2
    hours_added = datetime.timedelta(hours = hours)

    if received['id'] == 0:
        received['id']=None
        
    item = contenido(
        ContenidoID=received['id'] if 'id' in received else None,
        EscuelaSabaticaID=received['idEs'] if 'idEs' in received else None,
        Titulo=received['title'] if 'title' in received else None,
        Versiculo=received['verse'] if 'verse' in received else None,
        Color=received['remoteColor'] if 'remoteColor' in received else None,
        IsEGW=received['egw'] if 'egw' in received else None,
        Fecha=received['date'] if 'date' in received else None,
        VersionCodigo=received['versionCode'] if 'versionCode' in received else None,
        NumeroLeccion=received['lessonNumber'] if 'lessonNumber' in received else None,
        FechaCreacion=current_date_and_time,
        CreadoPor=received['createdBy'] if 'createdBy' in received else None,
        IsVigente=1
    )
    return item


def set_false_vigente(received):
    item = contenido(
        ContenidoID=received['id'] if 'id' in received else None
    )
    return item

@Contenido_Controller.route("api/v1.0/Contenido", methods=['GET'])
def get_by_es():
    es7 = request.args.get('es7')
    tipo = request.args.get('tipo')
    return jsonify(
        _contenido_Domain.get_by_es(es7,tipo)
    )

@Contenido_Controller.route("api/v1.0/Contenido/lessons", methods=['GET'])
def get_by_lesson():
    es7 = request.args.get('es7')
    lesson = request.args.get('lesson')
    return jsonify(
        _contenido_Domain.get_by_lesson(es7,lesson)
    )

@Contenido_Controller.route("api/v1.0/Contenido/egw", methods=['GET'])
def get_by_egw():
    es7 = request.args.get('es7')
    lesson = request.args.get('lesson')
    return jsonify(
        _contenido_Domain.get_by_egw(es7,lesson)
    )

@Contenido_Controller.route('api/v1.0/Contenido/<id>/', methods=['GET'])
def get_by_id(id):
    return jsonify(_contenido_Domain.get_by_id(id))

@Contenido_Controller.route('api/v1.0/Contenido/create', methods=['POST'])
def post_create():
    received = request.json
    es7= get_from_request(received)
    return jsonify(
        _contenido_Domain.insert(es7)
    )

@Contenido_Controller.route('api/v1.0/Contenido/inactive', methods=['PATCH'])
def vigente():
    received = request.json
    if 'id' not in received:
        return json_response(success=False, message='Debe proporcionar el identificador')
    item = set_false_vigente(received)
    return jsonify(
        _contenido_Domain.vigente(item)
    )

@Contenido_Controller.route('api/v1.0/Contenido/update', methods=['PUT'])
def update():
    received = request.json
    if 'id' not in received:
        return json_response(success=False, message='Debe proporcionar minimo el identificador')
    item = get_from_request(received)
    return jsonify(
        _contenido_Domain.update(item)
    )