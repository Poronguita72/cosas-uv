
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

# Esta funcion solicita y retorna un
# número entero y positivo desde el teclado
def ingresar_numero_entero_positivo() -> int:
    numero_a_retornar = None

    entrada_valida = False
    while entrada_valida == False:
        try:
            numero = int(input("Ingrese un numero entero positivo: "))
        except:
            print("Ingrese sólo números enteros y positivos")
            continue

        if numero > 0:
            entrada_valida = True
            numero_a_retornar = numero
        else:
            print("Debe ingresar un número mayor que cero")

    return numero_a_retornar

# probar la funcion revisar_digitos()
numero_a_mostrar = None

numero_a_mostrar = ingresar_numero_entero_positivo()

mostrar_digitos(numero_a_mostrar)





