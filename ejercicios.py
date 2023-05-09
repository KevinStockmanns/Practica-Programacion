# EJERCICIO 1
# Suma de enteros del 1 al N
def suma_enteros(ent):
    if not isinstance(ent, int):
        raise 'El numero ingresado debe ser un número entero'
    
    sum = 0
    for i in range(1, ent + 1):
        sum = sum + i
    print(sum)

# suma_enteros(100)

# EJERCICIO 2
# Escribir un programa que lea un número entero y determine si es par o impar.
def es_par(num):
    if not isinstance(num, int):
        return 'No es un numero entero'
    
    if num % 2 != 0:
        print(f'El numero {num} NO es primo')
    else:
        print(f'El numero {num} ES primo')


# es_par(-56)

# EJERCICIO 3
# Escribir un programa que lea una cadena de texto y determine si es un palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a izquierda).
def palindromo(word):
    if not isinstance(word, str):
        raise 'El valor ingresado no es un string'
    
    if word.lower() == word[::-1].lower():
        print(f'La palabra "{word}" SI es palindromo')
    else:
        print(f'La palabra "{word}" NO es palindromo')


# palindromo('ana')


# EJERCICIO 4
# Escribir un programa que lea una lista de números y devuelva el valor mínimo y máximo de la lista.
def max_min(nums):
    if not isinstance(nums, list) or not nums:
        raise 'La lista ingresada no es valida'
    
    max = nums[0]
    min = nums[0]

    for i in nums:
        try:
            i = float(i)
        except:
            raise 'Los elementos de la lista deben ser numeros'
        if i > max:
            max = i
        elif i < min:
            min = i
    
    print(f'El número menor es {min} y el mayor es {max}')
    
# max_min([1, 2, 4, -10])

# EJERCICIO 5
# Escribir un programa que lea un número entero y devuelva una lista con los primeros n números de la serie de Fibonacci.
def fibonacci(num):
    if not isinstance(num, int):
        raise 'Debe ingresar un numero.'
    
    a, b = 1, 2
    lista = []
    for i in range(num):
        lista.append(a)
        a, b = b, a + b
    
    print(lista)
    
fibonacci(10)