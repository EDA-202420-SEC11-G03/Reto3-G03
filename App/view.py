import sys
from App import logic as lg
from datetime import datetime


def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    return lg.new_logic()

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    rta= lg.load_data(control,"./Data/accidents-small.csv" )
    print(rta)

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    r = []
    x=input(print("Introduzca el inicio de la fecha a filtrar: "))
    y=input(print("Introduzca el final de la fecha a filtrar: "))
    total, accidentes = lg.req_1(control, x,y)

    for accidente in accidentes["elements"]:
        for i in accidente["elements"]:
            if i["End_Time"] == "Desconocido" or i["Start_Time"] == "Desconocido":
                duracion = "Desconocido"
            else:
                duracion = i["End_Time"] - i["Start_Time"]
            info_accidente = {
                        "ID": i["ID"],
                        "Fecha y Hora de Inicio": i["Start_Time"].strftime("%Y-%m-%d %H:%M"),
                        "Ciudad": i["City"],
                        "Estado": i["State"],
                        "Descripción": i["Description"][:40],
                        "Duración en Horas": duracion
                    }
            r.append(info_accidente)
    
    if len(r) > 10:
        final = r[:5], r[-5:]
    else: 
        final = r   
    print(total, final)


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    r = []
    x=input(print("Introduzca el número de accidentes a filtrar: "))
    total, accidentes = lg.req_3(control, x)

    for accidente in accidentes["elements"]:
        for i in accidente["elements"]:
            if i["End_Time"] == "Desconocido" or i["Start_Time"] == "Desconocido":
                duracion = "Desconocido"
            else:
                duracion = i["End_Time"] - i["Start_Time"]
            info_accidente = {
                        "ID": i["ID"],
                        "Fecha y Hora de Inicio": i["Start_Time"].strftime("%Y-%m-%d %H:%M"),
                        "Ciudad": i["City"],                    
                        "Estado": i["State"],
                        "Precipitación": i["Precipitation(in)"],
                        "Severidad": i["Severity"],
                        "Descripción": i["Description"][:40],
                        "Duración en Horas": duracion 
                    }
            r.append(info_accidente)
    print(total, r)


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    x= input(print("introduzca fecha inical: "))
    y= input(print("introduzca fecha final: "))
    z= input(print("introduzca codiciones: "))
    rta= lg.req_5(control, x, y, z)
    print(rta)
def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    a= input(print("introduzca fecha inical: "))
    b= input(print("introduzca fecha final: "))
    c= input(print("introduzca umbral de humedad: "))
    d= input(print("introduzca lista de condados: "))
    rta= lg.req_6(control, a,b,c,d)
    print(rta)
    
    
    
    


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
