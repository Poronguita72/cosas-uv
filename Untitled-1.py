codigo = input("Ingresa el código de asistencia: ")

suma = sum(int(d) for d in codigo)
longitud = len(codigo)

if suma % longitud == 0:
    print(" Código válido")
else:
    print("Código inválido")