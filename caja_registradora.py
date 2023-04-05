class CajaRegistradora:
    def __init__(self):
        self.subtotal = 0
        self.total_itbis = 0
        self.comprobante_fiscal = False
        self.rnc = None
    
    def agregar_producto(self, precio):
        try:
            precio_sin_itbis = float(precio)
            itbis = precio_sin_itbis * 0.18
            self.subtotal += precio_sin_itbis
            self.total_itbis += itbis
            print("Enviando el producto...")
            print("Producto agregado. Subtotal:", self.subtotal, "ITBIS:", self.total_itbis)
        except ValueError:
            print("Error: el precio debe ser un número.")
    
    def imprimir_total(self):
        total = self.subtotal + self.total_itbis
        print("Subtotal:", self.subtotal)
        print("ITBIS:", self.total_itbis)
        print("Total:", total)
        if self.comprobante_fiscal and self.rnc:
            print("Comprobante fiscal generado con RNC:", self.rnc)


def programa_principal():
    caja = CajaRegistradora()
    
    comprobante = input("¿Desea generar un comprobante fiscal? (S/N): ")
    if comprobante.upper() == "S":
        caja.comprobante_fiscal = True
    
    if caja.comprobante_fiscal:
        rnc = input("Por favor, ingrese su RNC de 10 dígitos: ")
        if len(rnc) == 10 and rnc.isdigit():
            caja.rnc = rnc
            print("RNC registrado correctamente.") 
        else:
            print("Error: el RNC debe ser un número de 10 dígitos.")
            return
    
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

if __name__ == "__main__":
    programa_principal() 



#                 (DIAGRAMA DE FLUJO)

 #           Inicio
 #           |
 #           Crear objeto CajaRegistradora
 #           |
 #           Preguntar si se desea generar un comprobante fiscal
 #           |
 #           Si se desea generar un comprobante fiscal
 #           |   Pedir RNC
 #           |   Si el RNC es válido, registrarlo
 #           |   Si el RNC no es válido, mostrar mensaje de error y terminar programa
 #           |
 #           Mientras el usuario no seleccione "Salir"
 #           |   Preguntar al usuario qué acción desea realizar
 #           |   Si se selecciona "Agregar producto"
 #           |   |   Pedir el precio del producto
 #           |   |   Si el precio es un número, agregar el producto
 #           |   |   Si el precio no es un número, mostrar mensaje de error
 #           |   Si se selecciona "Imprimir total", imprimir el subtotal, ITBIS y total
 #           |   Si se selecciona "Salir", terminar programa
 #           |   Si se selecciona una opción inválida, mostrar mensaje de error
 #           |
 #           Fin 


#                   (DIAGRAMA CASO DE USO) 

#                          Usuario
#                            |
#                            v
#                     Iniciar programa
#                            |
#                            v
#           Crear instancia de CajaRegistradora
#                            |
#                            v
#       Preguntar si desea generar comprobante fiscal
#                            |
#          +-----------------+-----------------+
#          |                                     |
#          v                                     v
#       Sí desea                             No desea
#  generar comprobante                  generar comprobante
#          |                                     |
#          v                                     v
#  Ingresar RNC válido                    No ingresar RNC
#          |                                     |
#          v                                     v
#   +------+-------+                    +--------+-------+
#   |              |                    |                |
#   v              v                    v                v
#Agregar        Imprimir           Terminar        Opción
#producto         total             programa       inválida
#   |              |                  |                |
#   v              v                  v                v
#Ingresar      Mostrar total         Fin          Mostrar error
#precio           CajaRegistradora               y volver a menú
#   |
#   v
# Mostrar mensaje de
#  error si precio
#   es inválido
