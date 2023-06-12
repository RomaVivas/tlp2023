oracion = input("Ingresa una oración: ")
contador_vocales = 0
for letra in oracion:

  if letra.lower() in 'aeiou':
        contador_vocales += 1
oracion_mayuscula = oracion.upper()
longitud_oracion = len(oracion)
print("La oración tiene", contador_vocales, "vocales.")
print("La oración en mayúsculas es:", oracion_mayuscula)
print("La oración tiene", longitud_oracion, "caracteres.")
