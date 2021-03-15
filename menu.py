#!/usr/bin/env python3
import os
from merge import archivos_merge
from panel_general import panel_general
from desarrollo_autor import info_desarrolladores
from reutilizacion import imprimir_analizador
from generales import validar_programa
from panelConsulta import panel_consultas
from arbol_de_invocacion import imprimir_diagrama

def texto_menu():
    print("""            1-Panel general de funciones
            2-Consulta de funciones
            3-Analizador de reutilización de código
            4-Árbol de invocación
            5-Información por desarrollador""")

def menu():
    """ [Autor : N/N]
        [Ayuda : Menu principal de nuestro programa]"""
    
    
    """ Esta es la funcion de menu principal de nuestro programa.
        Todo estara ejecutado desde aca.
    """
    vacio = validar_programa()
    if vacio != True:
        archivos_merge()
        fuente_codigo = open('fuente_unico.csv','r')
        comentarios = open('comentarios.csv','r')
        texto_menu()
        opcion = input('Ingrese una opcion: ')
        while opcion:
            while opcion not in '12345':
                opcion = input('Ingrese una opcion valida o enter para salir: ')
            borrador()
            if opcion == '':
                print('Gracias por participar de nuestro programa')
                exit()
            elif opcion == '1':
                panel_general(fuente_codigo,comentarios)
                enter = input('Ingrese enter para continuar')
            elif opcion == '2':
                panel_consultas(fuente_codigo, comentarios)
            elif opcion=='3':
                imprimir_analizador()
                enter = input("Ingrese enter para continuar")
            elif opcion=="4":
                imprimir_diagrama(fuente_codigo)
                enter = input("Ingrese enter para continuar")
            elif opcion=="5":
                info_desarrolladores(fuente_codigo,comentarios)
                enter = input("Ingrese enter para continuar")
            borrador()
            texto_menu()
            opcion = input('Ingrese una  opción o enter para salir: ')
        fuente_codigo.close()
        comentarios.close()
    else:
        print('\n\t\tATENCION [!]\n\n\tProgramas.txt ESTA VACIO\n')
        
def borrador():
    if os.name == 'posix':
        os.system ('clear')
    elif os.name == 'ce' or os.name == 'nt' or os.name == 'dos':
        os.system ('cls')
