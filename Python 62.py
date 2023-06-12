lista = []

while True:
    num = int(input("Ingrese un número (Ingrese 0 para terminar): "))
    if num == 0:
        break
    lista.append(num)

print("El tamaño de la lista es:", len(lista))
