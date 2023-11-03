lista = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
aprobadas = []
for cursos in lista:
    nota = float(input("Escribe la nota de " + cursos + ": "))
    if nota >= 5.0:
        aprobadas.append(cursos)
for aprobada in aprobadas:
    lista.remove(aprobada)
print("Las asignaturas que tienes que repetir son:")
for asignatura_repetir in lista:
    print(asignatura_repetir)
input()