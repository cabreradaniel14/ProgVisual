numero = int(input("Dígame cuántas materias quiere: "))

if numero < 1:
    print("Introduzca minimo una:")
else:
    lista = []
    for i in range(numero):
        print("Escriba el nombre de la materia", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    print("Las materias son:", lista)