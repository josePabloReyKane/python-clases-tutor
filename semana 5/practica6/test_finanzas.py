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

