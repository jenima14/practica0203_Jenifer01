lista = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
notas = []
for asignatura in lista:
    nota = input("Escribir la nota de " + asignatura + ": ")
    notas.append(nota)
for i in range(len(lista)):
    print("En", lista[i], "has sacado", notas[i])
input()