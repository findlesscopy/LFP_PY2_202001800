from operator import eq
from re import A
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.font as tkFont
from tkinter import filedialog

from numpy import append
from TypeToken import TypeToken
from helpers import Lector_Archivos
from Analizador import Analizador
from Sintactico import Sintactico
from tkinter import messagebox
from Data import Tabla, Tabla_Ordenada
import webbrowser
import sys






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
    text_area.insert(tk.INSERT,"\n Usuario: "+texto)
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
            for j in range(len(data)):
                if str(data[j].temporada) == fecha:
                    if str(data[j].local) == equipo1 and str(data[j].visitante) == equipo2:
                            #print(i,"hOLA")
                            text_area.insert(tk.INSERT,"\n Bot: "+"El partido se llevó a cabo el:"+data[j].fecha+" "+equipo1+" "+str(data[j].marcador_local)+" - "+str(data[j].marcador_visitante)+" "+equipo2)
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
            local = 0
            visitante = 0
            total = 0
            fecha = str(lexico.tokens[i+2].lexema)
            fecha = fecha.replace("<","")
            fecha = fecha.replace(">","")
            nombre_archivo = str(lexico.tokens[i+4].lexema)
            puntos = []
            equipos = []
            equipos_total = []
            tabla = []
            text_area.insert(tk.INSERT,"\nBot: "+"Generando archivo de Tabla General Temporada "+fecha)
            messagebox.showinfo(message="Se ha genera el reporte de Tabla General", title="Tabla General")
            f = open(nombre_archivo+'.html','w')
            f.write("<!doctype html>")
            f.write("<html lang=\"en\">")
            f.write("<head>")
            f.write(" <meta charset=\"utf-8\">")
            f.write("<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">")
            f.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">")
            f.write("<title>Reporte Tabla General</title>")
            f.write("<style>"
                "body {background-color: #F5EFB1;font-family: \"Lucida Console\", \"Courier New\", monospace;}"
                "h1 {background-color: #87DABF;}"
                "table, th, td {border: 1px solid black; text-align: center}""</style>")
            f.write("</head>")
            f.write("<body>")
            f.write("<H1><center>Tabla General</center></H1>")
            f.write("<center><table><tr><th>Posición</th><th>Equipo</th><th>Puntos</th>")
            for i in range(len(data)):
                if str(data[i].temporada) == fecha:
                    if int(data[i].marcador_local) > int(data[i].marcador_visitante):
                        puntos.append(Tabla(data[i].local,3))
                        local += 3
                        puntos.append(Tabla(data[i].visitante,0))
                        visitante += 0
                    elif int(data[i].marcador_local) < int(data[i].marcador_visitante):
                        puntos.append(Tabla(data[i].local,0))
                        local += 0
                        puntos.append(Tabla(data[i].visitante,3))
                        visitante += 3
                    elif int(data[i].marcador_local) == int(data[i].marcador_visitante):
                        puntos.append(Tabla(data[i].local,1))
                        local += 1
                        puntos.append(Tabla(data[i].visitante,1))
                        visitante += 1
                
                    equipos.append(data[i].local)
            puntos.sort(key=lambda x:x.equipo, reverse=False)
            for element in equipos:
                if element not in equipos_total:
                    equipos_total.append(element)
            equipos_total.sort()
            #print(puntos)
            #print(equipos_total)
            puntos_suma = []       
            for x in equipos_total:
                for y in range(len(puntos)):
                    if x == str(puntos[y].equipo):
                        puntos_suma.append(puntos[y].puntos)
                        puntos_suma1 = sum(puntos_suma)
                    else:
                        
                        puntos_suma.clear() 
                tabla.append(Tabla_Ordenada(x,puntos_suma1))
                    #tabla.append(Tabla_Ordenada(x,puntos_suma1))
                    #puntos_suma.clear()
            #print(puntos_suma1)
            #print(repr(tabla))
            tabla.sort(key=lambda x:x.puntos, reverse=True)
            
            for i in range(len(tabla)):
                f.write("<tr>")
                f.write("<center><td><h4>" + str(i+1) + "</td></h4>"+"<td><h4>" + str(tabla[i].equipo) +"</td></h4>"+"<td><h4>" + str(tabla[i].puntos) +"</td></h4></center>")
                f.write("</tr>")
            f.write("</table></center>")
            f.write("</body>")
            f.write("</html>")
            f.close()
            webbrowser.open(nombre_archivo+'.html') 
            #print(tabla)
        
        elif lexico.tokens[i].tipo == TypeToken.PARTIDOS.name:
            equipo = str(lexico.tokens[i+1].lexema)
            equipo = equipo.replace('"',"")
            fecha = str(lexico.tokens[i+3].lexema)
            fecha = fecha.replace("<","")
            fecha = fecha.replace(">","")
            nombre_archivo = str(lexico.tokens[i+5].lexema)
            jornadaInicial = int(lexico.tokens[i+7].lexema)
            jornadaFinal = int(lexico.tokens[i+9].lexema)
            text_area.insert(tk.INSERT,"\nBot: "+"Generando archivo de resultados del "+equipo+" temporada "+fecha+ " Jornada "+str(jornadaInicial)+" - " + str(jornadaFinal))
            messagebox.showinfo(message="Se ha genera el reporte del Equipo", title="Jornada")
            f = open(nombre_archivo+'.html','w')
            f.write("<!doctype html>")
            f.write("<html lang=\"en\">")
            f.write("<head>")
            f.write("<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">")
            f.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">")
            f.write("<title>Reporte del Equipo</title>")
            f.write("<style>"
                "body {background-color: #F5EFB1;font-family: \"Lucida Console\", \"Courier New\", monospace;}"
                "h1 {background-color: #87DABF;}"
                "table, th, td {border: 1px solid black; text-align: center}""</style>")
            f.write("</head>")
            f.write("<body>")
            f.write("<H1><center>Resultados</center></H1>")
            f.write("<center><table><tr><th>Local</th><th>Goles</th><th>Goles</th><th>Visitante</th>")
            for i in range(len(data)):
                if str(data[i].temporada) == fecha:
                    if int(data[i].jornada) >= jornadaInicial and int(data[i].jornada) <= jornadaFinal:
                        if str(data[i].local) == equipo:
                            f.write("<tr>")
                            f.write("<center><td><h4>" + equipo + "</td></h4>"+"<td><h4>" + str(data[i].marcador_local) +"</td></h4>"+"<td><h4>" + str(data[i].marcador_visitante) +"</td></h4>"+ "<td><h4>" + str(data[i].visitante) +"</td></h4>")
                            
                            f.write("</tr>") 
                            print(equipo+" "+str(data[i].marcador_local)+" VS "+str(data[i].marcador_visitante)+" "+str(data[i].visitante))
                        if str(data[i].visitante) == equipo:
                            f.write("<tr>")
                            f.write("<center><td><h4>" + str(data[i].local) + "</td></h4>"+"<td><h4>" + str(data[i].marcador_local) +"</td></h4>"+"<td><h4>" + str(data[i].marcador_visitante) +"</td></h4>"+ "<td><h4>" + equipo +"</td></h4>")
                            f.write("</tr>")  
                            print(str(data[i].local+" "+str(data[i].marcador_local)+" VS "+str(data[i].marcador_visitante)+" "+equipo))
        
            f.write("</table></center>")
            f.write("</body>")
            f.write("</html>")
            f.close()
            webbrowser.open(nombre_archivo+'.html')

        elif lexico.tokens[i].tipo == TypeToken.TOP.name:
            local = 0
            visitante = 0
            total = 0
            condicion = str(lexico.tokens[i+1].lexema)
            fecha = str(lexico.tokens[i+3].lexema)
            fecha = fecha.replace("<","")
            fecha = fecha.replace(">","")
            numero = int(lexico.tokens[i+5].lexema)
            puntos = []
            equipos = []
            equipos_total = []
            tabla = []
            text_area.insert(tk.INSERT,"\nBot: "+"Generando archivo de Top "+condicion+" Temporada "+fecha)
            messagebox.showinfo(message="Se ha genera el reporte de Top"+condicion, title="TOP")
            f = open('Top.html','w')
            f.write("<!doctype html>")
            f.write("<html lang=\"en\">")
            f.write("<head>")
            f.write(" <meta charset=\"utf-8\">")
            f.write("<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">")
            f.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">")
            f.write("<title>Reporte Top</title>")
            f.write("<style>"
                "body {background-color: #F5EFB1;font-family: \"Lucida Console\", \"Courier New\", monospace;}"
                "h1 {background-color: #87DABF;}"
                "table, th, td {border: 1px solid black; text-align: center}""</style>")
            f.write("</head>")
            f.write("<body>")
            f.write("<H1><center>Top</center></H1>")
            f.write("<center><table><tr><th>Posición</th><th>Equipo</th><th>Puntos</th>")
            for i in range(len(data)):
                if str(data[i].temporada) == fecha:
                    if int(data[i].marcador_local) > int(data[i].marcador_visitante):
                        puntos.append(Tabla(data[i].local,3))
                        local += 3
                        puntos.append(Tabla(data[i].visitante,0))
                        visitante += 0
                    elif int(data[i].marcador_local) < int(data[i].marcador_visitante):
                        puntos.append(Tabla(data[i].local,0))
                        local += 0
                        puntos.append(Tabla(data[i].visitante,3))
                        visitante += 3
                    elif int(data[i].marcador_local) == int(data[i].marcador_visitante):
                        puntos.append(Tabla(data[i].local,1))
                        local += 1
                        puntos.append(Tabla(data[i].visitante,1))
                        visitante += 1
                
                    equipos.append(data[i].local)
            puntos.sort(key=lambda x:x.equipo, reverse=False)
            for element in equipos:
                if element not in equipos_total:
                    equipos_total.append(element)
            equipos_total.sort()
            #print(puntos)
            #print(equipos_total)
            puntos_suma = []       
            for x in equipos_total:
                for y in range(len(puntos)):
                    if x == str(puntos[y].equipo):
                        puntos_suma.append(puntos[y].puntos)
                        puntos_suma1 = sum(puntos_suma)
                    else:
                        
                        puntos_suma.clear() 
                tabla.append(Tabla_Ordenada(x,puntos_suma1))
                    #tabla.append(Tabla_Ordenada(x,puntos_suma1))
                    #puntos_suma.clear()
            #print(puntos_suma1)
            #print(repr(tabla))
            if condicion == "SUPERIOR":

                tabla.sort(key=lambda x:x.puntos, reverse=True)
            
                for i in range(numero):
                    
                    f.write("<tr>")
                    f.write("<center><td><h4>" + str(i+1) + "</td></h4>"+"<td><h4>" + str(tabla[i].equipo) +"</td></h4>"+"<td><h4>" + str(tabla[i].puntos) +"</td></h4></center>")
                    f.write("</tr>")
                f.write("</table></center>")
                f.write("</body>")
                f.write("</html>")
                f.close()
                webbrowser.open('Top.html') 
                #print(tabla)
            elif condicion == "INFERIOR":
                tabla.sort(key=lambda x:x.puntos, reverse=False)
            
                for i in range(numero):
                    f.write("<tr>")
                    f.write("<center><td><h4>" + str(i+1) + "</td></h4>"+"<td><h4>" + str(tabla[i].equipo) +"</td></h4>"+"<td><h4>" + str(tabla[i].puntos) +"</td></h4></center>")
                    f.write("</tr>")
                f.write("</table></center>")
                f.write("</body>")
                f.write("</html>")
                f.close()
                webbrowser.open('Top.html') 
                #print(tabla)

        elif lexico.tokens[i].tipo == TypeToken.ADIOS.name:
            messagebox.showinfo(message="Cerrando el programa :D",title="Despedida")
            sys.exit()

def boton_aceptarTexto_command():
    Tk().withdraw()
    filedir = filedialog.askopenfilename(filetypes=[("Archivo data","*.form")])
    #print(direccion)
    texto = text_area.insert('end')
    #print(texto)
    with open(filedir,"r+",encoding = "utf-8") as f:
        f.truncate(0)
        f.write(texto)

def boton_manualUsuario_command():
    webbrowser.open('Manual de Usuario.pdf')

def boton_manualTecnico_command():
    webbrowser.open('Manual Tecnico.pdf')

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
boton_manualUsuario["command"] = boton_manualUsuario_command 

boton_manualTecnico=tk.Button(root)
boton_manualTecnico["font"] = ft
boton_manualTecnico["justify"] = "center"
boton_manualTecnico["text"] = "Manual Técnico"
boton_manualTecnico.place(x=460,y=310,width=120,height=30)
boton_manualTecnico["command"] = boton_manualTecnico_command 

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



