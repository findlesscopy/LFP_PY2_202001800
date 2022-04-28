class Data:

    def __init__(self,fecha, temporada, jornada, local, visitante, marcador_local, marcador_visitante):
        self.fecha = fecha
        self.temporada = temporada
        self.jornada = jornada
        self.local = local
        self.visitante = visitante
        self.marcador_local = marcador_local
        self.marcador_visitante = marcador_visitante


    def __repr__(self):
        return f'\n Fecha {self.fecha} Temporada {self.temporada} Jornada {self.jornada} Local {self.local} Visitante {self.visitante} Marcador Local {self.marcador_local} Marcador Visitante {self.marcador_visitante}'

class Tabla:
    def __init__(self,local,puntos_local,visitante,puntos_visitante):
        self.local = local
        self.puntos_local = puntos_local
        self.visitante = visitante
        self.puntos_visitante = puntos_visitante
    
    def __repr__(self):
        return f'\n Equipo Local {self.local} Puntos {self.puntos_local} Equipo Visitante {self.visitante} Puntos {self.puntos_visitante} '