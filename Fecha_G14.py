# Instituto Tecnológico de Costa Rica
# Escuela de Ingeniería en Computación
# Aseguramiento de la Calidad de Software
# Asignación 2 Calendario Gregoriano y Fechas
# Profesor: Ignacio Trejos Zelaya
# Estudiantes:  Ilenia Vásquez Vásquez - 201131390
#               Génesis Salazar Barquero - 201155873
# Primer Semestre, 2015



        

# Función que determina si un año es bisiesto.
def bisiesto(año):
    if isinstance(año, int):
        if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
                return True
        else:
            return False
    else:
        print("Ingrese un valor numérico entero.")

# Función que determina si una fecha es válida.
def fecha_es_valida(fecha):
    if isinstance(fecha,tuple) and len(fecha)!= 0 and isinstance(fecha[0],int) and isinstance(fecha[1], int) and isinstance(fecha[2],int):
        if fecha[0] >= 1582:
            if mes_valido(fecha[1]) and dia_valido(fecha):
                return True
            else:
                return False
        else:
            print("El año no corresponde al calendario gregoriano.")
    else:
        print("El formato de la fecha es incorrecto. Ejemplo: (año, mes, día) en donde año, mes y día son valores enteros positivos.")

# Función que, dada una fecha válida, determina la fecha del día siguiente.
def dia_siguiente(fecha):
    if fecha_es_valida(fecha):
        # Si es 31 de diciembre incrementa el año
        if fecha[1] == 12 and fecha[2] == 31:
            print ((fecha[0]+1,1,1))

        #Valida los casos del mes de febrero
        elif fecha[1] == 2:
            # Si es bisiesto y no es el ultimo dia , incrementa el día    
            if bisiesto(fecha[0]) and fecha[2] < 29:
                print ((fecha[0], fecha[1], fecha[2]+1))

            #Si es o no bisiesto, y es el ultimo día, incrementa el mes
            elif (bisiesto(fecha[0]) and fecha[2] == 29) or fecha[2] == 28:
                print ((fecha[0], fecha[1]+1, 1))

        # Si es el ultimo día de cualquier otro mes, incrementa el mes
        elif (fecha[1] in (4,6,9,11) and fecha[2] == 30) or fecha[2] == 31:
            print ((fecha[0], fecha[1]+1, 1))

        # Sino incrementa el día
        else:
            print ((fecha[0], fecha[1], fecha[2]+1))
    else:
        print("La fecha es inválida")


# Función que, dado un año válido, determina el dia de la semana que corresponde
# al primero de enero, con la siguiente codificación: 0 = domingo, 1 = lunes,
# 2 = martes, 3 = miércoles, 4 = jueves, 5 = viernes, 6 = sábado.
def dia_enero_1(año):
    # Implementación del algoritmo de Zeller para el calendario gregoriano    
    if isinstance(año, int):
        mes = 1
        día = 1
        
        a = (14 - mes)//12
        y = año - a
        m = mes + 12 * a - 2

        d = (día + y + y//4 - y//100 + y//400 + (31*m)//12) % 7
        print(d)

    else:
        print("Ingrese un valor numérico entero.")

#-----------------------FUNCIONES COMPLEMENTARIAS-----------------------------


# Función que determina si un día es válido.
# Retorna True si es válida, o False si es inválida.
def dia_valido(fecha):
    
    # Valida mes de febrero en años bisiestos y no bisiestos
    if fecha[1] == 2:
        if (bisiesto(fecha[0]) and 0 < fecha[2] <= 29) or 0 < fecha[2] <= 28:
            return True
        else:
            return False
    # Valida los meses de 31 días
    elif fecha[1] in (1,3,5,7,8,10,12) and 0 < fecha[2] <= 31:
        return True
    # Valida los meses de 30 dias
    elif fecha[1] in (4,6,9,11) and 0 < fecha[2] <= 30:
        return True
    else:
        return False

# Función que determina si un mes es válido
#Retorna True si es válido o False si es inválido
def mes_valido(mes):
    if 0 < mes <= 12:
        return True
    else:
        return False


##
##
###---------------- MENÚ --------------
##
##while True:
##
##    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-MENÚ PRINCIPAL-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
##    print("1) Determinar si un año es bisiesto.")
##    print("2) Determinar si una fecha es válida.")
##    print("3) Determinar la fecha del dia siguiente, dada una fecha válida.")
##    print("4) Determinar el día de la semana que corresponde al primero de enero, dado un año.")
##    print("5) Salir del programa.\n")
##    opcion = input("Digite la opción a realizar: ")
##
##    if opcion == "5":
##          break
##    try:      
##        if opcion == "1":
##            año = int(input("Digite el año: "))
##
##            if bisiesto(año):
##                print("El año es bisiesto")
##            else:
##                print("El año no es bisiesto")
##
##        elif opcion == "4":
##            año = int(input("Digite el año: "))
##            dia_enero_1(año)
##            
##        else:
##            año = int(input("Digite el año: "))
##            mes = int(input("Digite el mes: "))
##            día = int(input("Digite el día: "))
##
##            if opcion == "2":
##                if fecha_es_valida((año,mes,día)):
##                    print("La fecha es válida.")
##                else:
##                    print("La fecha es inválida.")
##
##            elif opcion == "3":
##                dia_siguiente((año,mes,día))
##
##    except ValueError:
##        print("El valor ingresado no es válido.")
##
##    
