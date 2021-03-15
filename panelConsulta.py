#!/usr/bin/env python3
from generales import reemplazar_string
from archivos import leer_linea_clasico,buscar_funciones
from tabla import formato_interrogacion,formato_numeral,imprimir_todo,tabla_consultas

def opcion_todo (nombre, archivo_funciones, archivo_comentarios):
    """[Autor: Juan Godoy]"""
    """[Ayuda : Funcion que imprime todo lo relacionado con las funciones ?todo, '#'todo,e imprimir ?todo]"""
    ayuda_funciones = open('ayuda_funciones.txt', 'w') 
    archivo_funciones.seek(0)
    archivo_comentarios.seek(0)
    
    lista_funciones = leer_linea_clasico(archivo_funciones, ',')
    lista_comentarios = leer_linea_clasico(archivo_comentarios, ',')
    #Se recorre todo el archivo secuencialmente para ir imprimiendo linea por linea segun el formato elegido.
    while lista_funciones[0] != '':
        if nombre == '?todo':
            formato_interrogacion(lista_funciones, lista_comentarios)
        elif nombre=='imprimir ?todo':
            imprimir_todo(ayuda_funciones, lista_funciones, lista_comentarios)
        else:
            formato_numeral(lista_funciones, lista_comentarios)
        lista_comentarios = leer_linea_clasico(archivo_comentarios, ',')
        lista_funciones = leer_linea_clasico(archivo_funciones, ',')
    ayuda_funciones.close()
    return 
    

def opciones_funcion(valor, archivo_funciones, archivo_comentarios):
    """[Autor : Juan Godoy]"""
    """[Ayuda : Segun la opcion que se elija, se imprime diferente informacion sobre las funciones]"""
    nombre_funcion = reemplazar_string([valor[-1]],'',valor)
    #nombre_funcion = valor.replace(valor[-1], '')
        
    archivo_comentarios.seek(0)
    archivo_funciones.seek(0)
        
    lista_comentarios = buscar_funciones(archivo_comentarios, nombre_funcion)
    lista_funciones = buscar_funciones(archivo_funciones, nombre_funcion)
    #Mira con que finaliza la funcion e imprime el formato que corresponda.
    if (valor.endswith('?')) and (lista_comentarios[0]!='') and (lista_funciones[0]!=''):
        formato_interrogacion(lista_funciones, lista_comentarios)
    elif (valor.endswith('#')) and (lista_comentarios[0]!='') and (lista_funciones[0]!=''):
        formato_numeral(lista_funciones, lista_comentarios)
    else:
         print('\nPorfavor ingrese un nombre de funcion seguido de un signo valido. \n')
        
        
def panel_consultas(fuente_unico, comentarios):
    """[Autor : Juan Godoy]"""
    """[Ayuda : Funcion principal que pide el ingreso de una funcion y segun la opcion que elijas, imprime diversas cosas]"""
    
    tabla_consultas(comentarios)
    print('  ?todo o #todo : Muestra Informacion para cada una de la funciones que se muestra en pantalla\n  imprimir ?todo: enviar contenido de funciones a un archivo, respete el espacio entre palabra y simbolo\n\n  Enter para salir')
    valor_solicitado = input('\nFunción: ')
    #Mientras no se de enter, se va iterando en dos conjuntos de opciones, las que imprimen todo el archivo o la que busca funciones especificas.
    while valor_solicitado:
        if valor_solicitado == 'imprimir ?todo' or valor_solicitado == '?todo' or valor_solicitado == '#todo':
            opcion_todo(valor_solicitado, fuente_unico, comentarios)
        else:
            opciones_funcion(valor_solicitado,fuente_unico, comentarios)
        print('  ?todo o #todo : Muestra Informacion para cada una de la funciones que se muestra en pantalla\n  imprimir ?todo: enviar contenido de funciones a un archivo,respete el espacio entre palabra y simbolo\n\n  Enter para salir')
        valor_solicitado = input('\nFunción: ')



    

    

