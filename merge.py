#!/usr/bin/env python3
import csv
from os import remove
from generales import buscar_dato,acomodar_lectura,reemplazar_string,ordenamiento_insercion,tipo_archivos
from archivos import *

def guardar_archivo(archivo_aux, lista_archivos):
    """[Autor : Alejandro] 
    Ayuda : Lee archivo_aux.csv, extrae la informacion y realiza la mezcla respectiva 
    para luego eliminar archivo_aux.csv 
    """
    archivo_mezcla = tipo_archivos(lista_archivos[0])
    with open(archivo_mezcla,'w', newline='') as prestaciones:
        with open(archivo_aux,'r') as auxiliar:
            entrada = csv.reader(auxiliar)
            data = [fila for fila in entrada if fila]
            ordenado = sorted(data, key=lambda fila: fila[0])
            for fila in ordenado:
                salida = csv.writer(prestaciones,delimiter=',')
                salida.writerow(fila)
    remove(archivo_aux)

def mezcla(lista_archivos):
    """[Autor : Alejandro]"""
    """[Ayuda : Mezcla Archivos CSV's] """
    archivo_aux = 'archivo_aux.csv'
    with open(archivo_aux,'w') as unificado:
        for archivo in lista_archivos:
            with open(archivo,'r') as arch:
                linea = leer_linea(arch).strip().split(',')
                while linea[0]!='':
                    entrada = csv.writer(unificado)
                    entrada.writerow(linea)
                    linea = leer_linea(arch).strip().split(',')
    guardar_archivo(archivo_aux,lista_archivos)

def separador_archivos(lista_archivos):
    """ Autor : Alejandro """
    """ Ayuda : Esta función recibe una lista con comentarios y fuente, divide en dos listas acorde al nombre respectivo """
    comentarios = []
    fuente_unico = []
    
    for ruta in lista_archivos:
        if 'comentarios' in ruta:
            comentarios.append(ruta)
        else:
            fuente_unico.append(ruta)    
    mezcla(comentarios)
    mezcla(fuente_unico)

def indice_vaciado(lista_datos, lista_borrar):
    """[Autor : Nicolas]
        Ayuda : Esta funcion recibira una lista con datos que podra
            ir borrando y cuando este vacia devolvera el indice donde se
            vacio por completo. 
    """
    i=0
    while i<len(lista_datos) and len(lista_borrar)>0:
        if lista_datos[i] in lista_borrar:
            lista_borrar.remove(lista_datos[i])
        i+=1
    return i

def analisis_linea(linea, linea_comentarios , linea_fuente,palabras_buscadas,palabras_faltantes):
    """ [Autor : Nicolas] """
    """ [Ayuda : Se le pasa una lista con las palabras encontradas y se fija si realmente alguna esta] """         
    if 'Autor' in palabras_buscadas and 'Ayuda' in palabras_buscadas:
        palabras_faltantes.extend(['Autor','Ayuda'])
        """
        ACLARACION : la funcion indice vaciado va a darme el indice en el cual 
        encuentra ambas palabras en la lista, para separarlas.Ya sabiendo que 
        ambas se van a encontrar,pero solo si estan las dos juntas en la misma 
        lista.
        """
        i = indice_vaciado(linea,['Ayuda','Autor'])
        linea_segunda = linea[i-1:len(linea)]
        linea_primera = linea[0:i-1]
        # Lo hago en cada una porque sino me corre el indice anterior.
        linea_primera = acomodar_lectura(linea_primera,['Autor','Ayuda','"""',','],'')
        linea_segunda = acomodar_lectura(linea_segunda,['Autor','Ayuda','"""',','],'')
        linea = ' '.join(linea_primera).strip()
        linea_comentarios.insert(1,linea)
        linea = ' '.join(linea_segunda).strip()
        linea_comentarios.insert(2,linea)
    elif 'Autor' in palabras_buscadas :
        palabras_faltantes.append('Autor')
        union = acomodar_lectura(linea,['"""','[',']','Autor',':'],'')
        linea = ' '.join(union).strip()
        linea_comentarios.insert(1,linea)
    elif 'Ayuda' in palabras_buscadas:
        palabras_faltantes.append('Ayuda')
        union = acomodar_lectura(linea,['"""','[',']','Ayuda',':'],'')
        linea = ' '.join(union).strip()
        linea_comentarios.insert(2,linea)
    elif '#' in palabras_buscadas or'"""'in palabras_buscadas:
        linea_fuente,linea_comentarios = comentarios(linea,linea_comentarios,linea_fuente)
    
    return linea_fuente,linea_comentarios,palabras_faltantes

def reunir_parametros(linea):
    """ [Autor : Nicolas] """
    """ [Ayuda : Reune los parametros necesarios]
        """
    nueva_lista=[]
    for x in range (2,len(linea)):
        nueva_lista.extend([linea[x]])
    nueva_lista = acomodar_lectura(nueva_lista,[','],' ')
    final = ' '.join(nueva_lista)

    return final
      
def proceso_archivos(nombre_modulo, archivo) :
    """ [Autor : Nicolas] """
    """ [Ayuda : Va a validar las lineas del archivo para saber 
        a cual de las dos salidas (comentarios y fuente unico) va a ir] 
        """
    funciones_fuente = [] # Aca iran a parar las funciones para fuente codigo 
    funciones_comentarios = [] # Y aca las funciones para comentarios
    ultima_lectura = leer_linea(archivo)
    while ultima_lectura:
        ultima_lectura = ultima_lectura.strip().split()
        if len(ultima_lectura)>0 and ultima_lectura[0] == 'def':
            # Analizaremos la funcion y la dividiremos en dos listas para saber a que archivo pertenecen.
            ultima_lectura = acomodar_lectura(ultima_lectura,['('],' (')
            ultima_lectura = acomodar_lectura(ultima_lectura,[':'],'')
            #Reuno los parametros
            parametros = reunir_parametros(ultima_lectura)
            nombre_funcion = ultima_lectura[1]
            parametros = reemplazar_string(',',' ',parametros)
            linea_fuente = [nombre_funcion,parametros,nombre_modulo]
            linea_comentarios = [nombre_funcion]
            # Luego de desmenuzar los datos obligatorios, entro al analisis de la funcion.
            linea_comentarios,linea_fuente,ultima_lectura = analizador_funcion(linea_fuente,linea_comentarios,archivo)
            funciones_fuente.append(linea_fuente)
            funciones_comentarios.append(linea_comentarios)
        else:#Si no es un def no es una funcion.Probablemente sea un from o un bloque principal.El enunciado no pide analizarlo.
            ultima_lectura = leer_linea(archivo)
    return ordenamiento_insercion(funciones_fuente),ordenamiento_insercion(funciones_comentarios)

def analizador_funcion(linea_fuente,linea_comentarios,archivo):
    """[Autor : Nicolas ]"""
    """[Ayuda : Analizara la funcion para enviarla a las listas correspondientes]"""
    lectura = leer_linea(archivo)
    
    #Si sale de este while, esta por empezar otra funcion o leyo el fin de archivo.
    palabras_faltantes = []
    while lectura and 'def'!= lectura[0:3] :
        lectura = lectura.strip().split()
        """ 
        La utilidad que le doy a acomodar_lectura es a limpiar un poco el texto.
        Se acomoda mejor en las listas y no quedan cosas pegadas a las palabras,
        que pueden complicar la comprension del texto cuando quiera buscar datos.
        """
        lectura = acomodar_lectura(lectura,[',','[',']',':'],' ')
        lectura = acomodar_lectura(lectura,['"""'],'""" ')
        lectura = acomodar_lectura(lectura,['#'],'# ')
        lectura = acomodar_lectura(lectura,['main()'],'')
        cuento = lectura.count('"""')
        """ 
        Preguntare si abrio una triple comillas 
        y nunca lo cerro. Eso nos estaria diciendo que el comentario
        no finalizo.
        """

        while cuento == 1:
            
            segunda_lectura = leer_linea(archivo).strip().split()
            segunda_lectura = acomodar_lectura(segunda_lectura,[','],'')
            segunda_lectura = acomodar_lectura(segunda_lectura,[']','[',':'],' ') 
            segunda_lectura = acomodar_lectura(segunda_lectura,['"""'],' """')
            lectura.extend(segunda_lectura)
            cuento = lectura.count('"""')
            """ En caso que en la nueva extension de las lecturas haya una nueva triple
                comillas, se entiende que cerro el comentario."""
        lectura = acomodar_lectura(lectura,['[',']',':'],'')
        encontradas = buscar_dato(['Ayuda','Autor','#','"""'],lectura)
        linea_fuente,linea_comentarios,palabras_faltantes = analisis_linea(lectura,linea_comentarios,linea_fuente,encontradas,palabras_faltantes)
        if len(encontradas) == 0 and lectura:
            linea_fuente.append(' '.join(lectura))
        lectura = leer_linea(archivo)
    linea_comentarios = encontrar_palabras(palabras_faltantes,linea_comentarios)
    
    return linea_comentarios,linea_fuente,lectura

def encontrar_palabras(palabras,linea_comentarios):
    """ [Autor : Nicolas]"""
    if 'Autor' not in palabras:
        linea_comentarios.insert(1,'N/N')
    if 'Ayuda' not in palabras:
        linea_comentarios.insert(2,'N/N')
    """[Ayuda: Encuentra las palabras autor o ayuda o le pone N/N para que se note la falta de un autor]"""
    return linea_comentarios

def comentarios(lectura, lista_comentarios, lista_fuente) :
    """
        [Ayuda : Este es el sector que corresponderia al analisis de la linea del archivo 
            que corresponde a comentarios]
    """
    
    i = 0
    encontro = False # Esto es condición para que cuando encuentre la almohadilla salga del while
    
    while i<len(lectura) and encontro == False:
        elemento = lectura[i]
        if elemento == '#' and i>0 :
            # Si entro aca es porque el comentario es entre medio de una linea.
            encontro = True
            comentario = lectura[i:len(lectura)]
            fuente_unico = lectura[0:i]
            comentario = acomodar_lectura(comentario,['#'],'')
            lista_fuente.append(' '.join(fuente_unico))
            lista_comentarios.append(' '.join(comentario))
        
        elif elemento == '#' and i==0 :
            encontro = True
            lectura = acomodar_lectura(lectura,['#'],'')
            lista_comentarios.append(' '.join(lectura))
        elif elemento == '"""' and i==0:
            lectura = acomodar_lectura(lectura,['"""'],'')
            lista_comentarios.append(' '.join(lectura))
        i+=1
    """ [Autor : Nicolas]"""
    return lista_fuente,lista_comentarios

def eliminar_archivos(archivos):
    """ [Autor : Nicolas]
        [Ayuda : Elimina archivos del directorio]"""
    
    for archivo in archivos:
        remove(archivo)

def archivos_merge () :
    """ [Autor : Nicolas]"""
    """[Ayuda : Esta funcion inicia el proceso de archivos]"""
    
    # Esta funcion guardará cada archivo ordenado en una lista
    
    lista_archivos = []
    rutas = open('programas.txt', 'r')
    ruta = leer_linea(rutas).strip()
    i = 0
    while ruta :
        i+=1 #Este indice lo creo para distinguir los archivos
        nombre_archivo = ruta.split('/').pop()
        nombre_archivo = nombre_archivo[0:len(nombre_archivo)-3]

        #Abro ruta dentro de programas.txt
        
        codigo = open(ruta,'r',encoding = 'utf8')
        fuente_unico,comentarios = proceso_archivos(nombre_archivo,codigo)
        ruta_fuente = 'fuente_unico'+str(i) +'.csv'
        ruta_comentarios = 'comentarios'+str(i) +'.csv'
        generar_archivo(fuente_unico,ruta_fuente)
        generar_archivo(comentarios,ruta_comentarios)
        lista_archivos.append(ruta_fuente)
        lista_archivos.append(ruta_comentarios)
        ruta = leer_linea(rutas).strip()
    """Finalizado el proceso del codigo, entraremos a 
        la mezcla final.
        """
    separador_archivos(lista_archivos)
    #Por ultimo borramos los archivos creados antes de la mezcla,
    eliminar_archivos(lista_archivos)
