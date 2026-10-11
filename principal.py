#se importa el archivo que contiene las funciones
from nomina import(pago_tiempo_competo, pago_por_horas, pago_por_comision, calcular_deducciones, calcular_auxilio, calcular_pago_neto)

#constantes que no cambian en el codigo hasta que no cambien el salario internamente desde el gobierno
SMLV= 1300000
AUXILIO_TRANSPORTE= 162000
TOPE_AUXILIO= SMLV* 2

#lista de las opciones a escoger
opciones= ["1. Empleado de tiempo completo", "2. Empleados por horas", "3. Empleado por comision", ""]
tipos = ["Tiempo completo", "Por horas", "Por comision"]

#acumuladores que empiezan en 0
total_general= 0
total_tiempo_completo= 0
total_horas= 0
total_comision= 0

#ciclo while
while True:
    #ciclo for anidado para elección de opciones
    for opcion_texto in opciones:
        print(opcion_texto) 

    #se pide una opción
    opcion = input('Elige la opcion: ')

    #opción 4 que genere el break y cierre el programa
    if opcion == 4:
        break

    #opciones restantes
    #opción 1 empleado tiempo completo
    elif opcion == '1':
        documento = input('Ingrese el número de documento: ')
        nombre = input('Ingrese su nombre: ')
        salario_mensual = float(input('Ingrese su salario mensual: '))
        dias_trabajados = int(input('Ingrese los dias trabajados (1-30, 1-31: '))
        #acumulador
        total_tiempo_completo = total_tiempo_completo + neto
        #condición anidada si el salario es 0, si los dias trabajados es < 1 o si los dias trabajados < 31
        if salario_mensual <= 0 or dias_trabajados < 1 or dias_trabajados < 31:
            print('Datos inválidos, intente de nuevo')
            #que el ciclo continue
            continue
        #salario bruto
        salario_bruto = pago_tiempo_competo(salario_mensual, dias_trabajados)

    #opción 2 empleado por horas
    elif opcion == '2':
        documento = input('Ingrese el número de documento: ')
        nombre = input('Ingrese su nombre: ')
        horas_trabajadas = float(input('Ingrese las horas trabajadas: '))
        valor_hora = float(input('Ingrese el valor de la hora: '))
        #acumulador
        total_horas = total_horas + neto
        #condición anidada si las horas trabajadas <= 0 o el valor de la hora <= 0
        if horas_trabajadas <= 0 or valor_hora <= 0:
            print('Datos inválidos, intente de nuevo')
            #que el ciclo continue
            continue
        #salario bruto
        salario_bruto = pago_por_horas(horas_trabajadas, valor_hora)

    #opción 3 empleado por comision
    elif opcion == 3:
        documento = input('Ingrese el número de documento: ')
        nombre = input('Ingrese su nombre: ')
        ventas = float(input('Ingrese el monto de las ventas del mes: '))
        #acumulador
        total_comision = total_comision + neto
        #condición anidada si las ventas < 0
        if ventas < 0:
            print('Opción inválida, intente de nuevo')
            #que el ciclo continue
            continue
        #salario bruto
        salario_bruto = pago_por_comision(ventas)

    #opción inválida
    else:
        print('Opción inválida, intente de nuevo')
        #para que el ciclo continue
        continue

    #validación del tipo de empleado según la opción
    indice = int(opcion) - 1
    tipo = tipos[indice]

    #calculos de todos los tipos de empleados
    salud, pension = calcular_deducciones(salario_bruto)
    auxilio = calcular_auxilio(salario_bruto, TOPE_AUXILIO, AUXILIO_TRANSPORTE)
    neto = calcular_pago_neto(salario_bruto, salud, pension, auxilio)

    #impresiones de datos del empleado
    print(f'Documento: {documento}')
    print(f'Nombre: {nombre}')
    print(f'Tipo: {tipo}')
    print(f'Salario bruto: {round(salario_bruto, 2)}')
    print(f'Deducción de la salud (4%): {round(salud, 2)}')
    print(f'Deducción de la pensión (4%): {round(pension, 2)}')
    print(f'Auxilio de transporte: {round(auxilio, 2)}')
    print(f'Pago neto: {round(neto, 2)}')

#fuera del ciclo
#reporte final
#condición de reporte = 0
if total_general == 0:
    print('No se registraron empleados.')
else:
    print(f'Total pago general: {round(total_general, 2)}')
    print(f'Total pagado tiempo completo: {round(total_tiempo_completo, 2)}')
    print(f'Total pagado por horas: {round(total_horas, 2)}')
    print(f'Total pagado por comisión: {round(total_comision, 2)}')