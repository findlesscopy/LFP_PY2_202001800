from operator import eq
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.font as tkFont
from tkinter import filedialog
from TypeToken import TypeToken
from helpers import Lector_Archivos
from Analizador import Analizador
from Sintactico import Sintactico
from tkinter import messagebox
from Data import Tabla
import webbrowser






def boton_reporteErrores_command():
    texto = mensaje.get(1.0,'end')
    lexico = Analizador(texto)
    lexico.ImprimirErrores()
    lexico.ReporteErrores()

def boton_limpiarLogErrores_command():
    texto = mensaje.get(1.0,'end')
    lexico = Analizador(texto)
    lexico.limpiarErrores()

def boton_reporteTokens_command():
    texto = mensaje.get(1.0,'end')
    lexico = Analizador(texto)
    lexico.Imprimir()
    lexico.ReporteToken()

def boton_limpiarLogTokens_command():
    texto = mensaje.get(1.0,'end')
    lexico = Analizador(texto)
    lexico.limpiarTokens()

def boton_enviar_command():
    data = Lector_Archivos()
    texto = mensaje.get(1.0,'end')
    text_area.insert(tk.INSERT,"\nUsuario: "+texto)
    lexico = Analizador(texto)
    lexico.Imprimir()
    lexico.ImprimirErrores()
    sintactico = Sintactico(lexico.tokens)
    longitud = len(lexico.tokens)
    for i in range(longitud):
        if lexico.tokens[i].tipo == TypeToken.RESULTADO.name:
            equipo1= str(lexico.tokens[i+1].lexema)
            equipo2 = str(lexico.tokens[i+3].lexema)
            fecha = str(lexico.tokens[i+5].lexema)
            equipo1 = equipo1.replace('"',"")
            equipo2 = equipo2.replace('"',"")
            fecha = fecha.replace("<","")
            fecha = fecha.replace(">","")
            for i in range(len(data)):
                if str(data[i].temporada) == fecha:
                    if str(data[i].local) == equipo1 and str(data[i].visitante) == equipo2:
                            print(i,"hOLA")
                            text_area.insert(tk.INSERT,"\nBot: "+"El partido se llevó a cabo el:"+data[i].fecha+" "+equipo1+" "+str(data[i].marcador_local)+" - "+str(data[i].marcador_visitante)+" "+equipo2)
        elif lexico.tokens[i].tipo == TypeToken.JORNADA.name:
            jornada = str(lexico.tokens[i+1].lexema)
            fecha = str(lexico.tokens[i+3].lexema)
            fecha = fecha.replace("<","")
            fecha = fecha.replace(">","")
            nombre_archivo = str(lexico.tokens[i+5].lexema)
            text_area.insert(tk.INSERT,"\nBot: "+"Generando archivo de resultados jornada "+jornada+" temporada "+fecha)
            messagebox.showinfo(message="Se ha genera el reporte de La Jornada", title="Jornada")
            f = open(nombre_archivo+'.html','w')
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
            f.write("<H1><center>JORNADA</center></H1>")
            f.write("<center><table><tr><th>Fecha </th><th>Local</th><th>Goles</th><th>Goles</th><th>Visitante</th>")
            for i in range(len(data)):
                if str(data[i].temporada) == fecha:
                    if str(data[i].jornada) == jornada:

                        f.write("<tr>")
                        f.write("<center><td><h4>" + str(data[i].fecha) + "</td></h4>"+"<td><h4>" + str(data[i].local) +"</td></h4>"+"<td><h4>" + str(data[i].marcador_local) +"</td></h4>"+ "<td><h4>" + str(data[i].marcador_visitante) +"</td></h4>"+ "<td><h4>" + str(data[i].visitante) +"</td></h4>"+"</center>")
                        f.write("</tr>")
            f.write("</table></center>")
            f.write("</body>")
            f.write("</html>")
            f.close()
            webbrowser.open(nombre_archivo+'.html') 

        elif lexico.tokens[i].tipo == TypeToken.GOLES.name:
            condicion = str(lexico.tokens[i+1].lexema)
            equipo = str(lexico.tokens[i+2].lexema)
            equipo = equipo.replace('"',"")
            fecha = str(lexico.tokens[i+4].lexema)
            fecha = fecha.replace("<","")
            fecha = fecha.replace(">","")
            goles_local = []
            goles_local1 = []
            goles_visitante = []
            goles_visitante1 = []
            
            if condicion == "LOCAL":
                for i in range(len(data)):
                    if str(data[i].temporada) == fecha:
                        if equipo == str(data[i].local):
                        
                            goles_local.append(int(data[i].marcador_local))
                            sumagoles_local = sum(goles_local)
                            #print(goles_local)
                text_area.insert(tk.INSERT,"\nBot: "+"Los goles anotados por el "+equipo+" de local en la temporada "+fecha+" fueron "+str(sumagoles_local))
            elif condicion == "VISITANTE":
                for i in range(len(data)):
                    if str(data[i].temporada) == fecha:
                        if equipo == str(data[i].visitante):
                        
                            goles_visitante.append(int(data[i].marcador_visitante))
                            sumagoles_visitante = sum(goles_visitante)
                            #print(goles_local)
                text_area.insert(tk.INSERT,"\nBot: "+"Los goles anotados por el "+equipo+" de visitante en la temporada "+fecha+" fueron "+str(sumagoles_visitante))
            elif condicion == "TOTAL":
                for i in range(len(data)):
                    if str(data[i].temporada) == fecha:
                            if equipo == str(data[i].local):
                        
                                goles_local1.append(int(data[i].marcador_local))
                                sumagoles_local = sum(goles_local1)
                            elif equipo == str(data[i].visitante):
                        
                                goles_visitante1.append(int(data[i].marcador_visitante))
                                sumagoles_visitante = sum(goles_visitante1)
                                #print(goles_local)
                        
                text_area.insert(tk.INSERT,"\nBot: "+"Los goles anotados por el "+equipo+" en la temporada "+fecha+" fueron "+str(sumagoles_local+sumagoles_visitante))

        elif lexico.tokens[i].tipo == TypeToken.TABLA_TEMPORADA.name:
            fecha = str(lexico.tokens[i+2].lexema)
            fecha = fecha.replace("<","")
            fecha = fecha.replace(">","")
            nombre_archivo = str(lexico.tokens[i+4])
            puntos = []
            for i in range(len(data)):
                if str(data[i].temporada) == fecha:
                    if int(data[i].marcador_local) > int(data[i].marcador_visitante):
                        puntos.append(Tabla(data[i].local,3,data[i].visitante,0))
                    elif int(data[i].marcador_local) < int(data[i].marcador_visitante):
                        puntos.append(Tabla(data[i].local,0,data[i].visitante,3))
                    elif int(data[i].marcador_local) == int(data[i].marcador_visitante):
                        puntos.append(Tabla(data[i].local,1,data[i].visitante,1))
                        
            for i in range(len(puntos)):
                if 

def boton_aceptarTexto_command():
    Tk().withdraw()
    filedir = filedialog.askopenfilename(filetypes=[("Archivo data","*.form")])
    #print(direccion)
    texto = text_area.insert('end')
    #print(texto)
    with open(filedir,"r+",encoding = "utf-8") as f:
        f.truncate(0)
        f.write(texto)

def boton_buscar_reporte():
    pass

root = Tk()
root.title("Menú Principal")
ft = tkFont.Font(family='Tahoma',size=8)


content = ttk.Frame(root)
frame = ttk.Frame(content, width=600, height=450)

text_area=tk.Text(root)
text_area["font"] = ft
text_area.place(x=30,y=60,width=412,height=320)
text_area.insert(tk.INSERT,"Bienvenido a La Liga Bot, Introduzca los comandos que desea ejecutar:")



mensaje = tk.Text(root)
mensaje["font"] = ft
mensaje.place(x=30,y=390,width=412,height=30)

label1=tk.Label(root)
label1["font"] = ft
label1["justify"] = "center"
label1["text"] = "Archivo ingresado"
label1.place(x=30,y=20,width=411,height=30)

boton_reporteErrores=tk.Button(root)
boton_reporteErrores["font"] = ft
boton_reporteErrores["justify"] = "center"
boton_reporteErrores["text"] = "Reporte de Errores"
boton_reporteErrores.place(x=460,y=60,width=121,height=30)
boton_reporteErrores["command"] = boton_reporteErrores_command 

boton_limpiarLogErrores=tk.Button(root)
boton_limpiarLogErrores["font"] = ft
boton_limpiarLogErrores["justify"] = "center"
boton_limpiarLogErrores["text"] = "Limpiar log de errores"
boton_limpiarLogErrores.place(x=460,y=110,width=121,height=30)
boton_limpiarLogErrores["command"] =boton_limpiarLogErrores_command

boton_reporteToken=tk.Button(root)
boton_reporteToken["font"] = ft
boton_reporteToken["justify"] = "center"
boton_reporteToken["text"] = "Reporte Tokens"
boton_reporteToken.place(x=460,y=160,width=120,height=30)
boton_reporteToken["command"] = boton_reporteTokens_command 
        

boton_limpiarLogTokens=tk.Button(root)
boton_limpiarLogTokens["font"] = ft
boton_limpiarLogTokens["justify"] = "center"
boton_limpiarLogTokens["text"] = "Limpiar log de tokens"
boton_limpiarLogTokens.place(x=460,y=210,width=120,height=30)
boton_limpiarLogTokens["command"] = boton_limpiarLogTokens_command 

boton_manualUsuario=tk.Button(root)
boton_manualUsuario["font"] = ft
boton_manualUsuario["justify"] = "center"
boton_manualUsuario["text"] = "Manual de Usuario"
boton_manualUsuario.place(x=460,y=260,width=120,height=30)
boton_manualUsuario["command"] = boton_buscar_reporte 

boton_manualTecnico=tk.Button(root)
boton_manualTecnico["font"] = ft
boton_manualTecnico["justify"] = "center"
boton_manualTecnico["text"] = "Manual Técnico"
boton_manualTecnico.place(x=460,y=310,width=120,height=30)
boton_manualTecnico["command"] = boton_buscar_reporte 

label2=tk.Label(root)
label2["font"] = ft
label2["justify"] = "center"
label2["text"] = "Seleccione una opción:"
label2.place(x=445,y=20,width=140,height=30)

boton_enviar=tk.Button(root)
boton_enviar["font"] = ft
boton_enviar["justify"] = "center"
boton_enviar["text"] = "Enviar"
boton_enviar.place(x=460,y=390,width=120,height=30)
boton_enviar["command"] = boton_enviar_command 



content.pack()
frame.pack()



root.mainloop()



