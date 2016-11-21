print("Perimetro y area de las figuras geometricas")
print ("\n")
n=int(input("Ingrese el numero de lados de una figura geometrica: "))

def triangulo():
    print ("El numero de lados pertenece a un triangulo")
    print ("\n")
    print ("Perimetro del triangulo")
    l=int(input("Ingrese el valor del lado del triangulo: "))
    perimetro=l*3
    print ("Perimetro igual a: ", perimetro)
    print ("\n")
    print ("Area del triangulo")
    b=int(input("Ingrese la base del triangulo: "))
    h=int(input("Ingrese la altura del triangulo: "))
    area=(b*h)/2
    print ("Area igual a: ", area)

def cuadrado():
    print ("El numero de lados pertenece a un cuadrado")
    print ("\n")
    print ("Perimetro del cuadrado")
    l=int(input("Ingrese el valor del lado del cuadrado: "))
    perimetro=l*4
    print ("Perimetro igual a: ", perimetro)
    print ("\n")
    print ("Area del cuadrado")
    area=l**2
    print ("Area igual a: ", area)

def pentagono():
    print ("El numero de lados pertenece a un pentagono")
    print ("\n")
    print ("Perimetro del pentagono")
    l=int(input("Ingrese el valor del lado del pentagono: "))
    perimetro=l*5
    print ("Perimetro igual a: ", perimetro)
    print ("\n")
    print ("Area del pentagono")
    ap=int(input("Ingrese el valor del apotema del pentagono: "))
    area=(5*l*ap)/2
    print ("Area igual a: ", area)
    

def figuras ():
    if (n==3):
        triangulo()
    elif (n==4):
        cuadrado()
    elif (n==5):
        pentagono()
        


figuras()
