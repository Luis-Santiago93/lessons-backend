from Entities.entities import contenido, escuela_sabatica
from Infrastructure.Repositories.RepositoryBase import RepositoryBase
from sqlalchemy import update

def get_json(o):
    return {'id': o.ContenidoID,
            'idEs': o.EscuelaSabaticaID,
            'title': o.Titulo,
            'remoteColor': o.Color,
            'egw': o.IsEGW,
            'date': o.Fecha,
            'versionCode': o.VersionCodigo,
            'lessonNumber': o.NumeroLeccion,
            'verse': o.Versiculo
        }

def get_json_lesson(o):
    def convert_id_english(x):
        if x <10:
            new_id=str('70')+str(x)
        else:
            new_id=str('7')+str(x)
        return int(new_id)
    
    list_lesson = []

    for content in o.leccion_diaria:
        if content.IsVigente == 1:
            list_lesson.append(content)

    def get_day(i):
        list_verses = [{"verse":"","verseText":""}]
        return {'dayTitle': i.Titulo,
                'verses': list_verses,
                'date':i.Fecha,
                'lessonText':i.TextoLeccion,
                'idDay':i.NumeroDia,
                'id':int(str(i.contenido.NumeroLeccion)+str(i.NumeroDia)),
                'idLesson':i.contenido.NumeroLeccion
            }
    
    return {'id': convert_id_english(o.NumeroLeccion) if o.escuela_sabatica.Lenguaje=='en' else o.NumeroLeccion,
            'idEs': o.EscuelaSabaticaID,
            'title': o.Titulo,
            'color': o.Color,
            'weekDate': o.Fecha,
            'versionCode': o.VersionCodigo,
            'lessonNumber': o.NumeroLeccion,
            'verse': o.Versiculo,
            "lessonType": "A",
            "language": o.escuela_sabatica.Lenguaje,
            'quarter': o.escuela_sabatica.Trimestre,
            'lessonDays': [get_day(i) for i in list_lesson]
        }

def get_json_egw(o):
    
    list_lesson = []
    trimestre=o.escuela_sabatica.Trimestre

    for content in o.leccion_diaria:
        if content.IsVigente == 1:
            list_lesson.append(content)

    def get_day(i):
        list_verses = [{"verse":"","verseText":""}]
        return {'dayTitle': i.Titulo,
                'verses': list_verses,
                'date':i.Fecha,
                'day':'-',
                'content':i.TextoLeccion,
                'idDay':i.NumeroDia,
                'id':int(str(i.contenido.NumeroLeccion)+str(i.NumeroDia)),
                'idLesson':i.contenido.NumeroLeccion,
                'quarterCode': trimestre
            }
    
    return {'id': o.NumeroLeccion,
            'idEs': o.EscuelaSabaticaID,
            'title': o.Titulo,
            'color': o.Color,
            'weekDate': o.Fecha,
            'versionCode': o.VersionCodigo,
            'lessonNumber': o.NumeroLeccion,
            'verse': o.Versiculo,
            "lessonType": "A",
            "language": o.escuela_sabatica.Lenguaje,
            'quarter': o.escuela_sabatica.Trimestre,
            'finalDate':'-',
            'studies': [get_day(i) for i in list_lesson]
        }
        
class Contenido_Repository(RepositoryBase):
    db = None

    def __init__(self,db):
        super().__init__(db, EntityBase=contenido, EntityName='contenido')

    def get_by_es(self,id,tipo):
        try:
            query=self.session().query(contenido).filter_by(EscuelaSabaticaID=id,IsEGW=tipo,IsVigente = 1).all()
            all_rows = [get_json(i) for i in query]
            return all_rows
        except:
            return None
            self.session().rollback()
            raise
        finally:
            self.session().close()

    def get_by_lesson(self,id,lesson):
        try:
            query=self.session().query(contenido).filter(contenido.EscuelaSabaticaID==id,contenido.NumeroLeccion==lesson,contenido.IsVigente == 1,contenido.IsEGW==2).all()
            all_rows = [get_json_lesson(i) for i in query]
            return all_rows
        except:
            return None
            self.session().rollback()
            raise
        finally:
            self.session().close()

    def get_by_egw(self,id,lesson):
        try:
            query=self.session().query(contenido).filter(contenido.EscuelaSabaticaID==id,contenido.NumeroLeccion==lesson,contenido.IsVigente == 1,contenido.IsEGW==1).all()
            all_rows = [get_json_egw(i) for i in query]
            return all_rows
        except:
            return None
            self.session().rollback()
            raise
        finally:
            self.session().close()

    def get_by_id(self, id):
        try:
            result=self.session().query(contenido).filter_by(ContenidoID=id, IsVigente = 1).first()
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
            query=self.session().query(contenido).filter(contenido.ContenidoID==id, contenido.IsVigente == 1).update({'IsVigente': 2})
            self.session().commit()
            return query
        except Exception as e:
            self.session().rollback()
            raise
        finally:
            self.session().close()
            
    def insert(self, item):
        return get_json(super().insert(item))