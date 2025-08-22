#Sistema de procesamiento matemático para valores no negativos que 
#valide y realice las siguientes operaciones:
#1.	Leer dos números enteros positivos únicamente
#2.	Sumar los dos números leídos
#3.	Restarle al primer número el segundo
#4.	Multiplicar los dos números
#5.	Dividir el primer número dado por el segundo

print("Por favor solo dijite numeros positivos")
numero1=int(input("Dijite el primero numero: "))
numero2=int(input("Dijite el segundo numero: "))

sumar=(numero1 + numero2)
print("La suma de los numero dados es de: " , sumar)

dividir=int(numero1/numero2)
print("La division de los numero dados es de: " , dividir)

if(numero1 > numero2):
    resta=(numero1-numero2)
    print("La resta de los numero dados es de: " , resta)
else:
    print("La resta de los numero dados no es posible ya que daria un valor negativo o igual a cero.")

if(numero1 and numero2 != 0):
    multiplicar=(numero1*numero2)
    print("La multiplicacion de los numero dados es de: " , multiplicar)
