# Escribir un programa que pida al usuario un número entero positivo y muestre 
# por pantalla la cuenta atrás desde ese número hasta cero separados por comas. 
# Deberá solicitar el número hasta introducir uno correcto.

def cuenta_regresiva(numero, cuenta_atras):
    try:
        numero = int(numero)
        if numero < 0:
            raise ValueError("Por favor, ingrese un número entero positivo válido.")
        while numero > 0:
            cuenta_atras.append(str(numero))
            numero -= 1
        return ", ".join(cuenta_atras)
    except ValueError:
        raise ValueError("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    cuenta_atras = []
    numero = -1
    while numero < 0:
        try:
            numero = int(input("Por favor, ingrese un número entero positivo: "))
            if numero < 0:
                print("Error: El número debe ser positivo.")
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")
    resultado = cuenta_regresiva(numero, cuenta_atras)
    print("Cuenta regresiva desde", numero, "hasta 0:", resultado)