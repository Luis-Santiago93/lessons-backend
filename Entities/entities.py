class escuela_sabatica(object):
    def __init__(self, EscuelaSabaticaID=None, ID=None, Titulo=None,Color=None,TrimestreTexto=None,
                    Trimestre=None,TrimestreNumero=None,UltimaVersionNombre=None,UltimaVersionCodigo=None, ForzarActualizacion=None, GoogleActualizacion=None, 
                    FlexibleActualizacion=None, VideoAyuda=None,Misionero=None, Portada=None,Lenguaje=None, AplicacionID=None,Ano=None,FechaCreacion=None,
                    CreadoPor=None,FechaModificacion=None,ModificadoPor=None,AlertaEGW=None,AlertaApp=None,IsVigente=None,IsPublicado=None):
        self.EscuelaSabaticaID = EscuelaSabaticaID
        self.ID = ID
        self.Titulo = Titulo
        self.Color = Color
        self.TrimestreTexto = TrimestreTexto
        self.Trimestre = Trimestre
        self.TrimestreNumero = TrimestreNumero
        self.UltimaVersionNombre = UltimaVersionNombre
        self.UltimaVersionCodigo = UltimaVersionCodigo
        self.ForzarActualizacion = ForzarActualizacion
        self.GoogleActualizacion = GoogleActualizacion
        self.FlexibleActualizacion = FlexibleActualizacion
        self.VideoAyuda = VideoAyuda
        self.Misionero = Misionero
        self.Portada = Portada
        self.Lenguaje = Lenguaje
        self.AplicacionID = AplicacionID
        self.Ano=Ano
        self.FechaCreacion = FechaCreacion
        self.CreadoPor = CreadoPor
        self.FechaModificacion = FechaModificacion
        self.ModificadoPor = ModificadoPor
        self.AlertaEGW = AlertaEGW
        self.AlertaApp = AlertaApp
        self.IsVigente = IsVigente
        self.IsPublicado = IsPublicado

    def __repr__(self):
        return "escuela_sabatica Object (Id='%s')" % self.EscuelaSabaticaID
        
class contenido(object):
    def __init__(self, ContenidoID=None, EscuelaSabaticaID=None,Titulo=None, Versiculo=None, NumeroLeccion=None,VersionCodigo=None,Fecha=None,
                    Color=None,IsEGW=None,FechaCreacion=None,
                    CreadoPor=None,FechaModificacion=None,ModificadoPor=None,IsVigente=None):
        self.ContenidoID = ContenidoID
        self.EscuelaSabaticaID = EscuelaSabaticaID
        self.Titulo = Titulo
        self.Versiculo = Versiculo
        self.NumeroLeccion = NumeroLeccion
        self.VersionCodigo = VersionCodigo
        self.Fecha = Fecha
        self.Color = Color
        self.IsEGW = IsEGW
        self.FechaCreacion = FechaCreacion
        self.CreadoPor = CreadoPor
        self.FechaModificacion = FechaModificacion
        self.ModificadoPor = ModificadoPor
        self.IsVigente = IsVigente
        
    def __repr__(self):
        return "contenido Object (Id='%s')" % self.ContenidoID
        
class leccion_diaria(object):
    def __init__(self, LeccionDiariaID=None, ContenidoID=None,Titulo=None, NumeroDia=None,VersionCodigo=None,Fecha=None,
                    TextoLeccion=None,FechaCreacion=None,
                    CreadoPor=None,FechaModificacion=None,ModificadoPor=None,IsVigente=None):
        self.LeccionDiariaID = LeccionDiariaID
        self.ContenidoID = ContenidoID
        self.Titulo = Titulo
        self.NumeroDia = NumeroDia
        self.Fecha = Fecha
        self.TextoLeccion = TextoLeccion
        self.FechaCreacion = FechaCreacion
        self.CreadoPor = CreadoPor
        self.FechaModificacion = FechaModificacion
        self.ModificadoPor = ModificadoPor
        self.IsVigente = IsVigente
        
    def __repr__(self):
        return "leccion_diaria Object (Id='%s')" % self.LeccionDiariaID