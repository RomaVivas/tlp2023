positivo=0
negativo=0
multiplo_15 = 0
par =0
for i in range (10):
    x = int(input("Ingrese un valor"))
    if x > 0:
        print ("el valor ingresado es positivo")
        positivo+=1
    if x < 0:
        print ("el valor ingresado es negativo")
        negativo+=1
    if x%15==0:
        print("el valor es multiplo 15")
        multiplo_15+=1
    if x%2==0:
        print ("el valor es par")
        par+=1
print (" la cantidad de valores positivos ingresados son: ",positivo)
print (" la cantidad de valores negativos ingresados son: ",negativo)
print (" la cantidad de valores multiplos de 15 ingresados son: ",multiplo_15)
print (" la cantidad de valores multiplos de 2 ingresados son: ",par)
