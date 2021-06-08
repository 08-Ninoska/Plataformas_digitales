# ingrese un numero y diga si es par o impar
"""
1. pedir al usuario ingresar un numero
2. hacer el calculo para ver si es par o impar (variable % 2== 0 es  par)
3. mostrar el mensaje
"""

numero= int(input("ingresar el numero: "))

if (numero == 0):  #si el numero es igual a cero
    print("cero")
elif(numero % 2 == 0): #caso contrario si el numero mod 2 es cero
    print("el numero es par ")
else:   #caso contrario
    print("el numero es impar ")

