
while(True):

    print("|* bienvenido a la pizaria las primisias *|")

    entrada=input(" *** oprime la tecla y para iniciar el programa *** :")
    
    if entrada == ("y") :

        tamaño =  str.lower (input("de que tamaño quiere su pizza grande,mediana,pequeña: "))

        sencilla = str.lower (input("quiere la pizza sencilla sin nada de ingredientes solo salsa y carne?: "))

        ingredientes = str.lower (input("o desea su pizza con ingredientes  como pepinillos, champiñones o cebolla? : "))
    
    # cuando es sincilla
    
    if tamaño == ("grande") and  sencilla == ("si"):
        print("=============================================================")
        print(f"el precio  de la pizza grande sencilla es de {60000} $ pesos")
        print("=============================================================")

    elif tamaño == ("mediana") and sencilla == ("si"):
        print("==============================================================")
        print(f"el precio de la pizza mediana sencilla es de {35000} $ pesos ")
        print("==============================================================")
    
    elif tamaño == ("pequeña") and sencilla == ("si"):
        print("======================================================")
        print(f" el precio de la pizza pequeña es de {25000} $ pesos ")
        print("======================================================")
    
        # cuando va con  ingredientes
        # #la grande con ingredientes
        
    elif tamaño == ("grande") and sencilla == ("no") and ingredientes == ("si"):
        print("*** la pizza grande de base te vale 60000 pesos***")
        print("**** ¡recuerede que los ingredientes tiene un costo adicional al de la pizza en si¡ ****")
        print("*****cuantos ingredientes desea en su pizza solo hay tres****")
        ingredientes = str.lower (input("cebolla | pepinillos | champiñones ¿cuantos quiere?"))
        
        if ingredientes == ("los tres") or ("todos"):
              print("** cada ingrediente  tiene un costo de 3000 pesos los tres suman 9000 **")
              print("==============================================================")
              print(f"la pizza grande con los tres ingredientes le vale {60000+9000} $ pesos" )
              print("==============================================================")
        if ingredientes == ("uno"):
            cual=input("cual")
            if cual == ("pepinillos") or ("champiñones") or ("cebolla"):
                print("=====================================================================")
                print(f"el precio de la pizza grande mas un ingrediente  es de {60000+3000} $ pesos ")
                print("======================================================================")

        if ingredientes == ("dos"):
            cual = input ("cuales")
            if ingredientes ==("pepinillos y champiñones") or ("champiñones y cebolla") or ("pepinillos y cebolla"):
                print("=====================================================================")
                print(f"el precio de la pizza grande mas dos ingredientes es de {60000+6000} $ pesos ") 
                print("======================================================================")


                                    # mediana con ingredientes

    elif tamaño == ("mediana") and sencilla == ("no") and ingredientes == ("si"):
        print("*** la pizza mediana de base te vale 35000 pesos***")
        print("*****cuantos ingredientes desea en su pizza solo hay tres****")
        ingredientes = str.lower (input("cebolla | pepinillos | champiñones ¿cuantos quiere?"))
        
        if ingredientes == ("los tres") or ("todos"):
            print("============================================================================")
            print(f"la pizza mediana con los tres ingredientes le vale  {35000+9000} $ pesos ")
            print("=============================================================================")

        if ingredientes == ("uno"):
            cual = input("cual")
            if cual == ("pepinillos") or ("champiñones") or ("cebolla"):
                print("==============================================================================")
                print(f"el precio de la pizza mediana mas un ingrediente  es de {35000+3000} $ pesos ")
                print("==============================================================================")

        if ingredientes == ("dos"):
            cual = input ("cuales")
            if ingredientes ==("pepinillos y champiñones") or ("champiñones y cebolla") or ("pepinillos y cebolla"):
                print("==============================================================================")
                print(f"el precio de la pizza mediana mas dos ingredientes es de {35000+6000} $ pesos") 
                print("==============================================================================")

                         # pequeña con ingredientes

    elif tamaño == ("pequeña") and sencilla == ("no") and ingredientes == ("si"):
        print("*** la pizza pequeña de base te vale 25000 pesos***")
        print("*****cuantos ingredientes desea en su pizza solo hay tres****")
        ingredientes = str.lower (input("cebolla | pepinillos | champiñones ¿cuantos quiere?"))
        
        if ingredientes == ("los tres") or ("todos"):
            print("=================================================================")
            print(f"la pizza mediana con los tres ingredientes le vale {25000+9000} $ pesos" )
            print("=================================================================")

        if ingredientes == ("uno"):
            cual = input("cual")
            if cual == ("pepinillos") or ("champiñones") or ("cebolla"):
                print("==============================================================================")
                print(f"el precio de la pizza pequeña mas un ingrediente  es de {25000+3000} $ pesos")
                print("==============================================================================")

        if ingredientes == ("dos"):
            cual = input ("cuales")
            if ingredientes ==("pepinillos y champiñones") or ("champiñones y cebolla") or ("pepinillos y cebolla"):
                print("================================================================================")
                print(f"el precio de la pizza pequeña mas dos ingredientes es de {25000+6000} $ pesos ")
                print("================================================================================")
    salida=input("si quiere salir del programa oprima la tecla n si quieres continuar oprima la tecla y :")
    if salida == ("n"):
        break
print("=========================")
print("***==== ¡the end! ====***")
print("==========================")