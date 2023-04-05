def programa_principal():
    caja = CajaRegistradora()
    
    comprobante = input("¿Desea generar un comprobante fiscal? (S/N): ")
    if comprobante.upper() == "S":
        caja.comprobante_fiscal = True
    
    if caja.comprobante_fiscal:
        while True:
            rnc = input("Por favor, ingrese su RNC de 10 dígitos: ")
            if len(rnc) == 10 and rnc.isdigit():
                caja.rnc = rnc
                print("RNC registrado correctamente.")
                break
            else:
                print("Error: el RNC debe ser un número de 10 dígitos.")
    
    while True:
        opcion = input("¿Qué desea hacer? (1) Agregar producto, (2) Imprimir total, (3) Salir: ")
        
        if opcion == "1":
            precio = input("Ingrese el precio del producto: ")
            caja.agregar_producto(precio)
        
        elif opcion == "2":
            caja.imprimir_total()
        
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción inválida. Intente de nuevo.")
