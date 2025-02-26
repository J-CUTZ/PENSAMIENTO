def ordenar_numero():    
    numero=input("Ingrese un Número de 5 digitos:")
    
    while(numero.isdigit()and len(numero)==5):
        print("Número no valido, debe ser 5 digitos:")
    numero=input("Ingrese un Número de 5 digitos:")
    
    digitos=(int(d)for and in numero)
    
    ascendente=sorted(digitos)
    descendente=sorted(digitos, reverse=True)
    
    print("El programa muestra en forma ascendente: ")
    print("El programa muestra en forma descendente: ")
    