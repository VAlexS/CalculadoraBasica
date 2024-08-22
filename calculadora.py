import math

def sumar(n1, n2):
    op1 = int(n1)
    op2 = int(n2)
    return op1 + op2


def restar(n1, n2):
    op1 = int(n1)
    op2 = int(n2)
    return op1 - op2


def multiplicar(n1, n2):
    op1 = int(n1)
    op2 = int(n2)
    return op1 * op2


def dividir(n1, n2):
    op1 = int(n1)
    op2 = int(n2)
    return op1 / op2


def potencia(base, exponente):
    op1 = int(base)
    op2 = int(exponente)
    return math.pow(op1, op2)


def raiz_cuadrada(numero):
    op = int(numero)
    return math.sqrt(op)


# ingrese lo que ingrese en input, lo toma como un string

while True:
    print("Ingrese una opcion entre las siguientes opciones: \n"
          "1 - Sumar\n"
          "2 - Restar\n"
          "3 - Multiplicar\n"
          "4 - Dividir\n"
          "5 - Potencia\n"
          "6 - Raiz cuadrada")
    try:
        opcion = input("Ingrese una opcion: ")
        op = int(opcion)
        if 1 <= op <= 6:
            break # sale del bucle si el numero es valido
        else:
            print("El numero introducido no esta entre 1 y 6. Inténtelo de nuevo")
    except ValueError:
        print("Eso no es un número valido. Por favor, introduce un número entre 1 y 6.")



if op == 1:
    operando1 = input("Ingrese el primer numero: ")
    operando2 = input("Ingrese el segundo numero: ")
    print(sumar(n1=operando1, n2=operando2))
elif op == 2:
    operando1 = input("Ingrese el primer numero: ")
    operando2 = input("Ingrese el segundo numero: ")
    print(restar(n1=operando1, n2=operando2))
elif op == 3:
    operando1 = input("Ingrese el primer numero: ")
    operando2 = input("Ingrese el segundo numero: ")
    print(multiplicar(n1=operando1, n2=operando2))
elif op == 4:
    operando1 = input("Ingrese el primer numero: ")
    operando2 = input("Ingrese el segundo numero: ")
    print(dividir(n1=operando1, n2=operando2))
elif op == 5:
    operando1 = input("Ingrese el primer numero: ")
    operando2 = input("Ingrese el segundo numero: ")
    print(potencia(base=operando1, exponente=operando2))
elif op == 6:
    operando = input("Introduzca un numero: ")
    print(raiz_cuadrada(numero=operando))





