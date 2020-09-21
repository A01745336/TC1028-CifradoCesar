#codificación
#Recebir el mensaje que se quiera codificar
#Recibir el numero de casillas para lograr la codificación
#Iniciar un ciclo for que recorra todas las letras del texto
#Cambiar los caracteres a valor numerico con chr
#Sumar el numero de casillas a la letra en cuestion
#Cambiar los valores numericos a caracteres con ord
#Ir construyendo el mensaje desencriptado
def codificacion_cesar (mensaje, casillas):
    letraEncriptada = ""
    mensajeE = ""
    for indice in range (len(mensaje)):
        letraEncriptada=chr (ord(mensaje[indice])+casillas)
        mensajeE=mensajeE+letraEncriptada
    return mensajeE

#codificación
#Recibir el mensaje que se quiera decodificar
#Recibir el numero de casillas para lograr la decodificación
#Iniciar un ciclo for que recorra todas las letras del texto
#Cambiar los caracteres a valor numerico
#Restar el numero de casillas a la letra en cuestion
#Cambiar los valores numericos a caracteres
#Ir construyendo el mensaje encriptado
def decodificacion_cesar(mensajeE, casillas):
    letraDesencriptada = ""
    mensajeD = ""
    for indice in range (len(mensajeE)):
        letraDesencriptada=chr (ord(mensajeE[indice])-casillas)
        mensajeD=mensajeD+letraDesencriptada
    return mensajeD

print (codificacion_cesar("Hola Mundo", 3))
print (decodificacion_cesar("Krod#Pxqgr", 3))
