# Solicitar un número al usuario
numero = int(input("Ingresa un número"))

# Mostrar la tabla de multiplicar
print(f"tabla de multiplicar del {numero}:")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")