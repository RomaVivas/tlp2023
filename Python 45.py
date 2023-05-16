continuar = 1
suma=0
while continuar == 1:
    numero = int(input("Ingresa un número entero: "))
    suma += numero
    respuesta = input("¿Deseas ingresar otro número? Si es asi ingrese SI: ")
    if respuesta != "SI":
        continuar = 0
        print("La suma de los números ingresados es:", suma)
        print("El programa finalizó")
