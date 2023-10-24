from src.Ejercicio_1 import mostrar_anios_cumplidos

def test_mostrar_anios_cumplidos():
    assert mostrar_anios_cumplidos(5) == "Has cumplido 1 años.\nHas cumplido 2 años.\nHas cumplido 3 años.\nHas cumplido 4 años.\nHas cumplido 5 años.\n"

def test_mostrar_anios_cumplidos_invalido():
    assert mostrar_anios_cumplidos(-3) == "Por favor, ingresa una edad válida." 

def test_mostrar_anios_cumplidos_letras():
    assert mostrar_anios_cumplidos("abc") == "Por favor, ingresa un número entero para tu edad."

def test_mostrar_anios_cumplidos_letras():
    assert mostrar_anios_cumplidos(0) == "Por favor, ingresa una edad válida."