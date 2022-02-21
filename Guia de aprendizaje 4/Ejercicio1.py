'''
Realiza un programa en Python, que pida números mientras no se ingrese uno negativo. Al final, se
debe mostrar la suma de los números ingresados.

'''
def num():

    #Variables
    Contador=0
    Suma=0

    while (Contador == 0): 
        Num=int(input("Ingrese un numero: "))

        #conditional
        if Num < 0:
            Contador = Num
  
        else:
            Suma= Suma +Num

    #prints
    print("La suma de los numeros ingresados es: {} ".format(Suma))

num()