# Escribir un programa que pregunte al usuario su edad y muestre por 
# pantalla todos los años que ha cumplido (desde 1 hasta su edad).

def mostrar_anios_cumplidos(edad):
    try:
        edad = int(edad)
        if edad <= 0:
            return "Por favor, ingresa una edad válida."
    except ValueError:
        return "Por favor, ingresa un número entero para tu edad."
        
    mensaje = ""
    for numero in range(1, edad + 1):
        mensaje += "Has cumplido " + str(numero) + " años.\n"
    return mensaje

if __name__ == "__main__":
    # Entrada
    edad = 0
    while edad <= 0:
        try:
            edad = int(input("Por favor, ingresa tu edad (debe ser un número entero positivo): "))
            if edad <= 0:
                print("Por favor, ingresa una edad válida.")
        except ValueError:
            print("Por favor, ingresa un número entero para tu edad.")
    # Procesamiento
    resultado = mostrar_anios_cumplidos(edad)
    # Resultado
    print(resultado)