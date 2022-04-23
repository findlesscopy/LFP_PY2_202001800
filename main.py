import csv

with open('LaLigaBot-LFP.csv') as f:
    reader = csv.reader(f)
    for filas in reader:
        print("Fecha: {}  Temporada: {} Jornada: {} Equipos: {} vs {} Resultado: {} - {}".format(filas[0],filas[1],filas[2],filas[3],filas[4],filas[5],filas[6]))