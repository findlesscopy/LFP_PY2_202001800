from lib2to3.pgen2 import token
import turtle
from Token import Token
from tkinter import messagebox
import webbrowser
from Data import Data

class Analizador:
    #Guarda lo que llevo
    lexema = ''
    #Lista de token
    tokens = []
    #Estado en el que se encuentra
    estado = 1
    #Fila en la que se encuentra
    fila = 0
    #COlumna en la que se encuentra
    columna = 0
    #Bool para errores
    generar = False

    elementos = []
    entrada2 = ''
    def __init__(self, entrada):
        self.entrada2 = entrada
        self.lexema = ''
        self.tokens = []
        self.estado = 1
        self.fila = 1
        self.columna = 1
        self.generar = True
        tipos = Token("lexema",-1,-1,-1)

        entrada = entrada + '$'
        actual = ''
        longitud = len(entrada)
        
        i = 0
        while(i < longitud):
            actual = entrada[i]
            i += 1
            #Manejo inicial
            if self.estado == 1:
                if actual.isalpha():
                    self.estado = 2
                    self.columna += 1
                    self.lexema += actual
                    continue
                elif actual.isdigit():
                    self.estado = 3
                    self.columna += 1
                    self.lexema += actual
                    continue
                elif actual == "<":
                    self.estado = 4
                    self.columna += 1
                    self.lexema += actual
                    continue
                elif actual == '"':
                    self.estado = 5
                    self.columna += 1
                    self.lexema += actual
                    continue
                elif actual == "-":
                    self.estado = 6
                    self.columna += 1
                    self.lexema += actual
                    continue
                elif actual == ' ':
                    self.columna +=1
                    self.estado = 1
                elif actual == '\n':
                    self.fila += 1
                    self.estado = 1
                    self.columna = 1
                elif actual =='\r':
                    self.estado = 1
                elif actual == '\t':
                    self.columna += 5
                    self.estado = 1
                elif actual == '$':
                    print('Analisis terminado')
                else:
                    self.lexema += actual
                    self.AddToken(tipos.UNKNOWN)
                    self.columna += 1
                    self.generar = False
                    messagebox.showinfo(message="Ha ocurrido un error", title="Error")
                    self.lexema = ''

            #Manejo de Letras
            if self.estado == 2:
                if actual.isalpha():
                    self.estado = 2
                    self.columna += 1
                    self.lexema += actual
                else:
                    if self.Reservada():
                        self.AddToken(self.tipo)
                        i -= 1
                        continue
                    else:
                        self.AddToken(tipos.WORDS)
                        i -= 1
                        continue
                        
            #Manejo de Numeros
            if self.estado == 3:
                if actual.isdigit():
                    self.estado = 3
                    self.columna += 1
                    self.lexema += actual
                else: 
                    self.AddToken(tipos.NUMERO)
                    i -= 1
                    continue
            
            #Manejo de Fechas
            if self.estado == 4:
                if actual != ">":
                    self.estado = 4
                    self.columna += 1
                    self.lexema += actual
                elif actual == ">":
                    self.estado = 4
                    self.columna += 1
                    self.lexema += actual
                    self.AddToken(tipos.FECHA)
                    continue

            #Manejo de Cadenas
            if self.estado == 5:
                if actual != '"':
                    self.estado = 5
                    self.columna += 1
                    self.lexema += actual
                elif actual == '"':
                    self.estado = 5
                    self.columna += 1
                    self.lexema += actual
                    self.AddToken(tipos.EQUIPO)
                    continue    
            
            #Manejo de Banderas
            if self.estado == 6:
                if actual.isalpha():
                    self.estado = 6
                    self.columna += 1
                    self.lexema += actual
                else: 
                    if self.Banderas():
                        i -= 1
                        self.AddToken(self.tipo)
                        continue
                    else:
                        i -= 1
                        self.AddToken(tipos.WORDS)
                        continue
            

    def AddToken(self,tipo):
        self.tokens.append(Token(self.lexema, tipo, self.fila, self.columna))
        self.lexema = ""
        self.estado = 1
    
    def Banderas(self):
        bandera = self.lexema
        if bandera == "-f":
            self.tipo = Token.F
            return True
        if bandera == "-ji":
            self.tipo = Token.JI
            return True
        if bandera == "-jf":
            self.tipo = Token.JF
            return True
        if bandera == "-n":
            self.tipo = Token.N
            return True
        return False


    def Reservada(self):
        palabra = self.lexema.upper();
        if palabra == 'RESULTADO':
            self.tipo = Token.RESULTADO  
            return True
        if palabra == 'VS':
            self.tipo = Token.VS 
            return True
        if palabra == 'TEMPORADA':
            self.tipo = Token.TEMPORADA
            return True
        if palabra == 'JORNADA':
            self.tipo = Token.JORNADA
            return True
        if palabra == 'GOLES':
            self.tipo = Token.GOLES
            return True
        if palabra == 'LOCAL':
            self.tipo = Token.LOCAL
            return True
        if palabra == 'VISITANTE':
            self.tipo = Token.VISITANTE
            return True
        if palabra == 'TOTAL':
            self.tipo = Token.TOTAL
            return True
        if palabra == 'TABLA':
            self.tipo = Token.TABLA_TEMPORADA
            return True
        if palabra == 'PARTIDOS':
            self.tipo = Token.PARTIDOS
            return True
        if palabra == 'TOP':
            self.tipo = Token.TOP
            return True
        if palabra == 'SUPERIOR':
            self.tipo = Token.SUPERIOR
            return True
        if palabra == 'INFERIOR':
            self.tipo = Token.INFERIOR
            return True
        if palabra == 'ADIOS':
            self.tipo = Token.ADIOS
            return True
        return False
    
    def Imprimir(self):
        print("-------------Tokens--------------")
        tipos = Token("lexema", -1, -1, -1)
        for x in self.tokens:
            if x.tipo != tipos.UNKNOWN:
                print(x.getLexema()," --> ",x.getTipo(),' --> ',x.getFila(), ' --> ',x.getColumna())
    
    def ImprimirErrores(self):
        print("-------------Errores--------------")
        tipos = Token("lexema", -1, -1, -1)
        for x in self.tokens:
            if x.tipo == tipos.UNKNOWN:
                print(x.getLexema()," --> ",x.getFila(), ' --> ',x.getColumna(),'--> Error Lexico')
    
    