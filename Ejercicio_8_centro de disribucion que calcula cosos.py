#centro de disribucion que calcula cosos de envio aplicando politicas de descuentos escalonados por volumen y promocion por metodo de pago.

pesomercancias = int(input("Ingrese el peso de la mercancia en kg: "))
Valormercancias = int(input("Ingrese el valor de la mercancia: "))
metododepago= str(input("Ingrese el metodo de pago (efectivo, tarjeta): "))

#Calcular tarifa de envio
if(pesomercancias <= 500):
    tarifaenvio = 40000

elif(pesomercancias > 500 and pesomercancias <= 750):
    tarifaenvio = 80000

elif(pesomercancias > 750 and pesomercancias <= 1000):
    tarifaenvio = 100000

else:
    (pesomercancias > 1000)
    tarifaenvio = 100000 + ( ( (pesomercancias - 1000) // 10 ) * 500 )

print("El valor de la mercancia que desea llevar es de: ", Valormercancias)
print("El peso de la mercancia es de: ", pesomercancias, "kg")
print("El valor de la tarifa de envio es de: ", tarifaenvio)

# Descuento en el valor del envio

descuentoenvio = 0

if 300000 <= Valormercancias <= 600000:
    descuentoenvio = tarifaenvio * 0.20

elif 600000 < Valormercancias <= 1000000:
    descuentoenvio = tarifaenvio * 0.35

elif Valormercancias > 1000000:
    descuentoenvio = tarifaenvio * 0.50

tarifaenviodescuento = tarifaenvio - descuentoenvio


#Metodos de pago 

if(metododepago == "tarjeta"):
    tarifaenviodescuento = 0
    print("No se cobra tarifa de envio")


elif(metododepago == "efectivo"):
    if Valormercancias > 500000:
        tarifaenviodescuento = 0
        print("No se cobra tarifa de envio")

    elif 300000 < Valormercancias < 500000:
        tarifaenviodescuento = tarifaenviodescuento * 0.50

# Calculo del valor total
valortotal = Valormercancias + tarifaenviodescuento

print("Resumen de la compra:")
print("Valor de la mercancía:" , Valormercancias)
print("Tarifa de envío final:", tarifaenviodescuento)
print("Valor total a pagar: " , valortotal)