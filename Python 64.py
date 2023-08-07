alturas = []
total_alturas = 0

for i in range(5):
    personas = float(input("Ingrese un número: ".format (i + 1)))
    alturas.append(personas)
    total_alturas += alturas
altura_promedio = total_alturas/ 5
altura_baja = 0
altura_alto = 0
  
for altura in altura:
    if  altura > altura_promedio:
        altura_baja += 1
      else altura < altura_promedio:
          altura_alta += 1
print("Las alturas de 5 personas son:", alturas)
print("Altura promedio:", altura_promedio)
print("{} personas están por encima del promedio".format(altura_promedio))
print("{} personas están por debajo del promedio".format(altura_baja))
