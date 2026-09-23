# Examen práctico - Sistema de pedidos del kiosco
# Nombre y apellido:
# Curso:
#
# IMPORTANTE:
# Resolver el programa siguiendo las etapas indicadas en el README.md.
# Realizar los commits y push cuando se indique.



# =========================
# ETAPA 1 - INICIO
# =========================

Nombre = (input("Ingrese su nombre: "))
saldo = (input("Ingrese su saldo: "))
print(f"hola {Nombre} su saldo es {saldo} ")
productos = ["agua: 100", "pan:500", "manzanas: 300", "tostados: 1000"]
print(f"los productos son: {productos}")

# =========================
# ETAPA 2 - COMPRAS
# =========================
valor1 = float(input("Ingrese el valor de tus compras: "))
resta = float(saldo) - valor1
print(f"La resta de {saldo} y {valor1} es: {resta}")
if resta < 0:
    print("No tiene suficiente saldo para realizar esta compra.")

else:
    print("Compra realizada con éxito.")
while resta >= 0:
    valor2 = float(input("Ingrese el valor de tus compras: "))
    resta = resta - valor2
    print(f"La resta de {saldo} y {valor1} y {valor2} es: {resta}")
    if resta < 0:
        print("No tiene suficiente saldo para realizar esta compra.")
        break
    else:
        print("Compra realizada con éxito.")
# =========================
# ETAPA 3 - CICLO PRINCIPAL
# =========================

# Modificar el programa para que continúe funcionando
# hasta que el usuario decida finalizar la compra.


# =========================
# ETAPA 4 - PEDIDO Y RESUMEN
# =========================

# Mostrar el estado actual del pedido.
# Recorrer las listas con un for para mostrar productos y precios.
