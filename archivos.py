#!/usr/bin/env python3

def buscar_funciones (archivo, funcion):
    """[Autor : Juan Godoy]"""
    """[Ayuda : Va buscando en los archivos la funcion que necesito]"""
    linea=leer_linea_clasico(archivo,',')
    while funcion!= linea[0]:
        if linea[0] !='':
            linea=leer_linea_clasico(archivo, ',')
        else:
            funcion=''
    return linea

def formateo_linea(lista):
    """[Autor : Juan Godoy]"""
    """[Ayuda : Funcion que hace que cada linea no tenga mas de 80 caracteres]"""
    n=0
    acumulador=0
    nueva_lista=lista.split()
    while len(nueva_lista)!=n:
        acumulador+=len(nueva_lista[n])
        n+=1
        if acumulador<=70 and acumulador>50:
            nueva_lista.insert(n, '\n')
            acumulador=0
    lista=' '.join(nueva_lista)
    return lista

def grabar_archivo (archivo,leyenda) :
    
    """[Autor : Nicolas]"""
    """[Ayuda : Graba linea en un archivo pasado por parametro] """
    
    archivo.write(leyenda)

def generar_archivo (lista,ruta) :
    """[Autor : Nicolas]"""
    """[Ayuda : Genera un archivo a traves de un iterable y si lo necesitas te lo devuelve abierto]"""
    
    archivo = open(ruta,'w',newline='\n')
    for funcion in lista:
        
        leyenda = ','.join(funcion)+'\n'
        grabar_archivo(archivo,leyenda)

    archivo.close()

def leer_linea (archivo) :
    
    """[Ayuda : lee una linea del archivo y devuelve una lista]"""
    
    # Esta a diferencia de la otra leer_linea ya corta por espacio con el split()
    
    linea = archivo.readline()
    if linea:
        devolver = linea
    else:
        devolver = ''
    return devolver

def leer_linea_clasico (archivo,corte) :
    
    """[Ayuda : lee una linea del archivo y devuelve una tupla]"""
    
    linea = archivo.readline().strip('\n').split(corte)
    if linea[0]!='':
        devolver = linea
    else:
        devolver = '','',''
    """[Autor : N/N]"""
    return devolver
