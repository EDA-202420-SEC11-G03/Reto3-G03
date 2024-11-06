import time
from DataStructures.Tree import binary_search_tree as bst
import csv
from datetime import datetime
from DataStructures.List import array_list as ar

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
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
    listadeaccientes= ar.new_list()

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
        ar.add_last(listadeaccientes, accidente)
        
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
            keytreq2= accidente["State"]
            if bst.contains(catalog["treq2"], keytreq2)== False:
                bst.put(catalog["treq2"], keytreq2, bst.new_map())
            keytreq2sub = float(accidente["Visibility(mi)"])
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
                
                
                
        keytreq7= accidente["Start_Lat"]
        if bst.contains(catalog["treq7"], keytreq7)== False:
            bst.put(catalog["treq7"], keytreq7, bst.new_map())
        keytreq7sub= accidente["Start_Lng"]
        if bst.contains(bst.get(catalog["treq7"], keytreq7), keytreq7sub)== False:
            bst.put(bst.get(catalog["treq7"], keytreq7), keytreq7sub, bst.new_map())
        keytreq7subsub= accidente["End_Lat"]
        if bst.contains(bst.get(bst.get(catalog["treq7"], keytreq7), keytreq7sub), keytreq7subsub)== False:
            bst.put(bst.get(bst.get(catalog["treq7"], keytreq7), keytreq7sub), keytreq7subsub, bst.new_map())
        keytreq7subsubsub= accidente["End_Lng"] 
        if bst.contains(bst.get(bst.get(bst.get(catalog["treq7"], keytreq7), keytreq7sub), keytreq7subsub), keytreq7subsubsub) == False:
            lista = ar.new_list()
            lista = ar.add_last(lista, accidente)
            bst.put(bst.get(bst.get(bst.get(catalog["treq7"], keytreq7), keytreq7sub), keytreq7subsub), keytreq7subsubsub, lista)
        else:
            lista = bst.get(bst.get(bst.get(bst.get(catalog["treq7"], keytreq7), keytreq7sub), keytreq7subsub), keytreq7subsubsub)
            lista = ar.add_last(lista, accidente)
            bst.put(bst.get(bst.get(bst.get(catalog["treq7"], keytreq7), keytreq7sub), keytreq7subsub), keytreq7subsubsub, lista)           
    primeros= listadeaccientes["elements"][:5]
    ultimos= listadeaccientes["elements"][-5:]
    info= ar.new_list()
    for accidente in primeros:
        nuevodic={"ID": accidente["ID"], "Fecha y hora de inicio": accidente["Start_Time"],
                  "Ciudad": accidente["City"], "Estado": accidente["State"], "Descripcion": accidente["Description"],
                  "Tiempo de duracion": accidente["duracion en horas"]}
        ar.add_last(info, nuevodic)
    for accidente in ultimos:
        nuevodic={"ID": accidente["ID"], "Fecha y hora de inicio": accidente["Start_Time"],
                  "Ciudad": accidente["City"], "Estado": accidente["State"], "Descripcion": accidente["Description"],
                  "Tiempo de duracion": accidente["duracion en horas"]}
        ar.add_last(info, nuevodic)     
    return (listadeaccientes["size"], info["elements"])
# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog, visibility_range, states):
    """
    Determina el impacto de la visibilidad en accidentes de alta gravedad en múltiples estados.
    
    :param catalog: El catálogo de datos.
    :param visibility_range: Rango de visibilidad.
    :param states: Lista de estados.
    
    :returns: Un análisis detallado de los accidentes que cumplen los criterios.
    """
    tree = catalog["treq2"]
    result = {
        "Accidentes Totales": 0,
        "state_analysis": ar.new_list(),
        "Peor accidente": None
    }

    # Obtener todas las claves de visibilidad en el árbol
    states_set = bst.key_set(tree)

    
    total_accidents = 0
    worst_accident = None
    
    for state in states:
        
        state_analysis = {
            "Estado": state,
            "Numero de accidentes": 0,
            "Visibilidad Promedio": "indefinido",
            "Distancia": "indefinido",
        }
        
        num_accidentes = 0
        total_visibility = 0
        total_distance = 0
        
        if bst.contains(tree, state):
            state_tree = bst.get(tree, state)
            visibility_set = bst.key_set(state_tree)
            for visibility in visibility_set["elements"]:
                if visibility_range[0] <= visibility <= visibility_range[1]:
                    if bst.contains(state_tree, visibility):
                        accidents = bst.get(state_tree, visibility)
                        num_accidentes += accidents["size"]
                        for accident in accidents["elements"]:
                            total_visibility += float(accident["Visibility(mi)"])
                            total_distance += float(accident["Distance(mi)"])
                            if worst_accident is None or float(accident["Distance(mi)"]) > float(worst_accident["Distance(mi)"]):
                                worst_accident = accident
                                
        state_analysis["Numero de accidentes"] = num_accidentes
        if num_accidentes > 0:
            state_analysis["Visibilidad Promedio"] = round(total_visibility / num_accidentes, 2)
            state_analysis["Distancia"] = round(total_distance / num_accidentes, 2)
        
        total_accidents += num_accidentes
        ar.add_last(result["state_analysis"], state_analysis)    

    ar.merge_sort(result["state_analysis"], compare_accidents_visibility)
    ar.shell_sort(result["state_analysis"], compare_accidents_number)
    result["Accidentes Totales"] = total_accidents
    result["Peor accidente"] = worst_accident
    
    return result


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

def compare_accidents_number(acc1, acc2):
    if acc1["Numero de accidentes"] > acc2["Numero de accidentes"]:
        return True
    return False

def compare_accidents_visibility(acc1, acc2):
    if acc1["Visibilidad Promedio"] < acc2["Visibilidad Promedio"]:
        return True
    return False
    