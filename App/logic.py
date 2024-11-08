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
                    
       
        if int(accidente["Severity"])>=3 and (("Rain" in accidente["Weather_Condition"] or "Snow" in accidente["Weather_Condition"])) and float(accidente["Visibility(mi)"])<2:   
            keytreq3= accidente["Start_Time"]
            if bst.contains(catalog["treq3"], keytreq3)== False:
                lista=ar.new_list()
                lista= ar.add_last(lista, accidente)
                bst.put(catalog["treq3"], keytreq3, lista)
            else:
                lista = bst.get(catalog["treq3"], keytreq3)
                lista  = ar.add_last(lista, accidente)
                bst.put(catalog["treq3"], keytreq3, lista)           
        
        if int(accidente["Severity"]) >= 3 and float(accidente["Visibility(mi)"]) < 1:
            keytreq4 = accidente["Start_Time"]
            if bst.contains(catalog["treq4"], keytreq4) == False:
                bst.put(catalog["treq4"], keytreq4, bst.new_map())   
            keytreq4sub = accidente["Street"]
            if bst.contains(bst.get(catalog["treq4"], keytreq4), keytreq4sub) == False:
                lista = ar.new_list()
                lista = ar.add_last(lista, accidente)
                bst.put(bst.get(catalog["treq4"], keytreq4), keytreq4sub, lista)
            else:
                lista = bst.get(bst.get(catalog["treq4"], keytreq4), keytreq4sub)
                lista = ar.add_last(lista, accidente)
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


def req_1(catalog, p_start, p_end):
    """
    Retorna el resultado del requerimiento 1
    """
    start = get_time()
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
              
        ar.add_last(lista_accidentes, accidentes) 
         
        if f_inicial <= fecha_accidente <= f_final: #filtra el intervalo de las fechas parámetro     
            n_cumplen += len(accidentes)           
        if fecha_accidente > f_inicial:
            filtro_intervalo(nodo["left"]) #evalúa por qué dirección del arbol debe continuar      
        if fecha_accidente < f_final:
            filtro_intervalo(nodo["right"]) #evalúa por qué dirección del arbol debe continuar
    filtro_intervalo(catalog["treq1"]["root"])
    
    end = get_time()
    tiempo = delta_time(start,end)
    return n_cumplen, lista_accidentes, tiempo



def req_2(catalog, visibility_range, states):
    """
    Determina el impacto de la visibilidad en accidentes de alta gravedad en múltiples estados.
    
    :param catalog: El catálogo de datos.
    :param visibility_range: Rango de visibilidad.
    :param states: Lista de estados.
    
    :returns: Un análisis detallado de los accidentes que cumplen los criterios.
    """
    start = get_time()
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
    end = get_time()
    tiempo = delta_time(start,end)
    result["tiempo"] = tiempo
    
    return result


def req_3(catalog, n:int):
    """
    Retorna el resultado del requerimiento 3
    """
    inicio =get_time()
    n_cumplen = 0 #contador de cuantos accidentes ya han sido añadidos
    lista_accidentes = ar.new_list()
    
    rango = int(n) 
    
    def filtro_intervalo(nodo): #función auxiliar recursiva para cada nodo/sub-arbol
        nonlocal n_cumplen, lista_accidentes
        i = 0 
        if nodo is None:
            return      
        accidentes = nodo["value"]
        while i < len(accidentes) and n_cumplen < rango:           
            ar.add_last(lista_accidentes,accidentes)
            i += 1
            n_cumplen += 1   
        
        filtro_intervalo(nodo["left"])      
        filtro_intervalo(nodo["right"]) 
        
    filtro_intervalo(catalog["treq3"]["root"])
    final = get_time()
    tiempo = delta_time(inicio,final)
    return n_cumplen, lista_accidentes, tiempo
    


def req_4(catalog, time1, time2):
    """
    Retorna el resultado del requerimiento 4
    """
    inicio = get_time()
    tree = catalog["treq4"]
    result = ar.new_list()
    
    dates_set = bst.key_set(tree)
   
    fecha1 = datetime.strptime(time1, "%Y-%m-%d %H:%M:%S")
    fecha2 = datetime.strptime(time2, "%Y-%m-%d %H:%M:%S")
                      
   
    for date in dates_set["elements"]:
        if fecha1 <= date <= fecha2:
            street_accidents = bst.get(tree, date)
           
            street_accidents_set = bst.key_set(street_accidents)
           
            for street in street_accidents_set["elements"]:
                accidents = bst.get(street_accidents, street)
                analisis_via = {
                    "Calle": "",
                    "Peligrosidad (promedio de severidad)": 0,
                    "Numero de accidentes (severidad 3)": 0,
                    "Numero de accidentes (severidad 4)": 0,
                    "Visibilidad promedio": 0
                }
                num_accidents = 0
                num_accidents_severity_3 = 0
                num_accidents_severity_4 = 0
                total_severity = 0
                total_visibility = 0
                
                for accident in accidents["elements"]:
                    num_accidents += 1
                    total_severity += int(accident["Severity"])
                    total_visibility += float(accident["Visibility(mi)"])
                    if int(accident["Severity"]) == 3:
                        num_accidents_severity_3 += 1
                    elif int(accident["Severity"]) == 4:
                        num_accidents_severity_4 += 1
                    analisis_via["Calle"] = f"{street}, {accident['City']}, {accident['State']}"
                
                analisis_via["Peligrosidad (promedio de severidad)"] = round(total_severity / num_accidents, 2)
                analisis_via["Numero de accidentes (severidad 3)"] = num_accidents_severity_3
                analisis_via["Numero de accidentes (severidad 4)"] = num_accidents_severity_4
                analisis_via["Visibilidad promedio"] = round(total_visibility / num_accidents, 2)
                
                ar.add_last(result, analisis_via)
    final = get_time()
    print(delta_time(inicio,final)        )    
    return result

def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    inicio = get_time()
    condiciones = condiciones.split(",")
    fechaini = datetime.strptime(fechaini, '%Y-%m-%d')
    fechafin = datetime.strptime(fechafin, '%Y-%m-%d')
    fechafin = fechafin.date()
    fechaini = fechaini.date()
    trees= bst.values(catalog["treq5"], fechaini, fechafin)
    dicmañana={"franja": "mañana", "numero":0, "promedio":0}
    dictarde={"franja": "tarde","numero":0, "promedio":0}
    dicnoche={"franja": "noche","numero":0, "promedio":0}
    dicmadrugada={"franja": "madrugada","numero":0, "promedio":0}
    for condicion in condiciones:
        dicmañana[condicion]=0
        dictarde[condicion]=0
        dicnoche[condicion]=0
        dicmadrugada[condicion]=0
    for tree in trees["elements"]:
    
        weather= bst.key_set(tree)
        weather= weather["elements"]
        for clima in weather:
            for condicion in condiciones:
                if condicion in clima:
                    accidentes=bst.get(tree, clima)
                    for accidente in accidentes["elements"]:
                        horaaccidente= accidente["Start_Time"]
                        horaaccidente= horaaccidente.hour
                        if horaaccidente>=0 and horaaccidente<6:
                            dicmadrugada[condicion]+=1
                            dicmadrugada["numero"]+=1
                            dicmadrugada["promedio"]+= float(accidente["Severity"])
                        elif horaaccidente>=6 and horaaccidente<12:
                            dicmañana[condicion]+=1
                            dicmañana["numero"]+=1
                            dicmañana["promedio"]+= float(accidente["Severity"])
                        elif horaaccidente>=12 and horaaccidente<18:
                            dictarde[condicion]+=1
                            dictarde["numero"]+=1
                            dictarde["promedio"]+= float(accidente["Severity"])
                        elif horaaccidente>=18:
                            dicnoche[condicion]+=1
                            dicnoche["numero"]+=1
                            dicnoche["promedio"]+= float(accidente["Severity"])
    lista= ar.new_list()
    ar.add_last(lista, dicmadrugada)
    ar.add_last(lista, dicmañana)
    ar.add_last(lista, dictarde)
    ar.add_last(lista, dicnoche)
    
    for dic in lista["elements"]:
        if dic["numero"]!=0:
            dic["promedio"]= dic["promedio"]/ dic["numero"]
        dic["predominante"]= {"condicion": "", "cantidad": 0}
        for condicion in condiciones:
            if dic[condicion]>dic["predominante"]["cantidad"]:
                dic["predominante"]["cantidad"]= dic[condicion]    
                dic["predominante"]["condicion"]= condicion
    final = get_time()
    print(delta_time(inicio, final))
    return lista

def req_6(catalog, p_start, p_end, umbral, condados:list ):
    """
    Retorna el resultado del requerimiento 6
    """
    condados = condados.split()
    fechaini = datetime.strptime(fechaini,"%Y-%m-%d %H:%M:%S")
    fechafin = datetime.strptime(fechafin,"%Y-%m-%d %H:%M:%S")
    trees = bst.values(catalog["treq6"], fechaini, fechafin)
    diccondados = ar.new_list()
    for condado in condados:
        nuevodic= {"condado": condado,
            "numero":0,
            "temperatura promedio":0,
            "velocidad promedio": 0,
            "humedad promedio": 0,
            "distancia promedio": 0}
        ar.add_last (diccondados, nuevodic)
    for tree in trees["elements"]:
        arbolescondados= bst.values(tree, humedad, 100)
        for arbolcondado in arbolescondados ["elements"]:
            condados = bst.key_set(arbolcondado)
            for cond in condados ["elements"]:
                for diccondado in diccondados ["elements"]:
                    if cond==diccondado["condado"]:
                        accidentes = bst-get(arbolcondado, cond)
                        for accidente in accidentes:
                            diccondado ["numero"]+=1
                            diccondado ["temperatura promedio"]+= accidente ["Temperature (F)"]
    
    return 
    


def req_7(catalog, lat_start, lon_start, lat_end, lon_end):
    """
    Retorna el resultado del requerimiento 7
    """
    tree = catalog["treq7"]
    
    print(tree)
    
    id_set = bst.key_set(tree)
    
    result = ar.new_list()
    
    for key in id_set["elements"]:
        accident = bst.get(tree, key) 
        print(accident)
        if float(lat_start) <= float(accident["Start_Lat"]) <= float(lat_end) and float(lon_start) <= float(accident["Start_Lng"]) <= float(lon_end):
            ar.add_last(result, accident)
    
    ar.merge_sort(result, compare_lat_lon)
    
    retorno = ar.new_list()
    
    if ar.size(result) > 10:
        sub1 = ar.sub_list(result, 0, 5)
        sub2 = ar.sub_list(result, ar.size(result) - 5, 5)
        
        for accident in sub1["elements"]:
            ar.add_last(retorno, accident)
        for accident in sub2["elements"]:
            ar.add_last(retorno, accident)
            
    else:
        for accident in result["elements"]:
            ar.add_last(retorno, accident)
            
    return retorno
    


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

def compare_lat_lon(acc1, acc2):
    if (acc1["Start_Lat"], acc1["Start_Lng"], acc1["End_Lat"], acc1["End_Lng"]) < (acc2["Start_Lat"], acc2["Start_Lng"], acc2["End_Lat"], acc2["End_Lng"]):
        return True
    return False
    