def ingresar_codigo_valido() ->int:
    
    numero_valido = None
    ingresar_codigo_valido = False
 
    while ingresar_codigo_valido == False:
        
        dato_ingresado = input("ingrese un codigo (numero entero mayor a 0)" )
 
        try:
            numero = int(dato_ingresado)
        except:
            print("no puede ingresar un texto como entrada")
            
            
            if 13 < numero < 37: 
                ingresar_codigo_valido = True
                numero_valido = numero
            else:
                ingresar_codigo_valido = False
                
    return numero_valido


numero_valido = ingresar_codigo_valido
print(numero_valido)

