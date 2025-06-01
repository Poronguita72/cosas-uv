
def calcular_imc(peso: float, altura: float, decimales: int) -> float:
    IMC: float

    IMC = peso / (altura * altura)

    IMC = round(IMC, decimales)

    return IMC

IMC = calcular_imc(70, 1.75, 3)
print(IMC)

