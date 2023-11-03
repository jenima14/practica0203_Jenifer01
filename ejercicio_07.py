abecedario = list("abcdefghijklmnopqrstuvwxyz")
letras_resultante = []
for i in range(len(abecedario)):
    if (i + 1) % 3 != 0:
        letras_resultante.append(abecedario[i])
print("Lista resultante:")
print(letras_resultante)
input()