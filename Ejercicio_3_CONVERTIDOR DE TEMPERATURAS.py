### CONVERTIDOR DE TEMPERATURAS ###
### Un laboratorio necesita convertir mediciones térmicas desde la escala Celsius hacia las escalas Fahrenheit (usada en países anglosajones) y Kelvin (escala absoluta científica). ###


celcius= float(input("Digite la temperatura en grados celcius: "))

fahrenheit= (celcius * 9/5) + 32 
kelvin= celcius + 273.15

print("La temperatura digitada es de" , celcius , "°")
print("la conversion de temperatura a escala Fahrenheit es: " , fahrenheit , "°F" )
print("la conversion de temperatura a escala Kelvin es: " , kelvin , "°K" )

