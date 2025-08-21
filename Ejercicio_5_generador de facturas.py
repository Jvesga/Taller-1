#5.	Una empresa necesita generar facturas considerando:#
#- Precio base del producto#
#- Impuesto sobre Valor Agregado (IVA del 16%)#
#- Descuento por volumen (15% si el total supera $500,000)#

precio_base=int(input("Dijite el valor del producto: "))
cantidad=int(input("Dijite cuantos productos desea llevar el cliente: "))
total=int(precio_base*cantidad)
total_iva=int(total * 0.16)
total_iva2=int(total + total_iva)

print("El precio base de su producto es de: " , precio_base)
print("La cantidad que desea comprar es de: " , cantidad)
print("El total de su compra sin iva es de: " , total)
print("El total de su compra con iva es de: " , total_iva2)

if(total_iva2 > 500000):
    descuento_volumen=int(total_iva * 0.15)
    total_con_descuento=int(total_iva2 - descuento_volumen)
    print("El total de su compra con descuento es de: " , total_con_descuento)
