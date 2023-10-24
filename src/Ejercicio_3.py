# Escribir un programa que pida al usuario un número entero positivo y muestre 
# por pantalla la cuenta atrás desde ese número hasta cero separados por comas. 
# Deberá solicitar el número hasta introducir uno correcto.

def cuenta_regresiva(numero, cuenta_atras):
    try:
        numero = int(numero)
        if numero <= 0:
            raise ValueError("Por favor, ingrese un número entero no negativo y mayor que 0.")
        while numero >= 0:
            cuenta_atras.append(str(numero))
            numero -= 1
        return ", ".join(cuenta_atras)
    except ValueError as e:
        raise ValueError(str(e))

if __name__ == "__main__":
    # Entrada
    cuenta_atras = []
    numero = None
    # Procesamiento
    while numero is None or numero < 0:
        try:
            numero = int(input("Por favor, ingrese un número entero no negativo: "))
            resultado = cuenta_regresiva(numero, cuenta_atras)
            print("Cuenta regresiva desde", numero, "hasta 0:", resultado)
        except ValueError as e:
            print("Error:", e)