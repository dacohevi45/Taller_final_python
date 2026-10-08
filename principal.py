#se importa el archivo que contiene las funciones
from nomina import(pago_tiempo_competo, pago_por_horas, pago_por_comision, calcular_deducciones, calcular_auxilio, calcular_pago_neto)

#constantes que no cambian en el codigo hasta que no cambien el salario internamente desde el gobierno
SMLV= 1300000
AUXILIO_TRANSPORTE= 162000
TOPE_AUXILIO= SMLV* 2

#lista de las opciones a escoger
opciones= ["1. Empleado de tiempo completo", "2. Empleados por horas", "3. Empleado por comision", ""]
tipos = ["Tiempo completo", "Por horas", "Por comision"]

#acumuladores
total_general= 0
total_tiempo_completo= 0
total_horas= 0
total_comision= 0

#ciclo 
while True:
    for opcion_texto in opciones:
        print(opcion_texto)

    opcion = input('Elige la opcion: ')