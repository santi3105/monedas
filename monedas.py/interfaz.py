def menu():
    """
    muestra el menu de las monedas 
    """
    print("\n Bienvenido a la calculadora de monedas a dolares y euros")
    print("1)Pesos colombianos")
    print("2)Bolivares")
    print("3)pesos mexicanos")
    print("4)salir")
    op = int(input("digite una opcion del menu: "))
    return op

def opcion_seleccionada(op):
    """
    mostrar la opcion seleccionada
    """
    pesoscol= 1
    bolivares =2
    pesosmex=3
    salir=4
    if op == 1:
        print(f"usted selecciono la opcion cuadrado")
        return pesoscol
    elif op == 2:
        print(f"usted selecciono la opcion triangulo")
        return bolivares
    elif op == 3:
        print(f"usted selecciono la opcion circulo")
        return pesosmex
    elif op == 4:
        print(f"usted selecciono la opcion rectangulo")
        return salir
    else:
        return"opcin no valida!!!"