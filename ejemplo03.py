21
def suma_digitos(numero_entero: int) -> int:
    numero_actual = numero_entero

    suma_total = 0
    while numero_actual > 0:
        digito = numero_actual % 10
        suma_total = suma_total + digito

        numero_actual = numero_actual // 10

    return suma_total

def validar_numero(numero_entero):
    suma = suma_digitos(numero_entero)

    if suma % 2 == 0:
        return True
    else:
        return False

# Ingresar un numero hasta que
# el numero sea valido
numero_validado = None

dato_valido = False
while dato_valido == False:
    try:
        numero_ingresado = int(input("Ingrese nro: "))
    except:
        print("Ingrese un dato valido")
        continue

    esValido = validar_numero(numero_ingresado)

    if esValido == True:    
        dato_valido = True
        numero_validado = numero_ingresado
    else:
        print("Ingrese un numero valido")
