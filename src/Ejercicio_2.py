# Escribir un programa que pida al usuario un número entero positivo y 
# muestre por pantalla todos los números impares desde 1 hasta ese número 
# separados por comas.

def numeros_impares_hasta_n(numero):
    if not str(numero).isdigit() or int(numero) <= 0:
        raise ValueError("Por favor, ingrese un número entero positivo válido.")
    impares = []
    numimpar = 1
    while numimpar <= numero:
        impares.append(str(numimpar))
        numimpar += 2
    return ", ".join(impares)

if __name__ == "__main__":
    impares = []
    numimpar = 1
    numero_correcto = False
    while not numero_correcto:
        try:
            # Entrada
            numero = int(input("Por favor, ingrese un número entero positivo: "))
            # Procesamiento
            resultado = numeros_impares_hasta_n(numero)
            # Salida 1
            print("Números impares desde 1 hasta", numero, ":", resultado)
            numero_correcto = True
        except ValueError as e:
            # Salida 2
            print("Error:", e)