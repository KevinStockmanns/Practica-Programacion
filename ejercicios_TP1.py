# EJERCICIO 1
# Escriba un diagrama de flujo que permita generar los primeros 50 números pares.
def ejercicio1():
    c, p = 0, 0

    while c < 50:
        c, p = c + 1, p + 2

# ejercicio1()

# EJERCICIO 2
# Modifique el diagrama anterior de manera que calcule y muestre la suma total de los 50 nros. pares.
def ejercicio2():
    c, p, s = 0, 0, 0

    while c < 50:
        c, p , s = c + 1, p + 2, s + p
    
    print(s)
# ejercicio2()

# EJERCICIO 3
# Escriba un diagrama de flujo que permita hallar e imprimir el cuadrado de 40 números ingresados por teclado
def ejercicio3():
    c, n = 0, 0

    while c < 40:
        c = c + 1    # c += 1  (esto es lo mismo?)
        n = float(input('Ingrese un número:'))
        n = n * n
        print(n)

# ejercicio3()


# EJERCICIO 4
# Escriba un diagrama de flujo que permita Generar e imprimir los primeros N números, siendo N un número ingresado por teclado
def ejercicio4():
    num, n = 0, 0
    n = float(input('Ingrese un numero:'))
    while num < n:
        num = num + 1
        print(num)

# ejercicio4()



# EJERCICIO 5
# Escriba un diagrama de flujo que permita Generar y mostrar los primeros 50 números pares comenzando con el número 23.
def ejercicio5():
    c, p = 0, 23
    p = p + 1
    while c<50:
        c = c + 1
        print(p)
        p = p + 2

# ejercicio5()


# EJERCICIO 6
# Imprimir la tabla de multiplicar de un número ingresado por teclado
def ejercicio6():
    C, P , T = 1, 23, 0

    N, T = int(input('Ingrese el numero:')), int(input('Ingrese la tabla:'))
    
    while C <= T:
        print(f'{N} x {C} = {N * C}')
        C = C + 1

# ejercicio6()

# EJERCICIO 7
# Imprimir los números primos (divisibles solo por sí mismos) que hay entre 12 y 45
def ejercicio7():
    n = 12

    while n < 45:
        n = n + 1

        if n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
            print(n)

# ejercicio7()


# EJERCICIO 8
# Escriba un diagrama de flujo que permita Generar e imprimir los primeros 5 múltiples de 3, a partir del número 14
def ejercicio8():
    n, m = 14, 0

    def repeat():
        if n % 3 == 0:
            print(n)
            n = n + 3
            m = m + 1
        else:
            n = n + 1
    
    repeat()

    while m != 0:
        repeat()

ejercicio8()