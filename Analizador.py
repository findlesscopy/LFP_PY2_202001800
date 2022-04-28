from Token import Token
from TypeToken import TypeToken
from tkinter import messagebox
import webbrowser
from Data import Data

class Analizador:
    tipo = TypeToken.UNKNOWN
    #Guarda lo que llevo
    lexema = ''
    #Lista de token
    tokens = []
    #Estado en el que se encuentra
    estado = 1
    #Fila en la que se encuentra
    fila = 1
    #COlumna en la que se encuentra
    columna = 0
    #Bool para errores
    generar = False

    def __init__(self, entrada):
        self.lexema = ''
        self.tokens = []
        self.estado = 1
        self.fila = 1
        self.columna = 0
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
                    self.AddToken(TypeToken.UNKNOWN.name)
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
                        self.AddToken(TypeToken.WORDS.name)
                        i -= 1
                        continue
                        
            #Manejo de Numeros
            if self.estado == 3:
                if actual.isdigit():
                    self.estado = 3
                    self.columna += 1
                    self.lexema += actual
                else: 
                    self.AddToken(TypeToken.NUMERO.name)
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
                    self.AddToken(TypeToken.FECHA.name)
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
                    self.AddToken(TypeToken.EQUIPO.name)
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
                        self.AddToken(TypeToken.WORDS.name)
                        continue
            

    def AddToken(self,tipo):
        self.tokens.append(Token(self.lexema, tipo, self.fila, self.columna))
        self.lexema = ""
        self.estado = 1
        self.tipo = TypeToken.UNKNOWN
    
    def Banderas(self):
        bandera = self.lexema
        if bandera == "-f":
            self.tipo = TypeToken.F.name
            return True
        if bandera == "-ji":
            self.tipo = TypeToken.JI.name
            return True
        if bandera == "-jf":
            self.tipo = TypeToken.JF.name
            return True
        if bandera == "-n":
            self.tipo = TypeToken.N.name
            return True
        return False


    def Reservada(self):
        palabra = self.lexema.upper();
        if palabra == 'RESULTADO':
            self.tipo = TypeToken.RESULTADO.name  
            return True
        if palabra == 'VS':
            self.tipo = TypeToken.VS.name
            return True
        if palabra == 'TEMPORADA':
            self.tipo = TypeToken.TEMPORADA.name
            return True
        if palabra == 'JORNADA':
            self.tipo = TypeToken.JORNADA.name
            return True
        if palabra == 'GOLES':
            self.tipo = TypeToken.GOLES.name
            return True
        if palabra == 'LOCAL':
            self.tipo = TypeToken.CONDICION_GOLES.name
            return True
        if palabra == 'VISITANTE':
            self.tipo = TypeToken.CONDICION_GOLES.name
            return True
        if palabra == 'TOTAL':
            self.tipo = TypeToken.CONDICION_GOLES.name
            return True
        if palabra == 'TABLA':
            self.tipo = TypeToken.TABLA_TEMPORADA.name
            return True
        if palabra == 'PARTIDOS':
            self.tipo = TypeToken.PARTIDOS.name
            return True
        if palabra == 'TOP':
            self.tipo = TypeToken.TOP.name
            return True
        if palabra == 'SUPERIOR':
            self.tipo = TypeToken.CONDICION_TOP.name
            return True
        if palabra == 'INFERIOR':
            self.tipo = TypeToken.CONDICION_TOP.name
            return True
        if palabra == 'ADIOS':
            self.tipo = TypeToken.ADIOS.name
            return True
        return False
    
    def Imprimir(self):
        print("-------------Tokens--------------")
        tipos = Token("lexema", -1, -1, -1)
        for x in self.tokens:
            if str(x.tipo) != "UNKNOWN":
                print(x.lexema," --> ",str(x.tipo),' --> ',str(x.fila), ' --> ',str(x.columna))
    
    def ImprimirErrores(self):
        print("-------------Errores--------------")
        tipos = Token("lexema", -1, -1, -1)
        for x in self.tokens:
            if str(x.tipo) == "UNKNOWN":
                print(x.lexema," --> ",str(x.tipo),' --> ',str(x.fila), ' --> ',str(x.columna),'--> Error Lexico')
    
    def ReporteErrores(self):
        
        messagebox.showinfo(message="Se ha genera el reporte de Errores", title="Reporte")
        f = open('Reporte Errores.html','w')
        f.write("<!doctype html>")
        f.write("<html lang=\"en\">")
        f.write("<head>")
        f.write("<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">")
        f.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">")
        f.write("<title>Reporte del Tokens</title>")
        f.write("<style>"
            "body {background-color: #F5EFB1;font-family: \"Lucida Console\", \"Courier New\", monospace;}"
            "h1 {background-color: #87DABF;}"
            "table, th, td {border: 1px solid black; text-align: center}""</style>")
        f.write("</head>")
        f.write("<body>")
        f.write("<H1><center>REPORTE DE ERRORES LEXICOS</center></H1>")
        f.write("<center><table><tr><th>No. </th><th>Símbolo</th><th>Tipo</th><th>Fila</th><th>Columna</th>")
        tipos = Token("lexema", -1, -1, -1)
        i=0
        for x in self.tokens:
            i+=1
            if str(x.tipo) == "UNKNOWN":
                f.write("<tr>")
                f.write("<center><td><h4>" + str(i) + "</td></h4>"+"<td><h4>" + str(x.lexema ) +"</td></h4>"+"<td><h4>" + str(x.tipo) +"</td></h4>"+ "<td><h4>" + str(x.fila) +"</td></h4>"+ "<td><h4>" + str(x.columna) +"</td></h4>"+"</center>")
                f.write("</tr>")
        f.write("</table></center>")
        f.write("</body>")
        f.write("</html>")
        f.close()
        webbrowser.open('Reporte Errores.html') 
    
    def ReporteToken(self):
        
        messagebox.showinfo(message="Se ha genera el reporte de token", title="Reporte")
        f = open('Reporte Token.html','w')
        f.write("<!doctype html>")
        f.write("<html lang=\"en\">")
        f.write("<head>")
        f.write("<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">")
        f.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">")
        f.write("<title>Reporte del Tokens</title>")
        f.write("<style>"
            "body {background-color: #F5EFB1;font-family: \"Lucida Console\", \"Courier New\", monospace;}"
            "h1 {background-color: #87DABF;}"
            "table, th, td {border: 1px solid black; text-align: center}""</style>")
        f.write("</head>")
        f.write("<body>")
        f.write("<H1><center>REPORTE DE TOKENS</center></H1>")
        f.write("<center><table><tr><th>No. </th><th>Símbolo</th><th>Tipo</th><th>Fila</th><th>Columna</th>")
        tipos = Token("lexema", -1, -1, -1)
        i=0
        for x in self.tokens:
            i+=1
            if str(x.tipo) != "UNKNOWN":
                f.write("<tr>")
                f.write("<center><td><h4>" + str(i) + "</td></h4>"+"<td><h4>" + str(x.lexema ) +"</td></h4>"+"<td><h4>" + str(x.tipo) +"</td></h4>"+ "<td><h4>" + str(x.fila) +"</td></h4>"+ "<td><h4>" + str(x.columna) +"</td></h4>"+"</center>")
                f.write("</tr>")
        f.write("</table></center>")
        f.write("</body>")
        f.write("</html>")
        f.close()
        webbrowser.open('Reporte Token.html')
    
    def limpiarErrores(self):
        messagebox.showinfo(message="Se ha limpiado el log de Errores", title="Reporte")
        self.tokens.clear()

    def limpiarTokens(self):
        messagebox.showinfo(message="Se ha limpiado el log de Tokens", title="Reporte")
        self.tokens.clear()