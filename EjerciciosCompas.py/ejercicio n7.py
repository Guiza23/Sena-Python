"""Cinco miembros de un club contra la obesidad desean saber cuánto han bajado o subido de peso
desde la última vez que se reunieron. Para esto se debe realizar un ritual de pesaje en donde cada
uno se pesa en diez básculas distintas para así tener el promedio más exacto de su peso. Si existe
diferencia positiva entre este promedio de peso y el peso de la última vez que se reunieron, significa
que subieron de peso. Pero si la diferencia es negativa, significa que bajaron. Lo que el problema
requiere es que por cada persona se imprima un letrero que diga: “SUBIO” o “BAJO” y la cantidad de
kilos que subió o bajo de peso."""

miembros=0
suma_peso=0
while miembros <5: # condiciono con while para cada miembro cuando llegue a cinco se rompe
    print("integrante numero n° " + str (miembros + 1))
    peso_anterior=int(input("ingrese su peso anterior:"))
    miembros=miembros+1 # acumulo cada miembro
    print("================================================")

    basculas=0
    while basculas<3: # acumulo las basculas
        print("bascula numero n° "  + str (basculas + 1))
        peso_actual=int(input("cual es su peso "))
        basculas=basculas+1 # las acumulo para que cuando llegue a 10 me muestre el resultado
        suma_peso=suma_peso + peso_actual
        promedio=suma_peso/basculas
        print("======================================================")
    
    suma_peso=0

    
    if promedio > peso_anterior: #muestro los resultados!!! 
        print("HAS SUBIDO DE PESO")
        print("*****************************")
    elif promedio==peso_anterior:
        print("tu peso no ha cambiado")
    else:
        print(" HAS BAJADO DE PESO")
        print("******************************")
    



