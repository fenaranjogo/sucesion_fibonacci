#Código para generar los n primeros términos de la sucesión de fibonacci

#N es la cantidad de termino de la suseción de finobacci 
N = int(input("Ingrese el número de términos a generar: "))
a = 0
b = 1
for i in range(1,N+1):
    c = a + b
    a = b
    b = c
    print(a, end=' ')
