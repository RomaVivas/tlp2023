res=0
res1=0
res2=0
for tm in range(5):
    tmedad= int(input("ingrese la edad del estudiante (TM)"))
    res=tmedad+res
for tt in range (6):
    ttedad=int(input("ingrese la edad del estudiante (TT)"))
    res1=ttedad+res1
for tn in range (11):
    tnedad =int (input("ingrese la edad del estudiante (TN)"))
    res2=tnedad+res2
res=res/5
res1=res1/6
res2=res2/11
print("El promedio de edad de TM es",res)
print("El promedio de edad de TT es",res1)
print("El promedio de edad de TN es",res2)
if res > res1 and res > res2:
    print("El promedio mayor es el TM")
if res1 > res and res1 > res2:
    print("El promedio mayor es el TT")
if res2 > res and res2 > res1:
    print("El promedio mayor es el TN")
