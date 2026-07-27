

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
    
    return capital*(1+tasa)**periodo

def es_cuenta_premin(saldo,antiguedad_meses):
    if saldo<0 or antiguedad_meses<24:
        raise ValueError
    
    return True


def calcular_balance_neto(transacciones):
    if len(transacciones)==0:
        return 0

    return sum(transacciones)
    



def filtrar_compras_mayoter_a(trasacciones,umbral):
    if umbral<0:
        raise ValueError
    
    resultado=[]
    
    for trasaccione in trasacciones:
        if abs(trasaccione)>umbral and trasaccione<0:
            resultado.append(trasaccione)

    return resultado
            