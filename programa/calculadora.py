# Calculadora básica en Python

print("=== CALCULADORA BÁSICA ===")

# Pedimos los números
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Mostramos opciones
print("\nSelecciona la operación:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Elige una opción (1/2/3/4): ")

# Condicionales
if opcion == "1":
    resultado = num1 + num2
    print("Resultado:", resultado)

elif opcion == "2":
    resultado = num1 - num2
    print("Resultado:", resultado)

elif opcion == "3":
    resultado = num1 * num2
    print("Resultado:", resultado)

elif opcion == "4":
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado:", resultado)
    else:
        print("Error: No se puede dividir entre cero.")

else:
    print("Opción no válida.")