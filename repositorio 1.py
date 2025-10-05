import math

def menu():
    print("\n=== Calculadora Científica ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Seno")
    print("6. Coseno")
    print("7. Tangente")
    print("8. Potencia")
    print("9. Raíz cuadrada")
    print("0. Salir")

def main():
    while True:
        menu()
        opcion = input("Elige una opción: ")

        if opcion == "0":
            print("Saliendo...")
            break
        elif opcion in ["1","2","3","4","8"]:
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))

        if opcion == "1":
            print("Resultado:", a+b)
        elif opcion == "2":
            print("Resultado:", a-b)
        elif opcion == "3":
            print("Resultado:", a*b)
        elif opcion == "4":
            print("Resultado:", a/b if b != 0 else "Error: división por cero")
        elif opcion == "5":
            ang = float(input("Ingresa ángulo en grados: "))
            print("Resultado:", math.sin(math.radians(ang)))
        elif opcion == "6":
            ang = float(input("Ingresa ángulo en grados: "))
            print("Resultado:", math.cos(math.radians(ang)))
        elif opcion == "7":
            ang = float(input("Ingresa ángulo en grados: "))
            print("Resultado:", math.tan(math.radians(ang)))
        elif opcion == "8":
            print("Resultado:", math.pow(a,b))
        elif opcion == "9":
            n = float(input("Ingresa un número: "))
            print("Resultado:", math.sqrt(n))
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()