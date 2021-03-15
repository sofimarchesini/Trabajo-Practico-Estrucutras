from archivos import leer_linea
def listar_archivo (archivo):
    """ [Autor : Lucia] """
    """ [Ayuda : convierte al archivo en una lista donde cada elemento es una linea del mismo] """
    lista_ar = []
    linea = leer_linea(archivo)
    linea = (linea)
    while linea:
        lista_ar.append(linea.rstrip('\n').split(','))
        linea = leer_linea(archivo)
    return lista_ar

def tipo_archivos (archivo):
    """ Autor : Alejandro """
    """ Ayuda : valida si el archivo recibido es comentarios o fuente_unico """
    if 'comentarios' in archivo:
        archivo_unico = 'comentarios.csv'
    else:
        archivo_unico = 'fuente_unico.csv'
    return archivo_unico

def buscar_dato (lista_datos,linea):
    """ [Autor : Nicolas] """
    """ [Ayuda : Se le pasa una lista con datos a buscar en la linea del archivo] """

    encontradas = []

    for palabra in lista_datos:
        if palabra in linea:
            encontradas.append(palabra)
    return encontradas

def acomodar_lectura (lista,elementos_reemplazados,reemplazo):
    """ [ Autor : Nicolas] """
    """  [Ayuda : Reemplaza en una lista todos sus elementos] """

    lista_reemplazada = []

    for elemento in lista:
        elemento = reemplazar_string(elementos_reemplazados,reemplazo,elemento).split()
        lista_reemplazada.extend(elemento)
    return lista_reemplazada

def ordenamiento_insercion (lista) :

    """ [Autor : Nicolas] """
    """ [ Ayuda : Algoritmo de ordenamiento por insercion visto en clase] """
    for indice in range(1,len(lista)):
        valor = lista[indice]
        i = indice-1
        variable = True
        while i >= 0 and variable == True:
            if valor<lista[i]:
                lista[i+1] = lista[i]
                lista[i] = valor
                i = i-1
            else:
                variable = False
    return lista

def reemplazar_string (reemplazar,reemplazo,string):
    
    """ [ Autor : Nicolas] """
    """ [Ayuda : Con la funcion replace reemplazaremos los datos del parametro reemplazar
        con otro parametro reemplazo] """
    
    for elemento in reemplazar:
        string=string.replace(elemento,reemplazo)
    return string

def validar_programa ():

    """ [ Autor : Alejandro] """
    """ [Ayuda : Preguntaremos si hay alguna ruta en programas.txt] """

    archivo = open('programas.txt')
    linea = archivo.readline()
    validacion = False
    if not linea:
        validacion = True
    archivo.close()
    return validacion













