# CALCULAR AREA Y PERIMETRO DEL CIRCULO

# ingresa por teclado el radio (r)
import math
pi=math.pi

# DATOS
radio=float(input('ingrese el radio del circulo: '))

# OPERACION
area=pi*(radio**2)
per=2*radio*pi

# RESULTADO
print('Area= ',area)
print('Perimetro= ',per)


