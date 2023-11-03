palabra = input("Escribir una palabra: ").lower()
for vocal in 'aeiou':
    num_veces = palabra.count(vocal)
    print("La vocal '" + vocal + "' aparece " + str(num_veces) + " veces")
input()