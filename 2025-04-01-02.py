def sonidoAnimal(animal):
    sonido = "no se el sonido del animal"
    if animal == "perro":
        sonido = "guau"
        return sonido
    
    if animal == "gato":
        sonido = "miau"
        return sonido

    if animal == "gusano":
        sonido = "dfsfsfsdfsf"
        return sonido

    

print(sonidoAnimal("perro"))
print(sonidoAnimal("gato"))
print(sonidoAnimal("gusano"))