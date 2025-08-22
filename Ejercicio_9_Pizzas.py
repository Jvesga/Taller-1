#La pizzería Pequeña Italia ofrece pizzas vegetarianas y 
#no vegetarianas a sus clientes. 
#Los ingredientes para cada tipo de pizza aparecen a continuación.

#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
#y en función de su respuesta le muestre un menú con los 
#ingredientes disponibles para que elija. Solo se puede 
#elegir un ingrediente además de la mozzarella y el tomate que están en todas las pizzas. 
#Al final se debe mostrar por pantalla 
#si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

print("Pequeña italia ofrece pizzas vegetarianas y no vegetarianas")
pizza_cliente=input("Que tipo de pizza desea: ")

vegetariana=("vegetariana")
no_vegetariana=str("no vegetariana")
ingrediente1=("pimiento")
ingrediente2=("tofu")
ingrediente3=("peperoni")
ingrediente4=("jamon")
ingrediente5=("salmon")

if(pizza_cliente==vegetariana):
    print("La pizza que desea es vegetaria y nuestros ingredientes son" , "pimiento o tofu" )
    a=input("Elija un ingrediente: ")
    print("La pizza que elijio es Vegetariana y tiene los siguientes ingredientes:" , "mozzarella, tomate y" , a)
else:
    (pizza_cliente==no_vegetariana)
    print("La pizza que desea no es vegetaria y nuestros ingredientes son" , "peperoni, jamon o salmon")
    b=input("Elija un ingrediente: ")
    print("La pizza que elijio no es Vegetariana y tiene los siguientes ingredientes:" , "mozzarella, tomate y " , b)
