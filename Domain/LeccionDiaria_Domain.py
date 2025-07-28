from Domain.DomainBase import DomainBase
from Entities.entities import leccion_diaria
from Response.response import *
from Domain.Complements.Utils import *

class LeccionDiaria_Domain(DomainBase):
    _LeccionDiaria_Repository = None

    def __init__(self, Context):
        self._LeccionDiaria_Repository = Context.ContextLeccionDiaria_Repository
        super().__init__()

    def get_by_contenido(self,id):
        try:
            all_rows =self._LeccionDiaria_Repository.get_by_contenido(id)
            if not all_rows:
                return json_response(success=False, message='Consulta sin datos')
            return json_response(data=all_rows, message='Consulta con éxito', success=True)
        except Exception as e:
            return json_error_response(e)

    def get_by_id(self, id):
        try:
            i = self._LeccionDiaria_Repository.get_by_id(id)
            if i is None:
                return json_response(success=False, message='Elemento no encontrado')
            return json_response(data=i, success=True, message='Consulta con éxito')
        except Exception as e:
            return json_error_response(e)

    def insert(self, item: leccion_diaria):
        try:
            all_rows = self._LeccionDiaria_Repository.insert(item)
            if not all_rows:
                return json_response(success=False, message='Hubo un error al insertar')
            return json_response(data=all_rows, success=True, message='Elemento insertado con éxito')
        except Exception as e:
            return json_error_response(e)

    def vigente(self, item):
        try:
            i = self._LeccionDiaria_Repository.get_by_id(item.LeccionDiariaID)
            if i is None:
                return json_response(success=True, message='Elemento no encontrado')
            if self._LeccionDiaria_Repository.disable(item.LeccionDiariaID):
                return json_response(success=True, message='El elemento fue actualizado con éxito')
        except Exception as e:
            return json_error_response(e)
            
    def update(self, item):
        try:
            i = self._LeccionDiaria_Repository.get_by_id(item.LeccionDiariaID)
            if i is None:
                return json_response(success=True, message='Elemento no encontrado')
            if self._LeccionDiaria_Repository.update(serialize(item), item.LeccionDiariaID):
                return json_response(success=True, message='El elemento fue actualizado con éxito')
        except Exception as e:
            return json_error_response(e) 

    def delete(self, id):
        pass
