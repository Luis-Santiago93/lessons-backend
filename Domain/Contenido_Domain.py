from Domain.DomainBase import DomainBase
from Entities.entities import contenido
from Response.response import *
from Domain.Complements.Utils import *

class Contenido_Domain(DomainBase):
    _Contenido_Repository = None

    def __init__(self, Context):
        self._Contenido_Repository = Context.ContextContenido_Repository
        super().__init__()

    def get_by_es(self,id,tipo):
        try:
            all_rows =self._Contenido_Repository.get_by_es(id,tipo)
            if not all_rows:
                return json_response(success=False, message='Consulta sin datos')
            return json_response(data=all_rows, message='Consulta con éxito', success=True)
        except Exception as e:
            return json_error_response(e)

    def get_by_lesson(self,id,lesson):
        try:
            all_rows =self._Contenido_Repository.get_by_lesson(id,lesson)
            if not all_rows:
                return json_response(success=False, message='Consulta sin datos')
            return json_response(data=all_rows, message='Consulta con éxito', success=True)
        except Exception as e:
            return json_error_response(e)

    def get_by_egw(self,id,lesson):
        try:
            all_rows =self._Contenido_Repository.get_by_egw(id,lesson)
            if not all_rows:
                return json_response(success=False, message='Consulta sin datos')
            return json_response(data=all_rows, message='Consulta con éxito', success=True)
        except Exception as e:
            return json_error_response(e)

    def get_by_id(self, id):
        try:
            i = self._Contenido_Repository.get_by_id(id)
            if i is None:
                return json_response(success=False, message='Elemento no encontrado')
            return json_response(data=i, success=True, message='Consulta con éxito')
        except Exception as e:
            return json_error_response(e)

    def insert(self, item: contenido):
        try:
            all_rows = self._Contenido_Repository.insert(item)
            if not all_rows:
                return json_response(success=False, message='Hubo un error al insertar')
            return json_response(data=all_rows, success=True, message='Elemento insertado con éxito')
        except Exception as e:
            return json_error_response(e)

    def vigente(self, item):
        try:
            i = self._Contenido_Repository.get_by_id(item.ContenidoID)
            if i is None:
                return json_response(success=True, message='Elemento no encontrado')
            if self._Contenido_Repository.disable(item.ContenidoID):
                return json_response(success=True, message='El elemento fue actualizado con éxito')
        except Exception as e:
            return json_error_response(e)
            
    def update(self, item):
        try:
            i = self._Contenido_Repository.get_by_id(item.ContenidoID)
            if i is None:
                return json_response(success=True, message='Elemento no encontrado')
            if self._Contenido_Repository.update(serialize(item), item.ContenidoID):
                return json_response(success=True, message='El elemento fue actualizado con éxito')
        except Exception as e:
            return json_error_response(e) 

    def delete(self, id):
        pass