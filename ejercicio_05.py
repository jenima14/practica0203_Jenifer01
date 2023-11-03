numeros = list(range(1, 11))
for i in range(len(numeros) - 1, -1, -1):
    if i != 0:
        print(numeros[i], end=", ")
    else:
        print(numeros[i])
input()