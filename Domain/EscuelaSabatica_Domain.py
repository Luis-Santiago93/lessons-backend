from Domain.DomainBase import DomainBase
from Entities.entities import escuela_sabatica
from Response.response import *
from Domain.Complements.Utils import *

class EscuelaSabatica_Domain(DomainBase):
    _EscuelaSabatica_Repository = None

    def __init__(self, Context):
        self._EscuelaSabatica_Repository = Context.ContextEscuelaSabatica_Repository
        super().__init__()

    def get_all(self,language):
        try:
            all_rows =self._EscuelaSabatica_Repository.get_all(language)
            if not all_rows:
                return json_response(success=False, message='Consulta sin datos')
            return json_response(data=all_rows, message='Consulta con éxito', success=True)
        except Exception as e:
            return json_error_response(e)

    def get_by_id(self, id):
        try:
            i = self._EscuelaSabatica_Repository.get_by_id(id)
            if i is None:
                return json_response(success=False, message='Elemento no encontrado')
            return json_response(data=i, success=True, message='Consulta con éxito')
        except Exception as e:
            return json_error_response(e)

    def insert(self, item: escuela_sabatica):
        try:
            all_rows = self._EscuelaSabatica_Repository.insert(item)
            if not all_rows:
                return json_response(success=False, message='Hubo un error al insertar')
            return json_response(data=all_rows, success=True, message='Elemento insertado con éxito')
        except Exception as e:
            return json_error_response(e)

    def vigente(self, item):
        try:
            i = self._EscuelaSabatica_Repository.get_by_id(item.EscuelaSabaticaID)
            if i is None:
                return json_response(success=True, message='Elemento no encontrado')
            if self._EscuelaSabatica_Repository.disable(item.EscuelaSabaticaID):
                return json_response(success=True, message='El elemento fue actualizado con éxito')
        except Exception as e:
            return json_error_response(e)
            
    def publicado(self, item):
        try:
            if item.IsPublicado==1:
                i = self._EscuelaSabatica_Repository.get_published(item.Lenguaje)
                if not i:
                    if self._EscuelaSabatica_Repository.published(item.EscuelaSabaticaID,item.IsPublicado):
                        return json_response(success=True, message='Publicado con éxito')
                else:
                    return json_response(data=i, success=False, message='Actualmente existe publicado una lección')
            else:
                if self._EscuelaSabatica_Repository.published(item.EscuelaSabaticaID,item.IsPublicado):
                    return json_response(success=True, message='Actualizado con éxito')
        except Exception as e:
            return json_error_response(e)

    def get_published(self, language):
        try:
            all_rows =self._EscuelaSabatica_Repository.get_published(language)
            if not all_rows:
                return json_response(success=False, message='Consulta sin datos')
            return json_response(data=all_rows, message='Consulta con éxito', success=True)
        except Exception as e:
            return json_error_response(e)

    def update(self, item):
        try:
            i = self._EscuelaSabatica_Repository.get_by_id(item.EscuelaSabaticaID)
            if i is None:
                return json_response(success=True, message='Elemento no encontrado')
            if self._EscuelaSabatica_Repository.update(serialize(item), item.EscuelaSabaticaID):
                return json_response(success=True, message='El elemento fue actualizado con éxito')
        except Exception as e:
            return json_error_response(e) 

    def delete(self, id):
        pass
