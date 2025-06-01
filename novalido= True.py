def verificarnum():
    noValido= True 
    while noValido:
        try:
            print("ingrese un numero")
            num=int(input())
            if num >0:
                noValido = False
            else:
                print("ingrese un numero valido")
        except:
            print("error, ingrese un numero")
    return num


def registrodeasistencia(): 
    suma = sum(int(d) for d in numero)
    longitud = len(num) 
    if suma % longitud == 0:
     print(" Código válido")
    else:
     print("Código inválido")

numero: int     
numero = verificarnum()
registrodeasistencia(numero)