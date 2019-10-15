

numero = float(input ("Digite un numero: "))

def imprimir_tabla(numero):
    
    LIMITE = 10
   
    contador = 1
    while contador <= LIMITE:
        resultado = contador * numero
        print("{} x {} = {}".format(numero, contador, resultado))
  
        contador = contador + 1


imprimir_tabla(numero)