#!/usrbin/env python3 
"""
Panel general de Funciones
Mediante esta opción se debe mostrar por pantalla, una tabla con la siguiente información
por columna.
"""
from tabla import imprimir_panel
from generales import listar_archivo,acomodar_lectura
from archivos import grabar_archivo
def organizar_archivo(lista_ar):
    """[Autor: Lucia]"""
    """[Ayuda: Crea un diccionario donde la calve es el nombre de la funcion que a su vez tiene un diccionario adentro
        donde las claves son los atributos de las columnas]"""
    funciones = {}
    for funcion in lista_ar:
        funciones[funcion[0]] = {} # Estructura del dic
        funciones[funcion[0]]["Nombre"] = "{}.{}".format(funcion[0], funcion[2]) # nombre_funcion.modulo
        funciones[funcion[0]]["Parametros"] = funcion[1].strip('()')
        funciones[funcion[0]]["Lineas"] = len(funcion) - 3 #Por los parametros,el modulo y el nombre
        funciones[funcion[0]]["Invocaciones"] = 0
        funciones[funcion[0]]["return"] = 0
        funciones[funcion[0]]["if"] = 0
        funciones[funcion[0]]["elif"] = 0
        funciones[funcion[0]]["for"] = 0
        funciones[funcion[0]]["while"] = 0
        funciones[funcion[0]]["break"] = 0
        funciones[funcion[0]]["exit"] = 0
        funciones[funcion[0]]["Coment"] = 0
        funciones[funcion[0]]["Ayuda"] = ""
        funciones[funcion[0]]["Autor"] = ""

    return funciones

def contador (elementos, lista_ar, dic):
    """[Autor: Lucia]
        [Ayuda: Cuenta la cantidad de veces que aparece el elemento que se le le pasa por parametro]"""
    for elemento in elementos:
        for funcion in lista_ar:
            for i in range(3, len(funcion)): 
                dic[funcion[0]][elemento] += funcion[i].count(elemento + ' ')

    return dic

def parametros(lista_ar, dic):
    """[Autor: Lucia]"""
    """[Ayuda: Cuenta la cantidad de parametros]"""
    for key in dic:
        if dic[key]['Parametros'] == '':
            dic[key]['Parametros'] = 0
        else:
            cant = dic[key]["Parametros"].count(" ") # Utiliza 
            dic[key]["Parametros"] = cant + 1
    return dic


def extraigo_linea(funcion,key,dic):
    """ [Autor : Lucia]
        [Ayuda : Analizara las lineas de la funcion y devolvera
        un dic modificado]
        """
    funcion = funcion[3:len(funcion)]
    for linea in funcion:
        linea = linea.split()
        texto = ''+key+'('
        for elemento in linea:
            final = elemento[0:len(texto)]
            if final == texto:
                dic[key]['Invocaciones'] +=1 
    return dic

def invocaciones(lista_ar, dic):
    """[Autor: Lucia]
       [Ayuda: Cuenta la cantidad de veces que fue invocada cada funcion]"""
    for key in dic:
        # agarro una funcion
        for funcion in lista_ar:  
            funcion = acomodar_lectura(funcion,['='],' = ')
            extraigo_linea(funcion,key,dic)
    return dic

def lineas_coment(lista_ar, dic):
    """[Autor: Lucia]
       [Ayuda: cuenta las lineas de comentarios que no sean de autor o ayuda]"""
    for funcion in lista_ar:
        if (len(funcion) > 3):
            dic[funcion[0]]['Coment'] += len(funcion) -3
    return dic

def ayuda(lista_ar, dic):
    """[Autor: Lucia]
       [Ayuda: verifica si hay o no un comentario de ayuda dentro de la función]"""
    for funcion in lista_ar:
        if (funcion[2] == 'N/N'):
            dic[funcion[0]]['Ayuda'] = 'No'
        else:
            dic[funcion[0]]['Ayuda'] = 'Si'
    return dic

def autor(lista_ar, dic):
    """[Autor: Lucia]"""
    """[Ayuda: Indica el nombre del autor de la función]"""
    for funcion in lista_ar:
        dic[funcion[0]]['Autor'] = funcion[1]
    return dic

def unir(dic, lista_fu, lista_com):
    """[Autor: Lucia]"""
    """[Ayuda: Une todas las funciones contadoras con el diccionario]"""
    invocaciones(lista_fu, dic)
    contador(['for','while','break','exit','return','if','elif'], lista_fu, dic)
    parametros(lista_fu, dic)
    lineas_coment(lista_com, dic)
    ayuda(lista_com, dic)
    autor(lista_com, dic)
    return dic

def procesa_linea(valor,nombre,if_elif,archivo,valor_final):
    """[Autor : Nicolas]"""
    """[Ayuda : Funcion que graba la linea segun condiciones]"""
    if nombre == 'if' or nombre == 'elif':
        valor_final += valor
        if_elif.remove(nombre)
        if len(if_elif) == 0:
            leyenda = str(valor_final) + ','
            grabar_archivo(archivo,leyenda)
    else:            
        leyenda = str(valor) + ','
        grabar_archivo(archivo,leyenda)

    return if_elif


def panel_csv(dic):
    """[Autor : Nicolas]
       [Ayuda : Genera la escritura del archivo panel_general]"""
    archivo = open('panel_general.csv','w')
    lista = ['Funcion,','Parametros,','lineas,','invocaciones,','Returns,','If/Elif,','For,','While,','Break,','Exit,','Coment,','Ayuda,','Autor']
    for elemento in lista:
        archivo.write(elemento)
    archivo.write('\n')
    for funcion_principal in dic:
        if_elif = ['if','elif']
        valor_final = 0
        for valores in dic[funcion_principal]:
            valor = dic[funcion_principal][valores]
            # Esta funcion ejecutara todo el proceso para meter la linea en el archivo
            if_elif = procesa_linea(valor,valores,if_elif,archivo,valor_final)
        archivo.write('\n')
    archivo.close()


def panel_general(fuente_unico,comentarios):
    """[Autor: Lucia]"""
    """[Ayuda: ejecuta todo,es el main del programa]"""
    fuente_unico.seek(0)
    comentarios.seek(0)
    lista_fuente_unico = listar_archivo(fuente_unico)
    lista_comentarios = listar_archivo(comentarios)
    diccionario = organizar_archivo(lista_fuente_unico)
    dic_final = unir(diccionario, lista_fuente_unico, lista_comentarios)
    panel_csv(dic_final)
    imprimir_panel(dic_final)
