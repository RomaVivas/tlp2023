sueldos = []
suma_sueldos = 0

for i in range(5):
    sueldo = float(input("Ingrese el sueldo del operario {}: ".format(i+1)))
    sueldos.append(sueldo)
    suma_sueldos += sueldo

promedio_sueldos = suma_sueldos / 5

print("Los sueldos ingresados son:", sueldos)
print("El promedio de sueldos es:", promedio_sueldos)
