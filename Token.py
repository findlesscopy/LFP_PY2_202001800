class Token():
    lexema = ''
    tipo = 0
    fila = 0
    columna = 0

    #ENUM
    RESULTADO = 1
    VS = 2
    TEMPORADA = 3
    JORNADA = 4
    F = 5
    GOLES = 6
    LOCAL = 7
    VISITANTE = 8
    TOTAL = 9
    TABLA_TEMPORADA = 10
    PARTIDOS = 11
    JI = 12
    JF = 13
    TOP = 14
    N = 15
    SUPERIOR = 16
    INFERIOR = 17
    ADIOS = 18
    CADENA = 19
    NUMERO = 20
    FECHA = 21
    WORDS = 22
    UNKNOWN = 23

    #Constructor de la clase
    def __init__(self,lexema,tipo,fila,columna):
        self.lexema = lexema
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def getLexema(self):
        return self.lexema

    def getFila(self):
        return self.fila
    
    def getColumna(self):
        return self.columna

    def getTipo(self):
        if self.tipo == self.RESULTADO:
            return 'RESULTADO'
        elif self.tipo == self.VS:
            return 'VS'
        elif self.tipo == self.TEMPORADA:
            return 'TEMPORADA'
        elif self.tipo == self.JORNADA:
            return 'JORNADA'
        elif self.tipo == self.F:
            return 'F'
        elif self.tipo == self.GOLES:
            return 'GOLES'
        elif self.tipo == self.LOCAL:
            return 'LOCAL'
        elif self.tipo == self.VISITANTE:
            return 'VISITANTE'
        elif self.tipo == self.TOTAL:
            return 'TOTAL'
        elif self.tipo == self.TABLA_TEMPORADA:
            return 'TABLA_TEMPORADA'
        elif self.tipo == self.PARTIDOS:
            return 'PARTIDOS'
        elif self.tipo == self.JI:
            return 'JI'
        elif self.tipo == self.JF:
            return 'JF'
        elif self.tipo == self.TOP:
            return 'TOP'
        elif self.tipo == self.N:
            return 'N'
        elif self.tipo == self.SUPERIOR:
            return 'SUPERIOR'
        elif self.tipo == self.INFERIOR:
            return 'INFERIOR'
        elif self.tipo == self.ADIOS:
            return 'ADIOS'
        elif self.tipo == self.CADENA:
            return 'CADENA'
        elif self.tipo == self.NUMERO:
            return 'NUMERO'
        elif self.tipo == self.FECHA:
            return 'FECHA'
        elif self.tipo == self.WORDS:
            return 'WORDS'
        elif self.tipo == self.WORDS:
            return "WORDS"
        elif self.tipo == self.UNKNOWN:
            return "UNKNOWN"