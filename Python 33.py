num3=0
num5=0
for f in range(10):
    valor=int(input("Ingrese la nota:"))
    if valor%3==0:
        num3=num3+1
    if valor%5==0:
        num5=num5+1
print("Cantidad de valores ingresados de 3")        
print(num5)
print("Cantidad de valores ingresados de 5")
print(num3)


