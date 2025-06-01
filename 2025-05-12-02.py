
def validar_numero() -> int:
    numero_valido = None

    entrada_no_valida = True
    while entrada_no_valida == True:
        dato_ingresado = input("Ingrese un nro mayor que 9: ")
        try:
            numero_ingresado = int(dato_ingresado)
        except:
            print("No puede ingresar un string")
            continue

        if numero_ingresado > 9:
            # el numero es valido
            numero_valido = numero_ingresado
            entrada_no_valida = False
        else:
            print("Debe ingresar un nro mayor que 9")

    return numero_valido


# retorna True si es válido
# retorna False si no es válido
def validar_simetria(nro_a_validar) -> bool:
    numero_actual = nro_a_validar

    primer_digito = None
    ultimo_digito = None

    contador_digito = 0
    while numero_actual > 0:
        digito_actual = numero_actual % 10
        contador_digito = contador_digito + 1

        if contador_digito == 1:
            primer_digito = digito_actual

        numero_actual = numero_actual // 10

    ultimo_digito = digito_actual

    if primer_digito == ultimo_digito:
        return True
    else:
        return False


nro = validar_numero()
es_simetrico = validar_simetria(nro)

if es_simetrico == True:
    print("Es un código simetrico")
else:
    print("No es un código simétrico")
