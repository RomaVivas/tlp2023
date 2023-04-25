cantidad=0
calculo=0
superficie=0
n=int(input("¿Cuantos numeros quiere ingresar?:"))
for f in range(n):
 base=int(input("Ingrese el valor de base:"))
 altura=int(input("Ingrese el valor de altura:"))
 superficie=(base*altura/2)
 if superficie>=12:
        cantidad=cantidad+1        
print("Cantidad de triangulos con superficie igual o mayor a 12")
print(cantidad)
