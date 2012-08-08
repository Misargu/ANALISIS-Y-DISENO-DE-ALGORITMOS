print "Programa Para calcular el IMC \nEl indice de masa corporal (IMC) \nes una medida de asociacion \nentre el peso y la talla \nde un individuo \n \n"
peso= input("Digite su Peso \n")
estatura = input("Digite Su Estatura \n")
imc = (peso)/(estatura**2)
print "Su IMC es de : ",imc

if imc < 18.50 and imc > 16:
    print "\nEstado nutricional es INFRAPESO"
if imc < 16:
    print "\nEstado nutricional es DELGADEZ SEVERA"
if imc > 17 and imc <18.49:
    print "\nEstado nutricional es DELGADEZ NO MUY PRONUCIADA"
if imc >18.5 and imc < 25:
    print "\nEstado nutricional es NORMAL"
if imc >= 25 and imc < 30:
    print "\nEstado nutricional es SOBREPESO - PREOBESO"
if imc > 30 and imc < 35:
    print "\nEstado nutricional es OBESO TIPO 1"
if imc >= 35 and imc < 40:
    print "\nEstado nutricional es OBESO TIPO 2"
if imc >= 40:
    print "\nEstado nutricional es OBESO TIPO 3"
    
