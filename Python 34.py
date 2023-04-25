cantidad=0
n=int(input("¿Cuantos numeros quiere ingresar?:"))
for f in range(n):
 valor=int(input("Ingrese un valor:"))
 if valor<=1000:
        cantidad=cantidad+1        
print("Cantidad de numeros mayor e iguales a 1000")
print(cantidad)

