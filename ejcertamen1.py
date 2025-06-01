#parte 1 funciona
def suma_digitos(numero_entero: int)->int:
    numero_actual = numero_entero

    suma_total = 0
    while numero_actual > 0:
        digito = numero_actual % 10
        suma_total = suma_total + digito

        numero_actual = suma_total // 10

    return suma_total


def validacion_numerica(numero_entero):
    suma = suma_digitos(numero_entero)

    if suma % 2 == 0:
        return True
    else:
        return False

numero_validado = None
dato_valido = False
while dato_valido == False:

    numero_ingresado = int(input("ingrese un numero:"))


    es_valido = validacion_numerica(numero_ingresado)

    if es_valido == True:
        dato_valido = True
        numero_validado = numero_ingresado
    else:
        print("ingrese un numero valido")





