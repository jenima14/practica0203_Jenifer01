muestra_numeros = input("Escribir una muestra de números separados por comas: ").split(',')
numeros = [float(numero) for numero in muestra_numeros]
media = sum(numeros) / len(numeros)
variacion = sum((X - media) ** 2 for X in numeros) / len(numeros)
desviacion_tipica = variacion ** 0.5
print("La media de los números es: ", media)
print("La desviación típica de los números es: ", desviacion_tipica)
input()