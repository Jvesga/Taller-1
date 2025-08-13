numero=int(input("Digite el un numero: "))
modulo= numero % 2
if (modulo==0):
    potencia= numero**3
    print("El numero escrito es par y el resultado de su potencia cubica es: " , potencia)
else:
    potencia= numero**2
    print("El numero escrito es impar y el resultado de su potencia cuadrada es: " , potencia)