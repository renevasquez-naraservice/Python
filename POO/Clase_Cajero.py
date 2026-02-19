# Ejercicio de POO con Python
# Cajero automático

# ideas:
# El saldo no será una variable suelta ❌
# Será un atributo de una clase ✅
# El menú será un método
# Las acciones serán métodos

class Cajero:
    def __init__(self,usuario,saldo_inicial):
        self.nombre = usuario
        self.saldo = saldo_inicial
    
    #Definimos los métodos
    def ver_saldo(self):
        return (print (f"Su saldo actual {self.nombre} es => ",self.saldo))
    
    def depositar(self):
        monto= float(input("Cuánto desea depositar?: "))
        self.saldo +=monto
        print("Depósito realizado con Éxito.!")

    def retirar(self):
        monto= float(input("Cuánto desea retirar?: "))
        if monto <= self.saldo:
            self.saldo -=monto
            print("Retiro realizado con Éxito.!")
        else:
            print("FONDOS INSUFICIENTES :(")

    def mostrar_menu(self):
        print("\n1.- Ver saldo")
        print("2.- Depositar")
        print("3.- Retirar")
        print("4.- Salir")

    def iniciar(self):
        while True:
            self.mostrar_menu()
            opcion = int(input("Elige una opción => "))
            if opcion == 1 :
                self.ver_saldo()
            elif opcion == 2:
                self.depositar()
            elif opcion == 3:
                self.retirar()
            elif opcion == 4:
                break
            else:
                print("Opción inválida")

#Programa Cajero 
mi_cajero = Cajero("Jhon", 2000)    
mi_cajero.iniciar()   