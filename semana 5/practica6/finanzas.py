

def deposito(saldo_actual,monto):
    if monto < 0:
        raise ValueError
    
    
    return saldo_actual+monto


def retiro(saldo_actual,monto):
    if saldo_actual < monto:
        raise ValueError
    
    return saldo_actual - monto
    
def calcular_interes_conpuesto(capital,tasa,periodo):
    if capital<0:
        raise ValueError
    if tasa<0:
        raise ValueError
    
    return periodo*(1+tasa)**periodo

def es_cuenta_premin(saldo,antiguedad_meses):
    if saldo<0 or antiguedad_meses<24:
        raise ValueError
    
    return True


def calcular_balance_neto(transacciones):
    pass



def filtrar():
    pass