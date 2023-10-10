paises = []
habitantes = []

for x in range(5):
    nom1 = input("Ingrese el nombre del país: ")
    paises.append(nom1)
    nom2 = int(input("Ingrese la cantidad de habitantes:"))
    habitantes.append(nom2)
    
for k in range(4):
    for x in range(4-k):
       if(habitantes[x]<habitantes[x+1]):
        aux1 = habitantes[x]
        habitantes[x]= habitantes[x+1]
        habitantes[x+1]= aux1
        aux2= paises[x]
        paises[x]= paises[x+1]
        paises[x]= aux2
print("Lista de paises y sus cantidad de habitantes respectivas")
for x in range(5):
         print(paises[x],habitantes[x])

for x in range(4):
    for k in range(4-x):
       if(paises[k]<paises[k+1]):
        aux1 = paises[k]
        paises[k]= paises[k+1]
        paises[k+1]= aux1
        aux2= habitantes[k]
        habitantes[k]= habitantes[k+1]
        habitantes[k]= aux2
print("Lista de paises y sus orden alfabeticamente")
for x in range(5):
         print(paises[x],habitantes[x])
