nombre= input("ingrese su nombre minuscula: ")
vocales=['a', 'e','i','o','u']
if nombre[0] in vocales:
   print ("el nombre ingresado comienza con una vocal.")
else: 
    print ("el nombre ingresado no comienza con una vocal")
    
    print ("el primer caracter de su nombre es", nombre[0])
    print ("su nombe no tiene vocales", len(nombre), "letras")
