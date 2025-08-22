#Módulo de seguridad que valida credenciales de acceso 
# mediante secuencia numérica predefinida. 
# El sistema evalúa la coincidencia exacta 
# con el código de autenticación establecido.

#registro de nuevo usuario
nombreusuario=input("Por favor ingrese el nombre del nuevo usuario: ")
codigodeverificacionnuevousuario=input("Por favor ingrese el código de verificación del nuevo usuario: ")

#autenticacion
 
nombreusuarioautenticacion=input("Por favor ingrese el nombre del usuario para autenticación: ")
codigodeverificacionautenticacion=input("Por favor ingrese el código de verificación para autenticación: ")

#verificancion de credenciales  

if nombreusuarioautenticacion==nombreusuario:
    print("Nombre de usuario correcto")

else:
    print("Nombre de usuario incorrecto")

if codigodeverificacionautenticacion==codigodeverificacionnuevousuario:
    print("Código de verificación correcto")

else:
    print("Código de verificación incorrecto")
    print("Acceso denegado")


if nombreusuarioautenticacion==nombreusuario and codigodeverificacionautenticacion==codigodeverificacionnuevousuario:
    print("Acceso concedido")  