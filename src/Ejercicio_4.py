# Escribir un programa que pida al usuario un número entero, si la entrada no es 
# correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción 
# capturada.

def obtener_entero(numeroEnt):
    try:
        numeroEnt = int(numeroEnt)
        if numeroEnt > 0:
            return numeroEnt
        else:
            raise ValueError("Error: El número debe ser mayor que 0.")
    except ValueError:
        raise ValueError("Error: La entrada debe ser un número entero válido.")

if __name__ == "__main__":
    numeroEnt = None
    while numeroEnt is None or numeroEnt <= 0:
        try:
            numeroEnt = int(input("Escribe un número entero mayor que 0: "))
            numero = obtener_entero(numeroEnt)
            print("Número ingresado:", numero)
        except ValueError:
            print("Error: La entrada no es un número entero válido o es una letra.")