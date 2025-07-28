class SQLContext(object):
    ContextEscuelaSabatica_Repository = None
    ContextContenido_Repository = None
    ContextLeccionDiaria_Repository = None

    def __init__(self,app,band=True):
        from flask_sqlalchemy import SQLAlchemy
        from Infrastructure.Mapping import mappings
        from Infrastructure.Repositories.EscuelaSabatica_Repository import EscuelaSabatica_Repository
        from Infrastructure.Repositories.Contenido_Repository import Contenido_Repository
        from Infrastructure.Repositories.LeccionDiaria_Repository import LeccionDiaria_Repository

        db = SQLAlchemy(app)
        if band:
            mappings.init(db)

        self.db = db

        self.ContextEscuelaSabatica_Repository = EscuelaSabatica_Repository(db) 
        self.ContextContenido_Repository = Contenido_Repository (db)
        self.ContextLeccionDiaria_Repository = LeccionDiaria_Repository (db)

    def setup(self):
        self.db.create_all()