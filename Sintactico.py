from Token import Token
from TypeToken import TypeToken
class Sintactico:
    preanalisis = TypeToken.UNKNOWN
    pos = 0
    lista = []
    errorSintactico = False

    def __init__(self, lista):
        self.errorSintactico = False
        self.lista = lista
        self.lista.append(Token("#", TypeToken.ULTIMO, 0, 0))
        self.pos = 0
        self.preanalisis = self.lista[self.pos].tipo
        self.Inicio()

    def Match(self, type):
        if self.preanalisis != type:
            print(str(self.lista[self.pos].tipo), "--- Sintactico", "--- Se esperaba "+str(type))
            self.errorSintactico = True
        if self.preanalisis != TypeToken.ULTIMO.name:
            self.pos += 1
            self.preanalisis = self.lista[self.pos].tipo
        if self.preanalisis == TypeToken.ULTIMO.name:
            print("Se ha finalizado el Análisis Sintáctico")

    def Inicio(self):
        print("----- Inicio Análisis Sintactico -----")
        if TypeToken.RESULTADO.name == self.preanalisis:
            self.Resultado()
            self.Repetir()
        elif TypeToken.JORNADA.name == self.preanalisis:
            self.Jornada()
            self.Repetir()
        elif TypeToken.GOLES.name == self.preanalisis:
            self.Goles()
            self.Repetir()
        elif TypeToken.TABLA_TEMPORADA.name == self.preanalisis:
            self.Tabla_Temporada()
            self.Repetir()
        elif TypeToken.PARTIDOS.name == self.preanalisis:
            self.Partidos()
            self.Repetir()
        elif TypeToken.TOP.name == self.preanalisis:
            self.Top()
            self.Repetir()
        elif TypeToken.ADIOS.name == self.preanalisis:
            self.Adios()
            self.Repetir()
    
    def Resultado(self):
        self.Match(TypeToken.RESULTADO.name)
        self.Match(TypeToken.EQUIPO.name)
        self.Match(TypeToken.VS.name)
        self.Match(TypeToken.EQUIPO.name)
        self.Match(TypeToken.TEMPORADA.name)
        self.Match(TypeToken.FECHA.name)
    
    def Jornada(self):
       self.Match(TypeToken.JORNADA.name)
       self.Match(TypeToken.NUMERO.name)
       self.Match(TypeToken.TEMPORADA.name)
       self.Match(TypeToken.FECHA.name)
       self.Match(TypeToken.F.name)
       self.Match(TypeToken.WORDS.name)

    def Goles(self):
        self.Match(TypeToken.GOLES.name)
        self.Match(TypeToken.CONDICION_GOLES.name)
        self.Match(TypeToken.EQUIPO.name)
        self.Match(TypeToken.TEMPORADA.name)
        self.Match(TypeToken.FECHA.name)
    
    def Tabla_Temporada(self):
        self.Match(TypeToken.TABLA_TEMPORADA.name)
        self.Match(TypeToken.TEMPORADA.name)
        self.Match(TypeToken.FECHA.name)
        self.Match(TypeToken.F.name)
        self.Match(TypeToken.WORDS.name)
    
    def Partidos(self):
        self.Match(TypeToken.PARTIDOS.name)
        self.Match(TypeToken.EQUIPO.name)
        self.Match(TypeToken.TEMPORADA.name)
        self.Match(TypeToken.FECHA.name)
        self.Match(TypeToken.F.name)
        self.Match(TypeToken.WORDS.name)
        self.Match(TypeToken.JI.name)
        self.Match(TypeToken.NUMERO.name)
        self.Match(TypeToken.JF.name)
        self.Match(TypeToken.NUMERO.name)

    def Top(self):
        self.Match(TypeToken.TOP.name)
        self.Match(TypeToken.CONDICION_TOP.name)
        self.Match(TypeToken.TEMPORADA.name)
        self.Match(TypeToken.FECHA.name)
        self.Match(TypeToken.N.name)
        self.Match(TypeToken.NUMERO.name)
    
    def Adios(self):
        self.Match(TypeToken.ADIOS.name)
    
    def Repetir(self):
        if TypeToken.RESULTADO.name == self.preanalisis:
            self.Resultado()
            self.Repetir()
        elif TypeToken.JORNADA.name == self.preanalisis:
            self.Jornada()
            self.Repetir()
        elif TypeToken.GOLES.name == self.preanalisis:
            self.Goles()
            self.Repetir()
        elif TypeToken.TABLA_TEMPORADA.name == self.preanalisis:
            self.Tabla_Temporada()
            self.Repetir()
        elif TypeToken.PARTIDOS.name == self.preanalisis:
            self.Partidos()
            self.Repetir()
        elif TypeToken.TOP.name == self.preanalisis:
            self.Top()
            self.Repetir()
        elif TypeToken.ADIOS.name == self.preanalisis:
            self.Adios()
            self.Repetir()