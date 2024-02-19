import pytest
from src.Ejercicio_2 import numeros_impares_hasta_n

def test_numeros_impares_hasta_n():
    assert numeros_impares_hasta_n(5) == "1, 3, 5"
    assert numeros_impares_hasta_n(1) == "1"
    with pytest.raises(ValueError) as exc_info:
        numeros_impares_hasta_n(0)
    assert str(exc_info.value) == "Por favor, ingrese un número entero positivo válido."
    with pytest.raises(ValueError) as exc_info:
        numeros_impares_hasta_n(-1)
    assert str(exc_info.value) == "Por favor, ingrese un número entero positivo válido."
    with pytest.raises(ValueError) as exc_info:
        numeros_impares_hasta_n("hola")
    assert str(exc_info.value) == "Por favor, ingrese un número entero positivo válido."