antiguedad=int (input("ingrese cuantos años de antiguedad tiene "))
sueldo=int (input("ingrese el valor de su sueldo "))
if sueldo > 500 and antiguedad <= 10:
    aumento = (sueldo*20/100)
    resultado= sueldo + aumento
    print("el resultado es ")
    print(resultado)
else:
    if sueldo < 500 and antiguedad >= 10:
        aumento2 = (sueldo*5/100)
        resultado= sueldo + aumento2
        print("el resultado es ")
        print(resultado)
