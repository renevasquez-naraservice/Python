#Ejercicio => Menú interactivo simple
saldo = 100
print ("Saldo => ",saldo)
while saldo >0:
    print("------------------------------------------------------------------------------")
    print("Qué deseas hacer con tu dinero?")
    print("1.- Depositar")
    print("2.- Retirar")
    print("3.- Salir")
    accion = int(input("Selecciona una opción: "))
    if accion == 1:
        monto = int(input("¿Qué monto desea depositar? => "))
        saldo += monto
    elif accion == 2:
        monto = int(input("¿Qué monto desea retirar? => "))
        saldo -= monto
    elif accion == 3:
        print("------------------------------------------------------------------------------")
        print (f"Se retira con un saldo Actual de ==> {saldo}")
        break
    else: 
        print("Opción inválida vuelva a intentar")
    print("------------------------------------------------------------------------------")
    print (f"Su saldo Actual es ==> {saldo}")