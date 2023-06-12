numeros = [45, 3002, 197, 726, 20, 544, 8, 853]
contar = 0

for numero in numeros:
    if numero > 100:
        contar += 1

print("Hay " + str(contar) + " numeros mayores a 100")
