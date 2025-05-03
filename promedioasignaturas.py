def ingresar_estudiante():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    materias = []
    promedios = []
    while True:
        materia = input("Materia (o 'fin' para terminar): ")
        if materia.lower() == 'fin':
            break
        materias.append(materia)
        promedio = float(input(f"Promedio de {materia}: "))
        promedios.append(promedio)
    promedio_general = sum(promedios) / len(promedios) if promedios else 0
    return {'nombre': nombre, 'edad': edad, 'materias': materias, 'promedio': promedio_general}

estudiantes = []
while True:
    estudiantes.append(ingresar_estudiante())
    if input("¿Otro estudiante? (s/n): ").lower() != 's':
        break

print("\nInformación de todos los estudiantes:")
for i, est in enumerate(estudiantes, 1):
    print(f"\nEstudiante {i}: {est['nombre']}")
    print(f"  Edad: {est['edad']}")
    print(f"  Materias: {', '.join(est['materias'])}")
    print(f"  Promedio: {est['promedio']:.2f}")

mayores_a_8 = sum(e['promedio'] > 8 for e in estudiantes)
print(f"\nCantidad con promedio > 8: {mayores_a_8}")




