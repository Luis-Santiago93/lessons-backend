from Entities.entities import escuela_sabatica
from Entities.entities import contenido
from Infrastructure.Repositories.RepositoryBase import RepositoryBase
from sqlalchemy import update


def get_json_config(o):
    def get_content(i):
        return {'id': i.ContenidoID,
                'lessonNumber': str(i.NumeroLeccion),
                'versionCode': i.VersionCodigo,
                'title': i.Titulo,
                'date': i.Fecha,
                'remoteColor': i.Color,
            }
    
    list_contenido=[]
    list_egw=[]
    for content in o.contenido:
        if content.IsVigente==1 and content.IsEGW==2:
            list_contenido.append(content)

        if content.IsVigente==1 and content.IsEGW==1:
            list_egw.append(content)
    
    if o.AlertaApp==1:
        appAlert=True
    else:
        appAlert=False

    if o.AlertaEGW==1:
        egwAlert=True
    else:
        egwAlert=False

    if o.IsPublicado==1:
        publicado=True
    else:
        publicado=False

    if o.ForzarActualizacion==1:
        forzarActualizacion=True
    else:
        forzarActualizacion=False

    if o.GoogleActualizacion==1:
        googleActualizacion=True
    else:
        googleActualizacion=False

    if o.FlexibleActualizacion==1:
        flexActualizacion=True
    else:
        flexActualizacion=False

    return {'id': o.ID,
            'idEs': o.EscuelaSabaticaID,
            'title': o.Titulo,
            'color': o.Color,
            'quarterText': o.TrimestreTexto,
            'quarter': o.Trimestre,
            'latestVersionName': o.UltimaVersionNombre,
            'latestVersionCode': o.UltimaVersionCodigo,
            'forceUpdate': forzarActualizacion,
            'googleUpdate': googleActualizacion,
            'flexibleUpdate': flexActualizacion,
            'helpVideos': o.VideoAyuda,
            'mission': o.Misionero,
            'egwHasAlert': egwAlert,
            'appHasAlert': appAlert ,
            'published': publicado,
            'quarterNumber': o.TrimestreNumero,
            'language': o.Lenguaje,
            'year': o.Ano,
            'adultLessons': [get_content(i) for i in list_contenido],
            'egwLessons': [get_content(i) for i in list_egw]
        }

def get_json(o):
    return {'id': o.ID,
            'idEs': o.EscuelaSabaticaID,
            'title': o.Titulo,
            'color': o.Color,
            'quarterText': o.TrimestreTexto,
            'quarter': o.Trimestre,
            'latestVersionName': o.UltimaVersionNombre,
            'latestVersionCode': o.UltimaVersionCodigo,
            'forceUpdate': o.ForzarActualizacion,
            'googleUpdate': o.GoogleActualizacion,
            'flexibleUpdate': o.FlexibleActualizacion,
            'helpVideos': o.VideoAyuda,
            'mission': o.Misionero,
            'egwHasAlert': o.AlertaEGW,
            'appHasAlert': o.AlertaApp,
            'published': o.IsPublicado,
            'quarterNumber': o.TrimestreNumero,
            'year': o.Ano,
            'language': o.Lenguaje
        }
        
def get_json_all(o):
    def get_content(o):
        return {'id': o.ContenidoID,
                'lessonNumber': o.NumeroLeccion
            }
    return {'id': o.ID,
            'idEs': o.EscuelaSabaticaID,
            'title': o.Titulo,
            'color': o.Color,
            'quarterText': o.TrimestreTexto,
            'quarter': o.Trimestre,
            'latestVersionName': o.UltimaVersionNombre,
            'latestVersionCode': o.UltimaVersionCodigo,
            'forceUpdate': o.ForzarActualizacion,
            'googleUpdate': o.GoogleActualizacion,
            'flexibleUpdate': o.FlexibleActualizacion,
            'helpVideos': o.VideoAyuda,
            'mission': o.Misionero,
            'egwHasAlert': o.AlertaEGW,
            'appHasAlert': o.AlertaApp,
            'published': o.IsPublicado,
            'quarterNumber': o.TrimestreNumero,
            'language': o.Lenguaje,
            'frontPage': o.Portada,
            'year': o.Ano,
            'adultLessons': [get_content(i) for i in o.contenido]
        }

class EscuelaSabatica_Repository(RepositoryBase):
    db = None

    def __init__(self,db):
        super().__init__(db, EntityBase=escuela_sabatica, EntityName='escuela_sabatica')

    def get_all(self,language):
        try:
            query=self.session().query(escuela_sabatica).filter_by(Lenguaje=language,IsVigente = 1).all()
            all_rows = [get_json_all(i) for i in query]
            return all_rows
        except:
            return None
            self.session().rollback()
            raise
        finally:
            self.session().close()

    def get_by_id(self, id):
        try:
            result=self.session().query(escuela_sabatica).filter_by(EscuelaSabaticaID=id, IsVigente = 1).first()
            return get_json_all(result)
            self.session().commit()
        except Exception as e:
            return None
            self.session().rollback()
            raise
        finally:
            self.session().close()
            
    def get_published(self,language):
        try:
            result=self.session().query(escuela_sabatica).filter_by(Lenguaje=language, IsVigente = 1, IsPublicado=1).all()
            all_rows = [get_json_config(i) for i in result]
            return all_rows
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
            query=self.session().query(escuela_sabatica).filter(escuela_sabatica.EscuelaSabaticaID==id, escuela_sabatica.IsVigente == 1).update({'IsVigente': 2})
            self.session().commit()
            return query
        except Exception as e:
            self.session().rollback()
            raise
        finally:
            self.session().close()
            
    def published(self,id,publicado):
        try:
            query=self.session().query(escuela_sabatica).filter(escuela_sabatica.EscuelaSabaticaID==id, escuela_sabatica.IsVigente == 1).update({'IsPublicado': publicado})
            self.session().commit()
            return query
        except Exception as e:
            self.session().rollback()
            raise
        finally:
            self.session().close()

    def insert(self, item):
        return get_json(super().insert(item))