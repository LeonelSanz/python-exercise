# Tabla de multiplicar donde pasaremos el numero de la tabla por teclado
def tabla_multiplicar(tabla, limite):
    for i in range(1, limite):
        resultado = tabla * i
        print(f"{tabla} x {i} = {resultado}")

tabla = int(input("Que tabla de multiplicar quieres saber? "))

tabla_multiplicar(tabla,11)