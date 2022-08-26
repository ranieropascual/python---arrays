print ("------------------------------------------------------")
print ("ejercicio 1 vector 1 lectura de N elementos enteros")
print ("------------------------------------------------------")

#inicializar
i = 1
F = []

#entrada
print ("ingrese numero de elementos a ingresar: ")
numElementos = int(input())
#proceso
while i <= numElementos:
    elemento = int(input("ingrese elemento:"))
    F.append(elemento) #agregamos el elemento a la lista

    i = i + 1
#salida
print(F) #imprimimos la lista

