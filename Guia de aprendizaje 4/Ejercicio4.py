'''
Desarrolle un programa que invierta un número entero N dado por el usuario. Por ejemplo, de 12345
su número invertido es 54321.

'''

from ntpath import join


def invertir():

    while(True):
        
        Num=int(input("Ingrese un numero a convertir: "))

        Num = str(Num)

        print("".join(reversed(Num)))

        if Num==0 :
            break
        

invertir()