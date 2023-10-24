import pytest
from src.Ejercicio_4 import obtener_entero

def test_obtener_entero_correcto():
    assert obtener_entero("5") == 5

def test_obtener_entero_negativo():
    with pytest.raises(ValueError, match="Error: La entrada debe ser un número entero válido."):
        obtener_entero("-1")

def test_obtener_entero_letra():
    with pytest.raises(ValueError, match="La entrada debe ser un número entero válido."):
        obtener_entero("a")