__author__ = 'José Pablo Parajeles Luis Diego Pizarro'

def prueba(fun):
    ret = [(1200, 1, 1), (2000, 15, 1), (2000, 1, 32), (2000, 1, 31), (2000, 1, 30), (2000, 1, 29), (2000, 1, 28),
           (2000, 1, 27), (2000, 12, 31), (1995, 2, 28), (1995, 2, 20), (1995, 2, 29), (1995, 2, 30), (1995, 2, 31),
           (1995, 4, 31), (1995, 4, 30), (1995, 4, 29), (1995, 4, 28), (2015, 4, 20), (1994, 2, 29), (1994, 2, 28),
           (1994, 2, 20), (1900, 2, 29), (1900, 2, 28), (1900, 2, 20), (2000, 2, 29), (2000, 2, 28), (2000, 2, 20)]
    ora = ["Año Invalido", "Mes Invalido", "Dia Invalido", (2000,2,1), (2000,1,31), (2000,1,30), (2000,1,29),
           (2000,1,28), (2001,1,1), (1995,3,1), (1995,2,21), "Fecha Invalida", "Fecha Invalida", "Fecha Invalida",
           "Fecha Invalida", (1995,5,1), (1995,4,30), (1995,4,29), (2015,4,21), (1994,3,1), (1994,2,29), (1994,2,21),
           "Fecha Invalida", (1900,2,28), (1900,2,21), (2000,3,1), (2000,2,29), (2000,2,21)]
    for i,elem in enumerate(ret):
        try:
            print("R{}".format(i+1))
            print("Oraculo: {}".format(ora[i]))
            print("Result : {}".format(fun(elem)))
        except Exception as e:
            print(e)
        print()
    print()

from Fechas_Prof import dia_siguiente as dia_sig_prof
from Fecha_G14 import dia_siguiente as dia_sig_G14

prueba(dia_sig_prof)
prueba(dia_sig_G14)
