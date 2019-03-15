from Pila import Pila
from Colas import Cola

cola_trabajo = Cola()
n = 8
binario = 1011101101110101011
#print(binario)

residuo = binario % 10
resultado = int(binario / 10)
numeroFinal = residuo * pow(2, 0)



residuo = resultado % 10
resultado = int(resultado / 10)
numeroFinal = numeroFinal + (residuo * pow(2, 1))

residuo = resultado % 10
resultado = int(resultado / 10)
numeroFinal = numeroFinal + (residuo * pow(2, 2))

residuo = resultado % 10
resultado = int(resultado / 10)
numeroFinal = numeroFinal + (residuo * pow(2, 3))

residuo = resultado % 10
resultado = int(resultado / 10)
numeroFinal = numeroFinal + (residuo * pow(2, 4))


residuo = resultado % 10
resultado = int(resultado / 10)
numeroFinal = numeroFinal + (residuo * pow(2, 5))

residuo = resultado % 10
resultado = int(resultado / 10)
numeroFinal = numeroFinal + (residuo * pow(2, 6))

residuo = resultado % 10
resultado = int(resultado / 10)
numeroFinal = numeroFinal + (residuo * pow(2, 7))

residuo = resultado % 10
resultado = int(resultado / 10)
numeroFinal = numeroFinal + (residuo * pow(2, 8))

residuo = resultado % 10
resultado = int(resultado / 10)
numeroFinal = numeroFinal + (residuo * pow(2, 9))

residuo = resultado % 10
resultado = int(resultado / 10)
numeroFinal = numeroFinal + (residuo * pow(2, 10))
#print(resultado)
#print(numeroFinal)



resultado = binario
n = 0
numeroFinal = 0
residuo = 0
#print(binario)

while (binario != 0):
    #print ('Paso ', n)
    residuo = binario % 10
    #print('El residuo es ', residuo)
    binario = int(binario / 10)
    numeroFinal = numeroFinal + (residuo * pow(2, n))
    #print('La suma es ', numeroFinal)
    n = n + 1


#print (numeroFinal)

# 101110110
# 10111011      0 x 2^0
# 1011101       1 x 2^1
# 101110        1 x 2^2
# 10111         0 x 2^3
# 1011          1 x 2^4
# 101           1 x 2^5
# 10            1 x 2^6
# 1             0 x 2^7
#

# 6789
# 6789  /   10      = 678
# 6789  %   10              = 9
# 678   /   10      = 67
# 678   %   10              = 8
# 67    /   10      = 6
# 67    %   10              = 7
# 6     /   10      = 0
# 6     %   10              = 6



# 4 = 3 + 1
# 4 = 2 + 1 + 1
# 4 = 1 + 1 + 1 + 1

# 4 = 2 + 2

# 4 = 1 + 3


# 5 = 4 + 1
# 5 = 3 + 1 + 1
# 5 = 2 + 1 + 1 + 1
# 5 = 1 + 1 + 1 + 1 + 1

# 5 = 3 + 2
# 5 = 2 + 1 + 2

# 5 = 2 + 3

# 5 = 1 + 4





"""
if (n % 2 == 0):
    suma = n + (n-2) + (n-4) + (n-6)
    suma2 = 8 + 6 + 4 + 2
    print (suma)
else:
    print ('El numero es impar')
"""

suma = 0

a = [121, 55, 22, 13, 12]

b = a[0] + a[1] + a[2] + a[3] + a[4]

for i in range(len(a)):
    suma = suma + a[i]
#print(suma)

def sumarArreglo(arreglo):
    if(len(arreglo) == 1):
        return arreglo[0]
    else:
        return arreglo[0] + sumarArreglo(arreglo[1:])

# a = [22, 13, 55, 12, 121]
# 22 + (a = [13, 55, 12, 121])
# 22 + 13 + (a = [55, 12, 121])
# 22 + 13 + 55 + (a = [12, 121])
# 22 + 13 + 55 + 12 + (a = [121])
# 22 + 13 + 55 + 12 + 121

#print(sumarArreglo(a))
#print (suma)


def sumarNumero(num):
    if(num == 1):
        return 1
    else:
        return sumarNumero(num-1) + num

def sumarPares(num):
    if (num == 2):
        return 2
    else:
        return sumarPares(num - 2) + num

#print(sumarPares(10))

print (a)
rango = len(a)
for x in range(rango):
    l = x + 1
    for l in range(rango):
        w = l
        #print (x, l)

for i, item in enumerate(a):
    for item2 in a[(i+1):]:
        if (a[i] > item2):
            w = a.index(item2)
            temp = a[i]
            a[i] = item2
            a[w] = temp


def ordernarArreglo(arreglo):
    if(len(arreglo) == 1):
        return arreglo[0]
    else:
        for x in range(len(arreglo)):
            if (arreglo[0] > arreglo[x]):
                temp = arreglo[0]
                arreglo[0] = arreglo[x]
                arreglo[x] = temp
        return ordernarArreglo(arreglo[1:])

print (ordernarArreglo(a))