print("===================================")
print("   BIENVENIDO AL SISTEMA DE VENTAS  ")
print("===================================")

productos = []
precios = []
total = 0
opcion = 0

while opcion != 3:
    print("\nMENÚ PRINCIPAL")
    print("1. Añadir nuevo producto")
    print("2. Consultar registros")
    print("3. Finalizar venta")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        # Ciclo para registrar uno o varios productos
        while True:
            nombre = input("\nIngrese el nombre del producto: ")

            # Se valida que el precio ingresado sea un número correcto
            precio_valido = False
            while not precio_valido:
                try:
                    precio = float(input("Ingrese el precio del producto: "))
                    if precio > 0:
                        precio_valido = True
                    else:
                        print("Por favor coloque valores correctos")
                except:
                    print("Por favor coloque valores correctos")

            productos.append(nombre)
            precios.append(precio)
            total = total + precio
            print("Producto registrado.")

            continuar = input("¿Desea agregar otro producto? (s/n): ")
            if continuar != "s":
                break

    elif opcion == 2:
        if len(productos) == 0:
            print("\nNo hay productos registrados.")
        else:
            print("\nPRODUCTOS REGISTRADOS")
            i = 0
            # Ciclo para mostrar los productos registrados
            while i < len(productos):
                print(productos[i], "- $", precios[i])
                i = i + 1

            print("Total acumulado: $", total)

    elif opcion == 3:
        print("\nFinalizando venta...")

    else:
        print("Opción no válida.")

print("\n===== RESUMEN FINAL =====")

if len(productos) == 0:
    print("No se registraron productos.")
else:
    i = 0
    while i < len(productos):
        print(productos[i], "- $", precios[i])
        i = i + 1

    print("TOTAL A PAGAR: $", total)

print("Gracias por usar el sistema.")
