"""
===================================================
             CALCULADORA SIMPLE - MENÚ
===================================================

Este programa es una calculadora con un menú interactivo que permite
realizar operaciones básicas como suma, resta, multiplicación y división.

Autor: Mateo Lastra

Fecha: 2025-08-13
"""
# Crear un bucle infinito para mostrar el menú hasta que el usuario decida salir
while True:
    print("\n=== MENÚ DE LA CALCULADORA ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    # Solicitar al usuario que elija una opción del menú
    opcion = input("Seleccione una opción (1-5): ")

    # ==============OPERACIONES===============
    
    # Manejar las opciones del menú con un solo bloque if/elif/else
    if opcion == '1':
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")
    
    elif opcion == '2':
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}")

    elif opcion == '3':
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        resultado = num1 * num2
        print(f"El resultado de la multiplicación es: {resultado}")

    elif opcion == '4':
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        # Manejo de la división por cero para evitar errores
        if num2 == 0:
            print("Error: No se puede dividir por cero.")
        else:
            resultado = num1 / num2
            print(f"El resultado de la división es: {resultado}")

    elif opcion == '5':
        print("Saliendo del programa. ¡Hasta luego!")
        break
    
    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 5.")
    
    # Se agrega una pausa para que el usuario pueda ver el resultado antes de continuar,
    # solo si la opción no es salir.
    if opcion != '5':
        input("Presione Enter para continuar...")