lista_num_ganadores = []
numeros = int(input("Escribir la cantidad de números ganadores de la PRIMITIVA: "))
for i in range(numeros):
    num_ganador = int(input("Escribe un número ganador: "))
    lista_num_ganadores.append(num_ganador)
lista_num_ganadores.sort()
print("Números ganadores ordenados de menor a mayor:")
for numero in lista_num_ganadores:
    print(numero)
input()