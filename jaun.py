
while True:
    print("este es el menu para hacer figuras geometricas")
    print("1.circulo")
    print("2.cuadrado")
    print("3.triangulo")
    print("4.salir")
    opcion=int(input("seleccione una figura \n"))
    if opcion == 1:
        radio = float(input("ingrese el radio del circulo"))
        area = 3.1416 * radio * radio
        print("el area del circulo es:",area)
    elif opcion == 2:
        lado = float(input("ingrese el lado del cuadrado"))
        area = lado * lado
        print("el area del cuadrado es:",area)
    elif opcion == 3:
        base = float(input("ingrese la base del triangulo"))
        area = (base * altura) / 2
        print("el area del triangulo es:",area)
    elif opcion == 4:
        break


 # cerrar 