'''def almacenar_nombres(tamaño):
    """Solicitar nombres al usuario y almacenar sus longitudes"""
    nombres=[]
    longitudes=[]
    
    for i in range(tamaño):
        nombres=input(f"Ingrese el nombre{i+1}:")
        nombres.append(len(nombres))
        longitudes.append(len(longitudes))
    return nombres, longitudes 

while True:
    try: 
        tamaño=int(input("Ingrese el tamaño del arreglo:"))
        if tamaño>0:
            break
        else: 
            print("Por favor, ingrese un numero positivo.")
    except: ValueError
    print("Entrada invalida. Intente de nuevo.")
    
nombres,longitudes=almacenar_nombres(tamaño)
print("Lista de nombres:", nombres)
print("Longitudes de nombres:", longitudes)'''






'''n=int(input("Tamaño array:")) #8
m=int(input("Multiplos")) #5
salida=[] #vector
for i in range(1, n) #[(1, 7)]
salida.append(i*m)
print("Salida") # [1, 5, 10...... 35]'''







'''n = int(input("Ingrese el numero de clientes encuestados:"))
respuestas=[]
print("Ingrese las evaluaciones (1=Malo, 2=Regular, 3=Bueno. 4=Muy bueno, 5=Excelente):")
for i in range (n): 
    while True:
        valor = int(input("Cliente:"))
        if 1 <= valor <= 5:
            respuestas.append(valor)
            break
        else:
            print("Ingrese un numero valido entre 1 y 5")
        
conteo = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
for r in respuestas:
    conteo[r] += 1'''
