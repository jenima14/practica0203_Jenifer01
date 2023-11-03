palabra = input("Escribir una palabra: ").lower()
lista_palabra = list(palabra)
palabra_invertida = tuple(reversed(lista_palabra))
es_palindromo = list(lista_palabra) == list(palabra_invertida)
if es_palindromo:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")
input()