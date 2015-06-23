# Ejemplos de funcionalidad en el dominio de las fechas
# Autor: Ignacio Trejos Zelaya, Cenfotec e ITCR
# Version 5.0  2010.04.11 : mejoras de estilo o comentarios
# Versión 3.0  2010.04.04
# Para usos didácticos

# Valores globales para validaciones
fecha0 = (1600, 1, 1)
tuple_class = type(fecha0)
int_class = type(1)

# Determinar divisibilidad de un entero por otro (ambos no negativos)
def divide(dividendo, divisor):
    return (dividendo % divisor) == 0


# Determinar si año es bisiesto.  El orden en que se evalúan las condiciones es importante
def es_bisiesto(anio):
    if divide(anio, 400):
        return True
    elif divide(anio, 100):
        return False
    elif divide(anio, 4):
        return True
    else:
        return False


# funciones para determinar el número de días de un mes
def dias_febrero(anio):
    # determinar el número de días, dependiendo de si el año es bisiesto
    if es_bisiesto(anio):
        return 29
    else:
        return 28


def dias_mes(anio, mes):
    if mes == 2:
        return dias_febrero(anio)
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return 30
    else:
        return 31


def correccion_febrero(anio):
    # determinar si hay que sumar un día más, dependiendo de si el año es bisiesto
    if es_bisiesto(anio):
        return 1
    else:
        return 0


# Determinar los días transcurridos desde el
# primero de enero de un año hasta una fecha dada (anio, mes, dia)
# Se toma en cuenta el día
def dias_transcurridos(anio, mes, dia):
    if mes == 1:
        return dia
    elif mes == 2:
        return 31 + dia
    elif mes == 3:
        return 59 + dia + correccion_febrero(anio)
    elif mes == 4:
        return 90 + dia + correccion_febrero(anio)
    elif mes == 5:
        return 120 + dia + correccion_febrero(anio)
    elif mes == 6:
        return 151 + dia + correccion_febrero(anio)
    elif mes == 7:
        return 181 + dia + correccion_febrero(anio)
    elif mes == 8:
        return 212 + dia + correccion_febrero(anio)
    elif mes == 9:
        return 243 + dia + correccion_febrero(anio)
    elif mes == 10:
        return 273 + dia + correccion_febrero(anio)
    elif mes == 11:
        return 304 + dia + correccion_febrero(anio)
    elif mes == 12:
        return 334 + dia + correccion_febrero(anio)


# Determinar el componente de mes y de día de la fecha de un día ordinal dado
# a es el año, r es el ordinal del día,  dentro de ese año
# 1 corresponde a año.01.01
# 0 corresponde a año.12.31, caso bisiesto o no bisiesto
def mes_y_dia_de(a, r):
    if r == 0:
        return (12, 31)  # si es llamada desde otra función y el residuo es 0, correspone al último día del año
    elif r <= 31:
        return (1, r)
    elif r <= 59 + correccion_febrero(a):
        return (2, r - 31)
    elif r <= 90 + correccion_febrero(a):
        return (3, r - (59 + correccion_febrero(a)))
    elif r <= 120 + correccion_febrero(a):
        return (4, r - (90 + correccion_febrero(a)))
    elif r <= 151 + correccion_febrero(a):
        return (5, r - (120 + correccion_febrero(a)))
    elif r <= 181 + correccion_febrero(a):
        return (6, r - (151 + correccion_febrero(a)))
    elif r <= 212 + correccion_febrero(a):
        return (7, r - (181 + correccion_febrero(a)))
    elif r <= 243 + correccion_febrero(a):
        return (8, r - (212 + correccion_febrero(a)))
    elif r <= 273 + correccion_febrero(a):
        return (9, r - (243 + correccion_febrero(a)))
    elif r <= 304 + correccion_febrero(a):
        return (10, r - (273 + correccion_febrero(a)))
    elif r <= 334 + correccion_febrero(a):
        return (11, r - (304 + correccion_febrero(a)))
    elif r <= 365 + correccion_febrero(a):
        return (12, r - (334 + correccion_febrero(a)))


# Validar una fecha
def fecha_es_valida(tupla):
    # primero ver si es tupla de números enteros
    if not (type(tupla) == tuple_class):
        raise Exception("Fecha no es tupla")
    elif len(tupla) != 3:
        raise Exception("Fecha no es una tupla de 3 componentes")
    elif type(tupla[0]) != int_class:
        raise Exception("Primer componente de fecha no es un entero")
    elif type(tupla[1]) != int_class:
        raise Exception("Segundo componente de fecha no es un entero")
    elif type(tupla[2]) != int_class:
        raise Exception("Tercer componente de fecha no es un entero")
    dia = tupla[2]
    mes = tupla[1]
    anio = tupla[0]
    return (1 <= dia <= dias_mes(anio, mes)) and (1 <= mes <= 12) and (1600 <= anio <= 32767)


# Hacer una fecha válida a partir de una tupla de enteros
def hacer_fecha(anio, mes, dia):
    # hacer una fecha válida
    if type(anio) != int_class:
        raise Exception("Primer componente de fecha no es un entero")
    elif type(mes) != int_class:
        raise Exception("Segundo componente de fecha no es un entero")
    elif type(dia) != int_class:
        raise Exception("Tercer componente de fecha no es un entero")
    elif (1 <= dia <= dias_mes(anio, mes)) and (1 <= mes <= 12) and (1600 <= anio <= 32767):
        return (anio, mes, dia)


# bisiestos_antes_de calcula el número de años bisiestos entre 1600 y el anio dado, sin contar anio
# bisiestos_en_400 calcula el número de bisiestos en el período de un múltiplo de 400 años ANTES de anio
# anios_desde_400 es el número de años transcurridos desde el más reciente ciclo de 400 años
# no_bisiestos_de_100 es el número de años no bisiestos en el residuo, por ser múltiplos de 100
# periodos_de_4 es el número de períodos completos de 4 años en el residuo
def bisiestos_antes_de(anio):
    if anio <= 1600:
        return 0
    else:
        anios_1600 = anio - 1 - 1600  # años transcurridos desde origen hasta anio - 1
        bisiestos_en_400 = 97 * (anios_1600 // 400)
        anios_desde_400 = anios_1600 % 400
        no_bisiestos_de_100 = anios_desde_400 // 100
        periodos_de_4 = anios_desde_400 // 4
        return bisiestos_en_400 + periodos_de_4 - no_bisiestos_de_100 + (1 if anio > 1600 else 0)
        # Justificación de la fórmula:
        #   Si el año es 1600, no lo cuenta
        # + bisiestos en período de 400 años
        # + múltiplos de 4 en el residuo del ciclo de 400 años (años bisiestos
        # - años no bisiestos (múltiplos de 100 que no lo son de 400)


# Determinar el ordinal de un día desde 1600.01.01
def dia_desde_1600(anio, mes, dia):
    anios = anio - 1600  # años transcurridos desde origen hasta anio
    dias_previos_a_anio = 365 * anios + bisiestos_antes_de(anio)
    return dias_transcurridos(anio, mes, dia) + dias_previos_a_anio


# Para validar dia_desde_1600
def val_dia_desde_1600(fecha):
    dia = fecha[2]
    mes = fecha[1]
    anio = fecha[0]
    return dia_desde_1600(anio, mes, dia)


# Días entre dos fechas
def dias_entre(fecha1, fecha2):
    if not (fecha_es_valida(fecha1)):
        raise Exception("fecha1 es inválida")
    elif not (fecha_es_valida(fecha2)):
        raise Exception("fecha2 es inválida")

    dia1 = fecha1[2]
    mes1 = fecha1[1]
    anio1 = fecha1[0]
    dias_a_fecha1 = dia_desde_1600(anio1, mes1, dia1)

    dia2 = fecha2[2]
    mes2 = fecha2[1]
    anio2 = fecha2[0]
    dias_a_fecha2 = dia_desde_1600(anio2, mes2, dia2)

    return abs(dias_a_fecha1 - dias_a_fecha2)


# Determinar el día de la semana de una fecha
# 5 es el factor de corrección, pues el 1600.01.01 fue sábado
# 0 = domingo, 1 = lunes, ..., 6 = sábado
def dia_semana(anio, mes, dia):
    return (5 + dia_desde_1600(anio, mes, dia)) % 7

# Algunas constantes útiles para calcular la fecha dado un día ordinal
# Días en un año ordinario
d1N = 365
# Días en año bisiesto
d1B = 366
# Días en cuatrienio constituido por un año bisiesto seguido por 3 años normales
d4B = d1B + d1N * 3
# Días en 4 años normales; sólo se da al principio de un siglo de la forma 400 + k*100 (k in {1,2,3})
d4N = d1N * 4
# Días en ciclo de 400 años que inicia en año bisiesto (múltiplo de 400)
d400B = d1N * 400 + 97
# Días en ciclo de 100 años que inicia en año no bisiesto (múltiplo de 100)
d100N = d1N * 100 + 24
# Días en ciclo de 100 años que inicia en año bisiesto (múltiplo de 400)
d100B = d1N * 100 + 25


def fecha_de(ordinal_dia):  # retorna una tupla (anio, mes, dia)
    # Comienza por determinar el número de años completos previos a un día ordinal dado
    # pre: ordinal_dia > 0
    # Cuidado especial: en el límite (frontera) entre un ciclo y el siguiente
    # Determinar períodos de 400 años hasta un día ordinal
    a400 = (ordinal_dia - 1) // d400B
    # Iniciar los años a partir de 1600, con los períodos de 400 años
    a = 1600 + 400 * a400
    # Residuo de días posteriores a período de 400 años
    r = ordinal_dia % d400B
    # Analizar casos
    if r > d100B:  # más allá del primer siglo de un ciclo de 400 años.  Ese primer siglo inicia con un bisiesto.
        (a, r) = f100n(a + 100, r - d100B)  # Sumamos 100 años del siglo, quitamos de r sus días
    elif r == 0:  # es el último día de un ciclo de 400 años
        a = a + 399  # estamos en el último año de ese ciclo
    else:  # a está en el primer siglo, que inicia con un año bisiesto
        (a, r) = f100b(a, r)
    # determinar el mes, dado un año (a) y un desplazamiento relativo dentro del año (r)
    (m, d) = mes_y_dia_de(a, r)
    return (a, m, d)


# Determinar el año en que cae un día ordinal, dentro de un período de un siglo que inicia con un año no bisiesto
# En a está el año que sigue al primer siglo de un ciclo de 400 años
# Estos períodos de un siglo solo pueden aparecer después de un siglo que inicia con bisiesto
# f100N pre: a está al menos 100 años después del inicio de un ciclo de 400 años, a es no bisiesto
def f100n(a, r):
    # Determinar siglos precedentes
    a100 = (r - 1) // d100N
    # Acumular siglos precedentes
    a = a + 100 * a100
    # Residuo de días posteriores a un período de 100 años
    r = r % d100N
    # Analizar casos
    if r > d4N:  # más allá del primer ciclo de 4 años en un siglo que inicia en año no bisiesto,
        (a, r) = f4b(a + 4, r - d4N)  # que siempre es seguido por ciclos de 4 años donde el primero es bisiesto
    elif r == 0:  # es el último día de un ciclo de 100 años
        a = a + 99  # estamos en el último año de ese ciclo
    else:
        (a, r) = f_n(a, r)  # r está en un cuatrienio que inicia con un año no bisiesto
    return (a, r)


# Determinar el año en que cae un día ordinal, dentro de un período de un siglo que inicia con un año bisiesto
def f100b(a, r):
    # Determinar cuatrienios precedentes (que comienzan con un año bisiesto)
    a4 = (r - 1) // d4B
    # Acumular cuatrienios precedentes
    a = a + 4 * a4
    # Residuo de días posteriores a un período de 4 años
    r = r % d4B
    # Analizar casos
    if r > d1B:  # más allá del primer año (bisiesto)
        (a, r) = f_n(a + 1, r - d1B)  # 1 año bisiesto, seguido por 3 años no bisiestos
    elif r == 0:  # es el último día de un período BNNN
        a = a + 3
    return (a, r)


# Determinar el año de r, en un período de 4 años que inicia con un año bisiesto (BNNN)
def f4b(a, r):
    # Determinar cuatrienios que comienzan con un año bisiesto
    a4 = (r - 1) // d4B
    # Acumular cuatrienios precedentes
    a = a + 4 * a4
    # Residuo de días posteriores a un período de 4 años
    r = r % d4B
    # Analizar casos
    if r > d1B:  # más allá del primero (bisiesto)
        (a, r) = f_n(a + 1, r - d1B)  # 1 año bisiesto, seguido por 3 años no bisiestos
    elif r == 0:  # es el último día de un período BNNN
        a = a + 1
    return (a, r)


# Determinar el año de r, en un período de cuatro años no bisiestos consecutivos (sólo ocurre al inicio de siglo no div 400)
#   o bien
# Determinar el año en un período de tres años no bisiestos consecutivos (sólo ocurre después de un año bisiesto)
# fN pre:
def f_n(a, r):
    # Determinar años no bisiestos
    a1 = (r - 1) // d1N
    # Acumular años precedentes
    a = a + a1
    # Residuo de días posteriores a un año
    r = r % d1N
    return (a, r)


def fecha_futura(tupla, dias):
    od = val_dia_desde_1600(tupla) + dias
    return fecha_de(od)


def dia_siguiente(tupla):
    od = val_dia_desde_1600(tupla) + 1
    return fecha_de(od)
