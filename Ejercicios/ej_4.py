# Ejercicio de Listas y Estructuras de Datos en Python
# Enunciado ==> Trabaja con la siguiente lista

calificaciones = []
for i in range (3):
    calificaciones.append ( float(input (f"Ingrese la {i+1} calificación: ")))
print ("\n ----------------------------------------------------------------------- ")
# Imprime la lista de calificaciones
print("Calificaciones => ", calificaciones)

# Imprime la calificación más alta
print("Calificación más alta => ", max(calificaciones))

# Imprime la calificación más baja  
print("Calificación más baja => ", min(calificaciones))

# Imprime el promedio de las calificaciones
promedio = sum(calificaciones) / len(calificaciones)
print("Promedio de calificaciones => ", promedio)

print ("\n ----------------------------------------------------------------------- ")

# Imprime las calificaciones ordenadas de menor a mayor
calificaciones.sort()   
print("Calificaciones ordenadas de menor a mayor => ", calificaciones)          
# imprime las calificaciones ordenadas de mayor a menor
calificaciones.sort(reverse=True)
print("Calificaciones ordenadas de mayor a menor => ", calificaciones)

print ("\n ----------------------------------------------------------------------- ")
# Imprime las calificaciones que son mayores al promedio
print("Calificaciones mayores al promedio => ", [nota for nota in calificaciones if nota > promedio])

