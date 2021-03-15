#!/usr/bin/env python3
from tabla import carga_informacion_desarrollador

def leer_archivos_csv (archivocsv):
    """ Autor : Alejandro """
    """ Ayuda : leer archivos .csv y devuelve una lista de cada linea del archivo """
    linea = archivocsv.readline()
    return linea.rstrip('\n').split(',') if linea else ''
    
def info_desarrolladores(fuente_unico,comentarios):
    """ [Autor : Alejandro]
        [Ayuda : nose ]"""
    fuente_unico.seek(0)
    comentarios.seek(0)
    total_lineas = 0
    dicc_desarrolladores = {}
    linea_comentarios = leer_archivos_csv(comentarios)
    linea_fuente_unico = leer_archivos_csv(fuente_unico)
    while linea_comentarios and linea_fuente_unico:
        total_lineas += len(linea_fuente_unico[3:])
        if linea_comentarios[1].strip() in dicc_desarrolladores:
            dicc_desarrolladores[linea_comentarios[1].strip()].append([linea_fuente_unico[0],len(linea_fuente_unico[3:])])
        else:
            dicc_desarrolladores[linea_comentarios[1].strip()] = [[linea_fuente_unico[0],len(linea_fuente_unico[3:])]]
        linea_fuente_unico = leer_archivos_csv(fuente_unico)
        linea_comentarios = leer_archivos_csv(comentarios)
    carga_informacion_desarrollador(dicc_desarrolladores,total_lineas)

