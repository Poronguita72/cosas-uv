
def validar_numero() -> int:
    numero_valido = None

    entrada_no_valida = True
    while entrada_no_valida == True:
        dato_ingresado = input("Ingrese un nro mayor que cero: ")
        try:
            numero_ingresado = int(dato_ingresado)
        except:
            print("No puede ingresar un string")
            continue

        if numero_ingresado > 0:
            # el numero es valido
            numero_valido = numero_ingresado
            entrada_no_valida = False
        else:
            print("Debe ingresar un nro mayor que cero")

    return numero_valido

def examinar_numero(numero_valido: int) -> int:
    numero_actual = numero_valido

    total_leds = 0
    while numero_actual > 0:
        digito_actual = numero_actual % 10
        leds = cantidad_leds(digito_actual)
        print("Digito actual=", digito_actual, " cantidad de leds=", leds)
        total_leds = total_leds + leds

        numero_actual = numero_actual // 10

    return total_leds

def cantidad_leds(digito: int) -> int:
    cantidad = None

    if digito == 0 or digito == 6 or digito == 9:
        cantidad = 6
    elif digito == 1:
        cantidad = 2
    elif digito == 2 or digito == 3 or digito == 5:
        cantidad = 5
    elif digito == 4:
        cantidad = 4
    elif digito == 7:
        cantidad = 3
    elif digito == 8:
        cantidad = 7

    return cantidad

nro = validar_numero()
total_leds_usados = examinar_numero(nro)
print(f"El nro {nro} utliza {total_leds_usados}")

