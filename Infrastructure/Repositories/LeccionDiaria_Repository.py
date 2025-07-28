from Entities.entities import leccion_diaria
from Infrastructure.Repositories.RepositoryBase import RepositoryBase
from sqlalchemy import update

def get_json(o):
    return {'id': o.LeccionDiariaID,
            'idLesson': o.ContenidoID,
            'idDay': o.NumeroDia,
            'dayTitle': o.Titulo,
            'date': o.Fecha,
            'lessonText': o.TextoLeccion
        }
        
class LeccionDiaria_Repository(RepositoryBase):
    db = None

    def __init__(self,db):
        super().__init__(db, EntityBase=leccion_diaria, EntityName='leccion_diaria')

    def get_by_contenido(self,id):
        try:
            query=self.session().query(leccion_diaria).filter_by(ContenidoID=int(id),IsVigente = 1).all()
            all_rows = [get_json(i) for i in query]
            return all_rows
        except:
            return None
            self.session().rollback()
            raise
        finally:
            self.session().close()

    def get_by_id(self, id):
        try:
            result=self.session().query(leccion_diaria).filter_by(LeccionDiariaID=id, IsVigente = 1).first()
            return get_json(result)
            self.session().commit()
        except Exception as e:
            return None
            self.session().rollback()
            raise
        finally:
            self.session().close()
            
    def insert_multiple(self, item):
        try:
            self.session().add_all(item)
            self.session().commit()
            all_rows = [get_json(i) for i in item]
            return all_rows
        except Exception as e:
            print(e)
            return None
            self.session().rollback()
            raise
        finally:
            self.session().close()

    def disable(self,id):
        try:
            query=self.session().query(leccion_diaria).filter(leccion_diaria.LeccionDiariaID==id, leccion_diaria.IsVigente == 1).update({'IsVigente': 2})
            self.session().commit()
            return query
        except Exception as e:
            self.session().rollback()
            raise
        finally:
            self.session().close()
            
    def insert(self, item):
        return get_json(super().insert(item))