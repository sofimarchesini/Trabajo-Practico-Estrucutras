from reutilizacion import funciones_invocadas, crear_filas 
from generales import listar_archivo
from archivos import leer_linea_clasico

def busca_principal(dic):
    """[Autor: Lucia]"""
    """[Ayuda: Busca la función principal de un programa]"""
    principal = ''   
    valores = list(dic.values())
    for key in dic.keys():
        contador = 0
        posible_principal = ''
        while (len(valores) > contador) and (key not in list(valores[contador].keys())):
            posible_principal = key
            if (contador == len(valores) - 1):
                principal = posible_principal
            contador += 1   
    return principal


def cant_lineas(lista_ar_fu):
    """[Autor: Lucia]"""
    """[Ayuda: Cuenta la cantidad de lineas por funcion]"""
    
    dic = {}
    for funcion in lista_ar_fu:
        dic[funcion[0]] = (len(funcion) - 2)
        
    return dic

def imprimir_diagrama(fuente_unico): 
    """[Autor : Sofia Marchesini]"""
    """[Ayuda : este codigo permite imprimir las funciones main
        con sus respectivas funciones invocadas y las funciones que a su vez
        estas invocan y asi sucesivamente]"""
    
    fuente_unico.seek(0)
    lista_ar = listar_archivo(fuente_unico)
    fuente_unico.seek(0)
    dic_lineas = cant_lineas(lista_ar)
    diccionario = funciones_invocadas(fuente_unico)
    principal = busca_principal(diccionario)
    string = ""
    
    string_principal = " {} ({})".format(principal,dic_lineas[principal])
    for i in range (len(diccionario[principal].keys())):
        if i == 0:
            recursiva(diccionario,string_principal,list(diccionario[principal].keys())[i],dic_lineas,principal,string)
        elif list(diccionario[principal].keys())[i]:
            recursiva(diccionario," "*len(string_principal),list(diccionario[principal].keys())[i],dic_lineas,principal,string)
        
def recursiva(diccionario,espaciado,funcion,dic_lineas,principal,string):

    string = "{} --> {} ({})".format(espaciado,funcion,dic_lineas[funcion])
    
    if len(list(diccionario[funcion].keys())) == 0:
        print(string)
    
    for c in range(len(diccionario[funcion].keys())):
        if list(diccionario[funcion].keys())[c] == funcion:
            print("{} --> {} ({})".format(string,funcion,dic_lineas[funcion]))
        elif c == 0:
            recursiva(diccionario,string,list(diccionario[funcion].keys())[c],dic_lineas,principal,string)
        else:
            recursiva(diccionario," "*len(string),list(diccionario[funcion].keys())[c],dic_lineas,principal,string)

