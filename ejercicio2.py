print ("------------------------------------------------------")
print ("ejercicio 2")
print ("------------------------------------------------------")

#inicializar
suma =0
media =0.0
C =0
TEMP = [] #lista vacia para almacenar temperaturas

#entradas
print("ingrese cantidad de temperaturas:")
N = int(input())

#proceso
for i in range(N):   
    temperatura = float(input("ingrese temperatura {0}: ".format(i + 1)))
    TEMP.append(temperatura)
    suma = suma + TEMP[i] #division real

media = suma / N #division real

    #contar cuantas temperaturas son mayor que la media

for tempElement in TEMP:
    if tempElement >= media:
        C = C + 1
        print (tempElement)

#salida
print ("------------------------------------------------------")
print ("la media es: ", media)
print("total de temperaturas >= a la media es: ",C)


