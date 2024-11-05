import time
from DataStructures.Tree import binary_search_tree as bst
import csv
from datetime import datetime
from DataStructures.List import array_list as ar

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog= {"treq1": bst.new_map(), "treq2": bst.new_map(), "treq3": bst.new_map(), "treq4": bst.new_map(),
              "treq5": bst.new_map(), "treq6": bst.new_map(), "treq7": bst.new_map()}
    return catalog

# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    accidentes = csv.DictReader(open(filename, encoding='utf-8'))
    for accidente in accidentes:
        accidente["duracion en horas"]= 0
        if accidente["Start_Time"] is None:
            start_time= "Desconocido"
            accidente["duracion en horas"]= None
        else:
            start_time = datetime.strptime(accidente["Start_Time"], '%Y-%m-%d %H:%M:%S')
        if accidente["End_Time"] is None:
            end_time="Desconocido"
            accidente["duracion en horas"]= None
        else:
            end_time = datetime.strptime(accidente["End_Time"], '%Y-%m-%d %H:%M:%S')
        accidente["Start_Time"]= start_time
        accidente["End_Time"]= end_time
        if accidente["duracion en horas"] is not None:
            diferencia = accidente["End_Time"] - accidente["Start_Time"]
            horas = diferencia.total_seconds() / 3600
            accidente["duracion en horas"]= horas
        if accidente["duracion en horas"] is None:
            accidente["duracion en horas"]="Desconocido"
        if accidente["End_Lat"]=="":
           accidente["End_Lat"]=accidente["Start_Lat"] 
        if accidente["End_Lng"]=="":
           accidente["End_Lng"]=accidente["Start_Lng"] 
        if accidente["City"]=="":
            accidente["City"]="Desconocido"
        if accidente["State"]=="":
            accidente["State"]="Desconocido"
        if accidente["Description"]=="":
            accidente["Description"]="Desconocido"
        if accidente["Visibility(mi)"]=="":
            accidente["Visibility(mi)"]=0
        
        keytreq1= accidente["Start_Time"]
        if bst.contains(catalog["treq1"], keytreq1)== False:
            lista=ar.new_list()
            lista= ar.add_last(lista, accidente)
            bst.put(catalog["treq1"], keytreq1, lista)
        else:
            lista = bst.get(catalog["treq1"], keytreq1)
            lista  = ar.add_last(lista, accidente)
            bst.put(catalog["treq1"], keytreq1, lista)
          
          
        if int(accidente["Severity"])==4:   
            keytreq2= float(accidente["Visibility(mi)"])
            if bst.contains(catalog["treq2"], keytreq2)== False:
                bst.put(catalog["treq2"], keytreq2, bst.new_map())
            keytreq2sub= accidente["State"]
            if bst.contains(bst.get(catalog["treq2"], keytreq2), keytreq2sub)== False:
                lista=ar.new_list()
                lista= ar.add_last(lista, accidente)
                bst.put(bst.get(catalog["treq2"], keytreq2), keytreq2sub, lista)
            else:
                lista = bst.get(bst.get(catalog["treq2"], keytreq2), keytreq2sub)
                lista  = ar.add_last(lista, accidente)
                bst.put(bst.get(catalog["treq2"], keytreq2), keytreq2sub, lista)
                    
       
        if int(accidente["Severity"])>=3 and ("rain" in accidente["Weather_Condition"] or "snow" in accidente["Weather_Condition"]) and float(accidente["Visibility(mi)"])<2:   
            keytreq3= accidente["Start_Time"]
            if bst.contains(catalog["treq3"], keytreq3)== False:
                lista=ar.new_list()
                lista= ar.add_last(lista, accidente)
                bst.put(catalog["treq3"], keytreq3, lista)
            else:
                lista = bst.get(catalog["treq3"], keytreq3)
                lista  = ar.add_last(lista, accidente)
                bst.put(catalog["treq3"], keytreq3, lista)           
        
        if int(accidente["Severity"])>=3 and float(accidente["Visibility(mi)"])<1:
            keytreq4= accidente["Start_Time"]
            if bst.contains(catalog["treq4"], keytreq4)== False:
                bst.put(catalog["treq4"], keytreq4, bst.new_map())   
            keytreq4sub= accidente["Street"]
            if bst.contains(bst.get(catalog["treq4"], keytreq4), keytreq4sub)== False:
                lista=ar.new_list()
                lista= ar.add_last(lista, accidente)
                bst.put(bst.get(catalog["treq4"], keytreq4), keytreq4sub, lista)
            else:
                lista = bst.get(bst.get(catalog["treq4"], keytreq4), keytreq4sub)
                lista  = ar.add_last(lista, accidente)
                bst.put(bst.get(catalog["treq4"], keytreq4), keytreq4sub, lista)
                
        if int(accidente["Severity"])>=3:
            fecha= accidente["Start_Time"]
            solo_fecha = fecha.date()
            keytreq5= solo_fecha
            if bst.contains(catalog["treq5"], keytreq5)== False:
                bst.put(catalog["treq5"], keytreq5, bst.new_map()) 
            keytreq5sub= accidente["Weather_Condition"]
            if bst.contains(bst.get(catalog["treq5"], keytreq5), keytreq5sub)== False:
                lista=ar.new_list()
                lista= ar.add_last(lista, accidente)
                bst.put(bst.get(catalog["treq5"], keytreq5), keytreq5sub, lista)
            else:
                lista = bst.get(bst.get(catalog["treq5"], keytreq5), keytreq5sub)
                lista  = ar.add_last(lista, accidente)
                bst.put(bst.get(catalog["treq5"], keytreq5), keytreq5sub, lista)
                
        if int(accidente["Severity"])>=3:
            keytreq6= accidente["Start_Time"]
            if bst.contains(catalog["treq6"], keytreq6)== False:
                bst.put(catalog["treq6"], keytreq6, bst.new_map())
            keytreq6sub= accidente["Humidity(%)"]
            if bst.contains(bst.get(catalog["treq6"], keytreq6), keytreq6sub)== False:
                bst.put(bst.get(catalog["treq6"], keytreq6), keytreq6sub, bst.new_map())
            keytreq6subsub= accidente["County"]
            if bst.contains(bst.get(bst.get(catalog["treq6"], keytreq6), keytreq6sub), keytreq6subsub)== False:
                lista=ar.new_list()
                lista= ar.add_last(lista, accidente)
                bst.put(bst.get(bst.get(catalog["treq6"], keytreq6), keytreq6sub), keytreq6subsub, lista)
            else:
                lista = bst.get(bst.get(bst.get(catalog["treq6"], keytreq6), keytreq6sub), keytreq6subsub)
                lista  = ar.add_last(lista, accidente)
                bst.put(bst.get(bst.get(catalog["treq6"], keytreq6), keytreq6sub), keytreq6subsub, lista)
                
    return catalog 
# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog, p_start, p_end):
    """
    Retorna el resultado del requerimiento 1
    """
    f_inicial = datetime.strptime(p_start, "%Y-%m-%d %H:%M:%S") #conversión a formato adecuado
    f_final = datetime.strptime(p_end, "%Y-%m-%d %H:%M:%S") #conversión a formato adecuado
    n_cumplen = 0
    lista_accidentes = ar.new_list()
    
    def filtro_intervalo(nodo): #función auxiliar recursiva para cada nodo/sub-arbol
        nonlocal n_cumplen, lista_accidentes #elimina el error de referenciación
        
        if nodo is None:
            return    
        fecha_accidente = nodo["key"] #Llaves son las fechas, asignadas desde el load_data
        accidentes = nodo["value"]
        print("ACCIDENTES: ")
        print(accidentes)      
        ar.add_last(lista_accidentes, accidentes) 
         
        if f_inicial <= fecha_accidente <= f_final: #filtra el intervalo de las fechas parámetro     
            n_cumplen += len(accidentes)           
        if fecha_accidente > f_inicial:
            filtro_intervalo(nodo["left"]) #evalúa por qué dirección del arbol debe continuar      
        if fecha_accidente < f_final:
            filtro_intervalo(nodo["right"]) #evalúa por qué dirección del arbol debe continuar
    filtro_intervalo(catalog["treq1"]["root"])
    
    return n_cumplen, lista_accidentes

            
        
    
    


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
