num_equilateros= 0
num_isosceles=0
num_escalenos=0
n=int(input("ingrese los lados del triangulo"))
for n in range:
   lado1(float("ingrese el primer lado:"))
   lado2(float("ingrese el segundo lado:"))
   lado3(float("ingrese el tercer lado: "))
   if lado1 == lado2 == lado3:
      tipo = "equilatero"
      num_equilatero= num_equilatero +1
   else:
      if lado1 == lado2 or lado2 == lado3 or ladol == lado3:
         tipo = "isosceles"
         num_isosceles= num_isosceles +1
      else:
           if lado1 != lado2 or lado2 != lado3 or ladol != lado3:
               tipo = "escalenos"
               num_escalenos= num_escaleno +1
print ("el triangulo es ", tipo)
print ("cantidad de triangulos equilateros", num_equilatero)
print ("cantidad de triangulos isocsceles", num_isosceles)
print ("cantidad de triangulos escalenos", num_escalenos)
