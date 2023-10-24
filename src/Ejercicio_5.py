# Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance 
# la excepción NameError con el mensaje, "Incorrect Password!!"

def verificaContrasenia(contrasenia, contraseniaUser):
    if contraseniaUser != contrasenia:
        raise NameError("Incorrect Password!!")

if __name__ == "__main__":
    contrasenia = "Hola1234"
    contraseniaUser = ""
    while contrasenia != contraseniaUser:
        try:
            contraseniaUser = input("Escribe tu contraseña: ")
            verificaContrasenia(contrasenia, contraseniaUser)
        except NameError as e:
            print(e)