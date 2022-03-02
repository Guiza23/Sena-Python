'''
Diseñe un pseudocódigo que lea el valor de un ángulo expresado en radianes y calcule e imprima el
valor del seno de dicho ángulo. Se leerá también el número de términos de la serie.
SEN(X) = X - ( X 3 / 3 ! ) + ( X 5 / 5 ! ) - (X7/ 7!) + .....

'''

def factorial():
    fac= 1

    num=int(input("Ingrese un numero: "))
    for i in range (2,(num + 1)):
        fac= fac * i
        print(fac)
    
    
factorial()
