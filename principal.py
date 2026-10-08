from nomina import(pago_tiempo_competo, pago_por_horas, pago_por_comision, calcular_deducciones, calcular_auxilio, calcular_pago_neto)

SMLV= 1300000
AUXILIO_TRANSPORTE= 162000
TOPE_AUXILIO= SMLV* 2

total_general= 0
total_tiempo_completo= 0
total_horas= 0
total_comision= 0

opciones= ["1. Empleado de tiempo completo", "2. Empleados por horas", "3. Empleado por comision", ""]