from flask import Flask, Blueprint, request, jsonify, make_response, json, abort
from Domain.EscuelaSabatica_Domain import EscuelaSabatica_Domain
from Entities.entities import escuela_sabatica
from Response.response import *
import datetime
from settings import create_app, ENVIROMMENT_NAME


app = create_app(ENVIROMMENT_NAME)
Context = app.config["CONTEXT_FACTORY"](app, False)

EscuelaSabatica_Controller = Blueprint("EscuelaSabatica_Controller", __name__)
_escuela_sabatica_Domain = EscuelaSabatica_Domain(Context=Context)


def get_from_request(received):
    current_date_and_time = datetime.datetime.now()
    hours = 2
    hours_added = datetime.timedelta(hours = hours)

    if received['idEs'] == 0:
        received['idEs']=None
        
    item = escuela_sabatica(
        EscuelaSabaticaID=received['idEs'] if 'idEs' in received else None,
        ID=3,
        Titulo=received['title'] if 'title' in received else None,
        Color=received['color'] if 'color' in received else None,
        TrimestreTexto=received['quarterText'] if 'quarterText' in received else None,
        Trimestre=received['quarter'] if 'quarter' in received else None,
        TrimestreNumero=received['quarterNumber'] if 'quarterNumber' in received else None,
        UltimaVersionNombre=received['latestVersionName'] if 'latestVersionName' in received else None,
        UltimaVersionCodigo=received['latestVersionCode'] if 'latestVersionCode' in received else None,
        ForzarActualizacion=received['forceUpdate'] if 'forceUpdate' in received else None,
        GoogleActualizacion=received['googleUpdate'] if 'googleUpdate' in received else None,
        FlexibleActualizacion=received['flexibleUpdate'] if 'flexibleUpdate' in received else None,
        VideoAyuda=received['helpVideos'] if 'helpVideos' in received else None,
        Misionero=received['mission'] if 'mission' in received else None,
        Portada=received['frontPage'] if 'frontPage' in received else None,
        Lenguaje=received['language'] if 'language' in received else None,
        AlertaEGW=received['egwHasAlert'] if 'egwHasAlert' in received else None,
        AlertaApp=received['appHasAlert'] if 'appHasAlert' in received else None,
        Ano=received['year'] if 'year' in received else None,
        AplicacionID=0,
        FechaCreacion=current_date_and_time,
        CreadoPor=received['createdBy'] if 'createdBy' in received else None,
        IsVigente=1,
        IsPublicado=received['published'] if 'published' in received else None
    )
    return item


def set_false_vigente(received):
    item = escuela_sabatica(
        EscuelaSabaticaID=received['idEs'] if 'idEs' in received else None
    )
    return item
    
def set_publicado(received):
    item = escuela_sabatica(
        EscuelaSabaticaID=received['idEs'] if 'idEs' in received else None,
        Lenguaje=received['language'] if 'language' in received else None,
        IsPublicado=received['published'] if 'published' in received else None
    )
    return item
    
@EscuelaSabatica_Controller.route("api/v1.0/EscuelaSabatica/config", methods=['GET'])
def get_published():
    language = request.args.get('language',default = 'es')
    return jsonify(
        _escuela_sabatica_Domain.get_published(language)
    )

@EscuelaSabatica_Controller.route("api/v1.0/EscuelaSabatica", methods=['GET'])
def get_all():
    language = request.args.get('language',default = 'es')
    return jsonify(
        _escuela_sabatica_Domain.get_all(language)
    )

@EscuelaSabatica_Controller.route('api/v1.0/EscuelaSabatica/<id>/', methods=['GET'])
def get_by_id(id):
    return jsonify(_escuela_sabatica_Domain.get_by_id(id))

@EscuelaSabatica_Controller.route('api/v1.0/EscuelaSabatica/create', methods=['POST'])
def post_create():
    received = request.json
    es7= get_from_request(received)
    return jsonify(
        _escuela_sabatica_Domain.insert(es7)
    )

@EscuelaSabatica_Controller.route('api/v1.0/EscuelaSabatica/inactive', methods=['PATCH'])
def vigente():
    received = request.json
    if 'idEs' not in received:
        return json_response(success=False, message='Debe proporcionar el identificador')
    item = set_false_vigente(received)
    return jsonify(
        _escuela_sabatica_Domain.vigente(item)
    )

@EscuelaSabatica_Controller.route('api/v1.0/EscuelaSabatica/published', methods=['PATCH'])
def publicado():
    received = request.json
    if 'idEs' not in received:
        return json_response(success=False, message='Debe proporcionar el identificador')
    item = set_publicado(received)
    return jsonify(
        _escuela_sabatica_Domain.publicado(item)
    )

@EscuelaSabatica_Controller.route('api/v1.0/EscuelaSabatica/update', methods=['PUT'])
def update():
    received = request.json
    if 'idEs' not in received:
        return json_response(success=False, message='Debe proporcionar minimo el identificador')
    item = get_from_request(received)
    return jsonify(
        _escuela_sabatica_Domain.update(item)
    )