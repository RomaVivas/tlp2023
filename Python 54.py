clave = input("Ingrese su clave: ")

while len(clave) < 10 or len(clave) > 20:
    clave = input("La clave ingresada no es válida. Por favor, ingrese una clave entre 10 y 20 caracteres: ")

print("Clave ingresada correctamente: ", clave)
