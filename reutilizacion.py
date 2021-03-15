#!/usr/bin/env python3
from archivos import leer_linea_clasico
def lista_de_funciones():
    """
    [Autor : Sofia Marchesini]
    [Ayuda : Esta funcion crea una lista de funciones compuesta por
    los nombres de todas las funciones que se encuentran
    en el primer elemento de las lineas del archivo ]
    """
    fuente=open('fuente_unico.csv','r')
    linea = leer_linea_clasico(fuente,',')
    funciones = []
    while linea!=('','',''):
        funciones.append(linea[0])
        linea = leer_linea_clasico(fuente,',')
    fuente.close()
    return funciones


def veces_invocadas(linea):
    """
    [Autor : Sofia Marchesini]
    [Ayuda : esta funcion crea un dicionario compuesto por
    la clave como la funcion invocada y el valor
    como las veces que esta funcion fue invocada]
    """
    funciones = lista_de_funciones()
    cant_invocaciones = {}
    
    #recorro todas las funciones y me fijo una a una si estan en la linea leida por funciones_invocadas
    for funcion in funciones:
        #recorro todas las funciones de la lista de funciones
        for palabras in linea[3:]:
            #recorro todos los elementos de la linea que lei antes 
            if '{}('.format(funcion) in palabras and funcion not in cant_invocaciones:
                cant_invocaciones[funcion] = 1
            elif '{}('.format(funcion) in palabras and funcion in cant_invocaciones:
                cant_invocaciones[funcion] += 1
    return cant_invocaciones


def funciones_invocadas(fuente):
    """
    [Autor : Sofia Marchesini]
    [Ayuda: esta funcion crea un diccionario con todas las funciones como claves.
    El diccionario tendra como valor como un diccionario compuesto por la funcion
    que invoco , y el valor las veces invocada.
    Si no invoca ninguna funcion aparecera la lista vacia
    funcion1 {funcion2 : n veces} ,funcion 1 llama a funcion 2 n veces]
    
    """
    linea = leer_linea_clasico(fuente,',')
    invocaciones = {}
    while linea !=('','',''):
        funcion_1 = linea[0]   
        invocaciones[funcion_1] = veces_invocadas(linea)
        linea = leer_linea_clasico(fuente,',')

    return invocaciones


def crear_filas(invocaciones, funciones, total):
    """
    [Autor : Sofia Marchesini]
    [Ayuda : Empiezo la primera parte de crear la tabla]
    """
    nueva_fila = []
    y = len(funciones)
    
    for x in range(1, y+1):
        #marco el rango para que finalice al terminar la cantidad de funciones
        filas = []
        nueva_fila.append(filas)  
        #agrego la fila a la lista nueva_fila y reinicio la fila cada vez que es terminada la referida a una funcion en particular
        #creo la fila de cada una de las funciones referidas por el rango:
        for funcion in invocaciones:
            #recorro todas las funciones que tiene como clave el diccionario creado previamente
            #como recorro en a todas en el mismo  orden la fila saldra siempre ordenada
            if funciones[x-1] in invocaciones[funcion]: 
                filas.append('{:^4}|'.format('x'))
                #veo si la funcion del primer for esta en las funciones llamadas de la funcion del segundo for 
                #si es llamada agrego una x a la fila 
            elif funcion in invocaciones[funciones[x-1]]:
                filas.append('{:^4}|'.format(invocaciones[funciones[x-1]][funcion]))
                total[funcion] += invocaciones[funciones[x-1]][funcion]
                #veo si la funcion del segundo for es llamada por la  funcion del primer for
                #si la llama agrego la cantidad de veces que la llama a la fila
                #voy sumando al total de la funcion recorrida las veces que llama a la funcion en la que estoy parada
            else:
                filas.append('{:^4}|'.format(''))
                #si no es llamada ni llama agrego un string vacio
         
    
    return nueva_fila,total

def crear_tabla(invocaciones,tabla,funciones):
    """
    [Autor : Sofia Marchesini]
    [Ayuda : Empiezo a crear la tabla]
    """
    x = len(funciones)
    primera_fila = ''
    t = 0
    total = {}
    nuevo = ''
    funciones = lista_de_funciones()
    
    for funcion in funciones:
        total[funcion] = 0
    nueva_fila,total = crear_filas(invocaciones, funciones,total)
    
    for i in range(1,x+1):
        primera_fila += '{:^4}|'.format(i)
    tabla.write('-'*41 + '-----'*x + '\n')
    tabla.write('|{:<40}|'.format('FUNCIONES') + primera_fila + '\n')
    #creo la primera fila con el string "funciones" y los numeros que indican las funciones en las columnas
        
    for filas,funcion in zip(nueva_fila,invocaciones.keys()):
        t+=1
        tabla.write('|' + '-'*40 + '|----'*x + '|\n')
        tabla.write('|{:<40}|'.format(str(t)+ '-' + funcion.replace('$','')) +''.join(filas)+ '\n' )
    tabla.write('|' + '-'*40 + '|----'*x + '|\n')
    #incluyo todas las filas creadas en crear_filas dentro de la tabla central
    
    for valor in total.values():
        nuevo += '{:^4}|'.format(str(valor))        
    tabla.write('|{:40}|'.format('Total Invocaciones')  + nuevo + '\n')
    tabla.write('|' + '-'*40 + '|----'*x + '|\n')
    #finalizo la tabla con la ultima fila que contiene el total de invocaciones

def imprimir_analizador():
    """
    [Autor : Sofia Marchesini]
    [Ayuda : imprimo la tabla y la copio al archivo analizador.txt]
    """
    fuente = open('fuente_unico.csv','r')
    analizador = open('analizador.txt','w+')
    invocaciones = funciones_invocadas(fuente)
    funciones = lista_de_funciones()
    crear_tabla(invocaciones,analizador,funciones)
    analizador.seek(0)
    fila = analizador.readline().strip()
    #leo las lineas del analizador ylas imprimo
    while fila != '':
        print(fila)
        fila = analizador.readline().rstrip()
    analizador.close()
    fuente.close()
    
