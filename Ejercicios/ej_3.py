# Ejercicio de Bucles en Python
# Enunciado ==> Muestre la tabla de multiplicar de un número ingresado por el usuario Usando "FOR"
numero = int (input ("(FOR) Ingrese el número a multiplicar Estimado Usuario: "))
for i in range (1,11):
    print (f"Numero {numero} x {i} = ", numero * i)
print("\n")

# Enunciado ==> Muestre la tabla de multiplicar de un número ingresado por el usuario Usando "WHILE"
numero = int (input ("(WHILE) Ingrese el número a multiplicar Estimado Usuario: ")) 
i = 1
while i <= 10:
    print (f"Numero {numero} x {i} = ", numero * i)
    i += 1
print("\n")

# Enunciado ==> Muestre la tabla de multiplicar de un número ingresado por el usuario Usando "Do WHILE"
numero = int (input ("(DO WHILE) Ingrese el número a multiplicar Estimado Usuario: ")) 
i = 1
while True:
    print (f"Numero {numero} x {i} = ", numero * i)
    i += 1
    if i > 10:
        break
print("\n")