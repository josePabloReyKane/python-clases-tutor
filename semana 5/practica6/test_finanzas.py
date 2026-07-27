import finanzas
import pytest
def test_deposito():
    assert finanzas.deposito(15000,100)==15100

def test_deposito_erro():
    with pytest.raises(ValueError):
        finanzas.deposito(500,-55)
    

def test_retiro():
    assert finanzas.retiro(500,100)==400

def test_retiro_erro():
    with pytest.raises(ValueError):
        finanzas.retiro(100,200)

def test_calcular_interes_conpuesto():
    assert finanzas.calcular_interes_conpuesto(10,3,1)==40

def test_calcular_interes_conpuesto_erro_1():
    with pytest.raises(ValueError):
        finanzas.calcular_interes_conpuesto(-10,3,1)

def test_calcular_interes_conpuesto_erro_2():
    with pytest.raises(ValueError):
        finanzas.calcular_interes_conpuesto(10,-2,1)

def test_es_cuenta_premin_error_1():
    with pytest.raises(ValueError):
        finanzas.es_cuenta_premin(-20000,24)


def test_es_cuenta_premin_error_2():
    with pytest.raises(ValueError):
        finanzas.es_cuenta_premin(20000,-15)

def test_calcular_balance_neto():
    lista=[15456,-48597,987456]
    assert finanzas.calcular_balance_neto(lista)==954315
    assert finanzas.calcular_balance_neto([])==0


def test_filtrar_compras_mayoter_a():
    lista1=[500,-120,-30,-250]
    assert finanzas.filtrar_compras_mayoter_a(lista1,100)==[-120,-250]

def test_filtrar_compras_mayoter_a_error1():
    lista1=[500,-120,-30,-250]
    with pytest.raises(ValueError):
        finanzas.filtrar_compras_mayoter_a(lista1,-100)
