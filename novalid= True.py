novalid= True
while novalid:
    try:
        print("ingrese un numero")
        num= int(input())
        if num >=1 and num <=9:
           novalid= False
    else:
         print("error")
except:
    print ("el numero es", num )