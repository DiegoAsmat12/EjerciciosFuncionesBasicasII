#Ejercicio 1
def cuentaRegresiva(numero):
    arregloNumeros = []
    for i in range(numero,0,-1):
        arregloNumeros.append(i)
    return arregloNumeros

print(cuentaRegresiva(5))

#Ejercicio 2
def imprimeDevuelve(arreglo):
    if(len(arreglo)!=2):
        print("El argumento insertado no es valido: no es un arreglo de 2 elementos")
        return
    print(arreglo[0])
    return arreglo[1]

print(imprimeDevuelve([1,2]))

#Ejercicio 3
def primeroMasLongitud(arreglo):
    return arreglo[0]+len(arreglo)

print(primeroMasLongitud([1,2,3,4,5]))

#Ejercicio 4
def mayoresSegundo(arreglo):
    if(len(arreglo)<2):
        return False
    contador=0
    arregloMayor=[]
    for elemento in arreglo:
        if(elemento>arreglo[1]):
            contador+=1
            arregloMayor.append(elemento)
    print(contador)
    return arregloMayor

print(mayoresSegundo([5,2,3,2,1,4]))
print(mayoresSegundo([3]))

#Ejercicio 5
def longitudValor(longitud,valor):
    arreglo=[]
    for i in range(longitud):
        arreglo.append(valor)
    return arreglo

print(longitudValor(4,7))
print(longitudValor(6,2))
