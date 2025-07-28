from sqlalchemy import Boolean, CHAR, Column, Date, DateTime, Float, ForeignKey, Integer, Numeric, String, Text, text, JSON, and_
from sqlalchemy.orm import mapper, relationship
from sqlalchemy.sql import func
from Entities.entities import *

def init(db):
#------------------------------------------ Mapping ---------------------------------------------#
    escuela_sabatica_mapping = db.Table('escuela_sabatica',
        db.Column('EscuelaSabaticaID', Integer, primary_key=True,autoincrement=True),
        db.Column('ID', Integer),
        db.Column('Titulo', Text()),
        db.Column('Color', String(255)),
        db.Column('TrimestreTexto', String(255)),
        db.Column('Trimestre', String(255)),
        db.Column('TrimestreNumero', Integer),
        db.Column('UltimaVersionNombre', String(255)),
        db.Column('UltimaVersionCodigo', Integer),
        db.Column('ForzarActualizacion', Integer),
        db.Column('GoogleActualizacion', Integer),
        db.Column('FlexibleActualizacion', Integer),
        db.Column('VideoAyuda', Text()),
        db.Column('Misionero', Text()),
        db.Column('Portada', Text()),
        db.Column('Lenguaje', String(255)),
        db.Column('AplicacionID', Integer),
        db.Column('Ano', Integer),
        db.Column('FechaCreacion', DateTime),
        db.Column('CreadoPor', String(255)),
        db.Column('FechaModificacion', DateTime),
        db.Column('ModificadoPor', String(255)),
        db.Column('AlertaEGW', Integer),
        db.Column('AlertaApp', Integer),
        db.Column('IsVigente', Integer),
        db.Column('IsPublicado', Integer)
    )
    
    contenido_mapping = db.Table('contenido',
        db.Column('ContenidoID', Integer, primary_key=True,autoincrement=True),
        db.Column('EscuelaSabaticaID', Integer,ForeignKey("escuela_sabatica.EscuelaSabaticaID", onupdate="CASCADE", ondelete="CASCADE"), nullable=True),
        db.Column('Titulo', Text()),
        db.Column('Versiculo', Text()),
        db.Column('NumeroLeccion', Integer),
        db.Column('VersionCodigo', Integer),
        db.Column('Fecha', String(255)),
        db.Column('Color', String(255)),
        db.Column('IsEGW', Integer),
        db.Column('FechaCreacion', DateTime),
        db.Column('CreadoPor', String(255)),
        db.Column('FechaModificacion', DateTime),
        db.Column('ModificadoPor', String(255)),
        db.Column('IsVigente', Integer)
    )
    
    leccion_diaria_mapping = db.Table('leccion_diaria',
        db.Column('LeccionDiariaID', Integer, primary_key=True,autoincrement=True),
        db.Column('ContenidoID', Integer,ForeignKey("contenido.ContenidoID", onupdate="CASCADE", ondelete="CASCADE"), nullable=True),
        db.Column('Titulo', Text()),
        db.Column('NumeroDia', Integer),
        db.Column('TextoLeccion', Text()),
        db.Column('Fecha', String(255)),
        db.Column('FechaCreacion', DateTime),
        db.Column('CreadoPor', String(255)),
        db.Column('FechaModificacion', DateTime),
        db.Column('ModificadoPor', String(255)),
        db.Column('IsVigente', Integer)
    )
    
    db.mapper(escuela_sabatica, escuela_sabatica_mapping,properties={
        'contenido': relationship(contenido, lazy="subquery", backref='escuela_sabatica',order_by=contenido_mapping.c.NumeroLeccion)
    })
    
    db.mapper(contenido, contenido_mapping,properties={
        'leccion_diaria': relationship(leccion_diaria, lazy="subquery", backref='contenido',order_by=leccion_diaria_mapping.c.NumeroDia)
    })
    
    db.mapper(leccion_diaria, leccion_diaria_mapping)