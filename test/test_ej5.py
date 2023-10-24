import pytest
from src.Ejercicio_5 import verificaContrasenia

def test_verificaContrasenia_correcta():
    contrasenia = "Hola1234"
    contraseniaUser = "Hola1234"
    verificaContrasenia(contrasenia, contraseniaUser)

def test_verificaContrasenia_incorrecta():
    contrasenia = "Hola1234"
    contraseniaUser = "Hola5678"
    with pytest.raises(NameError, match="Incorrect Password!!"):
        verificaContrasenia(contrasenia, contraseniaUser)
