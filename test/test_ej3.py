import pytest
from src.Ejercicio_3 import cuenta_regresiva

def test_cuenta_regresiva():
    cuenta_atras = []
    assert cuenta_regresiva(5, cuenta_atras) == "5, 4, 3, 2, 1"
    assert cuenta_regresiva(0, cuenta_atras) == "0"
    assert cuenta_regresiva(-1, cuenta_atras) == ""

def generar_error():
    cuenta_atras = []
    cuenta_regresiva("hola", cuenta_atras)

def test_cuenta_regresiva_errores():
    with pytest.raises(ValueError) as exc_info:
        generar_error()
    assert str(exc_info.value) == "Por favor, ingrese un número entero válido."