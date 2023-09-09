#confeccionar una agenda. uttilizar un diccionario cuya clave sea la fecha.
#permitir almacenar distintas actividades para la misma fecha (se ingresa la hora y la actividad)
#implementar las siguientes funciones:
#1) Carga de datos en la agenda.
#2) listado completo de la agenda.
#3) consulta de una fecha.

def cargar():
    agenda=[]
    continua1="&"
    while continua1=="&":
        fecha=input("ingrese la fecha con formato dd/mm/aa:")
        continua2="&"
        lista=[]
        while continua2=="&":
            hora=input("ingrese la descripcion de la actividad:")
            actividad=input("ingrese la descripcion de la actividad:")
            lista.append((hora.actividad))
            continua2=input("ingresa otra actividad para la misma fecha[s/n]:")
            agenda[fecha]=lista
            continua1=input("ingresa otra fecha[s/n]:")
        return agenda

def imprimir(agenda):
    print("listado completo de la agenda")
    for fecha in agenda:
        print("para la fecha:"fecha)
        for hora,actividad in agenda[fecha]:
            print(hora,actividad)

def consulta_fecha(agenda)
fecha=input("ingrese la fecha que desea consultar:")
if fecha in agenda:
    for hora,actividad in agenda[fecha]:
        print(hora,actividad)

    else:
        print("no hay actividades agendadas para dicha fecha")


# bloque principal

agenda=cargar()
imprimir(agenda)
consulta_fecha(agenda)

        
            
        
        
