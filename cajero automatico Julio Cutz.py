def cajero_automatico():
    saldo = 3000
    intentos = 3
    
    while True:
        print(f"\nSaldo actual: Q{saldo}")
        
        try:
            monto = int(input("Ingrese monto a retirar: "))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")
            continue
        
        if monto < 0:
            print("No se pueden ingresar montos negativos. Intente de nuevo.")
            continue
        
        if monto == 0:
            print("Gracias por usar el cajero. Adiós.")
            break
        
        if monto > saldo:
            intentos -= 1
            print(f"Saldo insuficiente. Intentos restantes: {intentos}")
            if intentos == 0:
                print("Ha superado el número de intentos. Adiós.")
                break
        else:
            saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: Q{saldo}")
            
            if saldo == 0:
                print("Saldo agotado. Adiós.")
                break

if __name__ == "__main__":
    cajero_automatico()