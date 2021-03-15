#!/usr/bin/env python3
from archivos import  leer_linea, leer_linea_clasico,formateo_linea

def imprimir_panel(dic):
    """[Autor: Lucia]"""
    """[Ayuda: Crea la una tabla]"""
    Tabla = """ \
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|        FUNCION                        Parametros---Líneas---Invocaciones---Returns---If/elif---for---while---Break---Exit---Coment---Ayuda---Autor                |
--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
{}
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+\ 
"""
    Tabla = (Tabla.format('\n'.join('|{0:32}\t{1:5}\t{2:8}\t{3:5}\t{4:9}\t{5:4}\t{6:4}\t{7:3}\t{8:3}\t{9:3}\t{10:3}\t{11:1}\t{12:20}|'.format(dic[funcion]['Nombre'], dic[funcion]['Parametros'], 
                                                                                                                            dic[funcion]['Lineas'],
                                                                                                                            dic[funcion]['Invocaciones'], dic[funcion]['return'],
                                                                                                                            dic[funcion]['if'] + dic[funcion]['elif'], dic[funcion]['for'], 
                                                                                                                            dic[funcion]['while'], dic[funcion]['break'], 
                                                                                                                            dic[funcion]['exit'], dic[funcion]['Coment'],
                                                                                                                            dic[funcion]['Ayuda'], dic[funcion]['Autor'])
     for funcion in dic)))
    print (Tabla)

def tabla_consultas(archivo):
    """[Autor : Juan Godoy]"""
    """[Ayuda : Funcion que acumula nombres de funciones para luego dibujarlas en una tabla]"""
    contador = 0
    archivo.seek(0)
    nueva_lista = []
    linea = leer_linea_clasico(archivo, ',')
    print('{}'.format('\tFunciones:\n'.expandtabs(1)))
    print(' ----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    while linea[0]!='' or nueva_lista[0]!='':
        if contador!=5:
            nueva_lista.append(linea[0])
            contador+=1
        else:
            espaciador1 = 32-len(nueva_lista[0])
            espaciador2 = 32-len(nueva_lista[1])
            espaciador3 = 32-len(nueva_lista[2])
            espaciador4 = 32-len(nueva_lista[3])
            espaciador5 = 32-len(nueva_lista[4])
            print(' |{0}{5}|{1}{6}|{2}{7}|{3}{8}|{4}{9}|'.format(nueva_lista[0], nueva_lista[1], nueva_lista[2], nueva_lista[3],nueva_lista[4],
                                                                '\t'.expandtabs(espaciador1),'\t'.expandtabs(espaciador2),'\t'.expandtabs(espaciador3),'\t'.expandtabs(espaciador4), '\t'.expandtabs(espaciador5)))
            nueva_lista = []
            contador=0
            nueva_lista.append(linea[0])
        linea = leer_linea_clasico(archivo, ',')
    print(' ----------------------------------------------------------------------------------------------------------------------------------------------------------------------')

def imprimir_todo(archivo, lista_funcion, lista_comentarios):
    """[Autor : Juan Godoy]"""
    """[Ayuda : imprime en un archivo .txt lo relacionado con la opcion ?]"""
    if len(lista_funcion[1])>80 or len(lista_comentarios[2])>80:
        lista_funcion[1] = formateo_linea(lista_funcion[1])
        lista_comentarios[2] = formateo_linea(lista_comentarios[2])
    archivo.write('-------------------------------------------------\n')
    archivo.write('Función: {0}\r\nAyuda: {1}\r\nParametros: {2}\r\nModulo: {3}\r\nAutor: {4}\n'.format(lista_funcion[0], lista_comentarios[2], lista_funcion[1], lista_funcion[2], lista_comentarios[1]))
    archivo.write('-------------------------------------------------\n')

def formato_interrogacion(lista_funciones, lista_comentarios):
    """[Autor: Juan Godoy]"""
    """[Ayuda : Un formato visual para las opciones con interrogacion]"""
    print('-------------------------------------------------')
    print('Función: {0}\r\nAyuda: {1}\r\nParametros: {2}\r\nModulo: {3}\r\nAutor: {4}'.format(lista_funciones[0], lista_comentarios[2], lista_funciones[1], lista_funciones[2], lista_comentarios[1]))
    print('----------------------------------')

def formato_numeral(lista_funciones, lista_comentarios):
    """[Autor : Juan Godoy]"""
    """[Ayuda : Formato visual para las opciones numeral]"""
    n = 3
    m = 2
    print('-------------------------------------------------')
    print('Función: {0}\nParametros: {1}\nModulo: {2}\nAutor: {3}\nDescripcion:{4}\nExtra: '.format(lista_funciones[0],lista_funciones[1],lista_funciones[2],lista_comentarios[1],lista_comentarios[2]))
    while (len(lista_funciones) != n):
        print(lista_funciones[n])
        n += 1
    while len(lista_comentarios) != m:
        print(lista_comentarios[m])
        m += 1
    return

def imprimir_tabla_desarrollador(participacion):
    """[Autor : Alejandro]
       [Ayuda : Imprime la tabla para desarrollador]"""
    informacion = open(participacion,'r')
    linea = informacion.readline()
    print(linea)
    while linea != '':
        print(linea)
        linea = informacion.readline()
    informacion.close()
            
def carga_informacion_desarrollador(dicc_desarrolladores,total_lineas):
    """[Autor : Alejandro]"""
    total_desarrollador = 0
    participacion = 'participacion.txt'
    with open(participacion,'w') as informe:
        total_funciones = 0
        linea = '-'*50
        informe.write('\n\tInforme de Desarrollo por Autor'+'\n')
        for autor,funciones in dicc_desarrolladores.items():
            acum_lineas = 0
            cant_funciones_desarrollador = 0
            informe.write('\n'+linea)
            informe.write('\n\nAutor:  {}\n'.format(autor))
            informe.write('{:>30}\t\t{}\n'.format('Función','Lineas'))
            informe.write(linea+'\n')
            lista_funciones = sorted(funciones, key= lambda funcion:funcion[1])
            total_funciones += len(lista_funciones)
            for data in lista_funciones:
                cant_funciones_desarrollador += 1
                acum_lineas += data[1]
                informe.write('{:>30}\t\t{}'.format(data[0],data[1])+'\n')
                porcentaje=(acum_lineas*100)//total_lineas
            informe.write('\t{} Funcion/es - Lineas\t\t{}  {}%'.format(cant_funciones_desarrollador,acum_lineas,porcentaje))
        informe.write('\n\nTotal Funciones {} - Lineas {}'.format(total_funciones,total_lineas)+'\n')
    imprimir_tabla_desarrollador(participacion)

