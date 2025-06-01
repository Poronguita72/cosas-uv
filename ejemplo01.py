
# revisar los digitos de un numero entero
# mostrar cada digito en la consola

def mostrar_digitos(numero_entero: int):
    numero_actual = numero_entero

    while numero_actual > 0:
        # se determina el digito de
        # de la unidad del numero actual
        digito = numero_actual % 10
        print(digito)
        numero_actual = numero_actual // 10


# probar la funcion revisar_digitos()
numero_a_mostrar = None

# ciclo de validación de entrada
entrada_valida = False
while entrada_valida == False:
    try:
        numero = int(input("Ingrese un numero entero positivo: "))
    except:
        print("Ingrese sólo números enteros y positivos")
        continue

    if numero > 0:
        entrada_valida = True
        numero_a_mostrar = numero
    else:
        print("Debe ingresar un número mayor que cero")

# fin del ciclo de validación
# la variable numero_a_mostrar contiene un
# numero entero y positivo para ser utilizado
# en la funcion mostrar_digitos()

mostrar_digitos(numero_a_mostrar)





