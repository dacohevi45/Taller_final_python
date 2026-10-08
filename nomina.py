SLMV= 1300000

def pago_tiempo_competo(salario_mensual, dias_trabajados):
    if dias_trabajados>=30:
        return salario_mensual
    else: 
        return salario_mensual (dias_trabajados / 30)

def pago_por_horas(horas_trabajadas, valor_hora):
    return horas_trabajadas * valor_hora

def pago_por_comision(ventas):
    if ventas>=5000000 and ventas <= 10000000:
        comision= ventas*0.25
    elif ventas>=11000000 and ventas <=40000000:
        comision= ventas*0.35
    elif ventas >=41000000 and ventas <=70000000:
        comision= ventas*0.45
    elif ventas >= 71000000 and ventas <= 100000000:
        comision= ventas*0.70
    else:
        comision= 0
        bono= SLMV * 0.5
        return comision + bono

def calcular_deducciones(salario_bruto):
    salud= salario_bruto*0.04
    pension= salario_bruto*0.04
    return salud, pension

def calcular_auxilio(salario_bruto, tope, auxilio):
    if salario_bruto<= tope:
        return auxilio
    return 0

def calcular_pago_neto(salario_bruto, salud, pension, auxilio):
    return salario_bruto- salud- pension+ auxilio
