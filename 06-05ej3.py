continuar = True
suma_acumulada = 0

while continuar:
    entrada_datos = input("ingrese un número(q para mostrar y salir): ")
    
    if entrada_datos == "q":
        continuar = False
    else:
        try:
            numero_a_sumar = int(entrada_datos)
            suma_acumulada = suma_acumulada + numero_a_sumar
        except:
            print("entrada no valida")
print(f"la suma es {suma_acumulada}")