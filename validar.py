print("asd")
novalido= True 

while novalido:
    try:
        print("ingrese su numero")       
        num= input(int())
        if num > 0:
            novalido= False
        else:
            print("numero fuera de rango permitido")
    except:
        print("error, la entrada no es un numero")
        
ni=0
while num > 0:
    d=num %10
    ni = ni* 10+d
    num= num// 10
    
print("numero invertdo:")        