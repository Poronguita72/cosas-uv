
def resistenciaEquivalente(resistencia1, resistencia2):

    numerador = resistencia1 * resistencia2
    denominador = resistencia1 + resistencia2

    rEquivalente = numerador / denominador

    return rEquivalente

resistencia1 = 20
resistencia2 = 30
resistencia3 = 40
resistencia4 = 50

rEquivalente1     = resistenciaEquivalente(resistencia1, resistencia2)
rEquivalente2     = resistenciaEquivalente(rEquivalente1, resistencia3)
rEquivalenteTotal = resistenciaEquivalente(rEquivalente2, resistencia4)

print("La resistencia equivalente es:", rEquivalenteTotal)

print("La resistencia equivalente entre 20 y 70 es:", resistenciaEquivalente(20,70))
