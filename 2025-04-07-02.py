
def interes_simple(capital: int, tasa: float, tiempo: int) -> float:
    interes_generado: float

    interes_generado = capital * tasa * tiempo

    return interes_generado


######################################################
# Ejemplo de uso: 
# Un capital de $2000 a una tasa anual del 3% (0.03) 
# durante 4 años generará un interés de $240.
#
interes_calculado = interes_simple(2000, 0.03, 4)
print("El interes generado es:", interes_calculado)


#####################
# Otro ejemplo de uso
#
capital = int(input("Ingrese capital:"))
interes = float(input("Ingrese interes:"))
tiempo  = int(input("Ingrese cantidad de años:"))

interes_calculado = interes_simple(capital, interes, tiempo)
print("El interes generado es:", interes_calculado)