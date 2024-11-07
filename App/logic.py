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


def req_3(catalog, n:int):
    """
    Retorna el resultado del requerimiento 3
    """
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
    
    return n_cumplen, lista_accidentes
    


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
    return lista

def req_6(catalog, p_start, p_end, umbral, condados:list ):
    """
    Retorna el resultado del requerimiento 6
    """
    n_cumplen = 0 #contador de cuantos accidentes ya han sido añadidos
    lista_accidentes = ar.new_list()
    f_inicial = datetime.strptime(p_start, "%Y-%m-%d %H:%M:%S") #conversión a formato adecuado
    f_final = datetime.strptime(p_end, "%Y-%m-%d %H:%M:%S") #conversión a formato adecuado
    
  
    def filtro_intervalo(nodo): #función auxiliar recursiva para cada nodo/sub-arbol
        nonlocal n_cumplen, lista_accidentes
        
        if nodo is None:
            return      
        
        f_accidente = nodo["key"]
        accidentes = nodo["value"]
            
        for i in bst.key_set(accidentes)["elements"]:
            humedad_actual = i
            if f_inicial < f_accidente < f_final and humedad_actual > umbral:
                ar.add_last(lista_accidentes,accidentes)
                n_cumplen += 1   
        
        filtro_intervalo(nodo["left"])      
        filtro_intervalo(nodo["right"])     
    filtro_intervalo(catalog["treq6"]["root"])
    
    for county in lista_accidentes["elements"]["value"]["value"]["elements"]:
        print(county)
        print("\n")
    
    return 
    


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
