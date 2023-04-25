num1 = int (input("ingrese un  valor "))
num2 = int (input("ingrese un  valor "))
num3 = int (input("ingrese un  valor "))

if (num1 > num2  and num1 > num3):  
   if (num2 > num3):
       print ("El numero mas grande es: ", num1, " y el numero menor es: ", num3)
   else:
       print ("El numero mas grande es: ", num1, " y el numero menor es: ", num2)

if (num2 > num1  and num2 > num3):  
   if (num1 > num3):
       print ("El numero mas grande es: ", num2, " y el numero menor es: ", num1)
   else:
       print ("El numero mas grande es: ", num2, " y el numero menor es: ", num3)

if (num3 > num1  and num3 > num2):  
   if (num1 > num2):
       print ("El numero mas grande es: ", num3, " y el numero menor es: ", num1)
   else:
       print ("El numero mas grande es: ", num3, " y el numero menor es: ", num2)
