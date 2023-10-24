import pytest
from src.Ejercicio_3 import cuenta_regresiva

def test_cuenta_regresiva():
    cuenta_atras = []
    assert cuenta_regresiva(5, cuenta_atras) == "5, 4, 3, 2, 1, 0"

def generar_error(numero):
    cuenta_atras = []
    cuenta_regresiva(numero, cuenta_atras)

def test_cuenta_regresiva_errores():
    with pytest.raises(ValueError) as exc_info:
        generar_error(0)
    assert str(exc_info.value) == "Por favor, ingrese un número entero no negativo y mayor que 0."

def test_cuenta_regresiva_errores():
    with pytest.raises(ValueError) as exc_info:
        generar_error(-1)
    assert str(exc_info.value) == "Por favor, ingrese un número entero no negativo y mayor que 0."