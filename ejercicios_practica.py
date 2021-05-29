#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"

condicion = False


def ej1():
    # Ejercicios con bucles "while"

    
    # Dado el siguiente "while", complete la condicion
    # para que el "while" itere siempre que <x sea menor a 6>
    # Además, complete la línea de código necesaria para que
    # el valor de "x" incremente "1" en cada iteración
    # reemplace "condicion" por lo que crea necesario
    # Coloque la línea de código para que "X" incremente "1"

    x = 0

    while x < 6:
        x += 1    
        print("Valor de x =", x)
        

    # Dado el siguiente "while", complete la condicion
    # para que el "while" itere siempre que <x sea mayor o igual a 0>
    # Además, complete la línea de código necesaria para que
    # el valor de "x" decremente "1" en cada iteración
    # reemplace "condicion" por lo que crea necesario
    # Coloque la línea de código para que "X" decremente "1"

    x = 5

    while x >= 0: 
        x -= 1   
        print("Valor de x =", x)
        


def ej2():
    # Ejemplos con bucles "for"

    # Dado la siguiente lista de colores, utilizar "for"
    # para imprimir en pantalla todos los colores
    # Itere el "for" utilizando la lista como parámero
    # y utilizar como elemento del "for" cada color
    # for color ...
    # Itere el "for" utilizando el tamaño de la lista
    # como parámetro y utilizar el índice para acceder a
    # los elementos de la lista
    # for i ...

    colores = ['rojo', 'naranja', 'verde', 'azul']
    for i in colores:
        print(i)
    # Acá te faltó armar el otro for con el índice, así: 
    # for i in range(len(colores)):
    


def ej3():
    # Ejemplos con bucles "for"
    # Dado la siguiente lista de números, utilizar "for"
    # para recorrer toda la lista y realizar la sumatoria de todos los números
    # La sumatoria se deberá ir guardando en la variable "suma"
    # Variable ya inicializada, la suma arranca en cero
    numeros = ([1, 5, -1, 6, 10, 2, -5])
    suma = 0
    for numero in [1, 5, -1, 6, 10, 2, -5]:
        suma= suma + numero
        print(suma)  
    

def ej4():
    # Ejercicios con bucles "while"

    
    # Realizar un bucle "while" cuya condición de continuidad
    # sea que <x sea menor a 10> y que <x sea distinto de 6>
    # Colocar ambas condiciones como condicion del "while" realizando
    # una condición compuesta (utilice el operador "and" o "or" según corresponda)
    # En cada iteracion del bucle debe incrementar el valor de "x" en "2"
    # e imprimir en pantalla el resultado de X (antes de incrementar) con print
    # Realice el mismo bucle "while" pero en vez de estar formado por una condición
    # compuesta, que el "while" siga iterando mientras <x sea menos a 10>, y dentro del
    # "while" consultar si <x es igual a 6>, y en ese caso realizar una interrupción del bucle
    # En cada iteracion del bucle debe incrementar el valor de "x" en "2"
    # e imprimir en pantalla el resultado de X (antes de incrementar) con print

    x = 0
    while x < 10 and x != 6:
        x += 2    
        print("Valor de x =", x)

    

    x = 0
    while x < 10:
        if x == 6:
            break
        print(x)
        x += 2

        
        
            
            



        
        
            
            

            
            
            


        
            
            
            





def ej5():
    # Ejercicio de secuencias numéricas
    # Pedir por consola dos números que representen el principio y fin de una
    # secuencia numérica.
    # Realizar un bucle "for" que recorra esa secuencia armada con "range"
    # y calcule a sumatoria total de todos los números dentro de esa secuencia
    # Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    # sino que va hasta el anterior
    # fin....
    # for ... in range(....)
    # Imprimir el valor de la sumatoria
    inicio = int(input('Ingrese el primer número de la secuencia\n'))
    fin = int(input('ingrese numero mayor o igual al anterior\n'))

    for numbers in range(inicio, fin): # <--  Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
           # sino que va hasta el anterior! for numbers in range(inicio,fin+1)
           lista1 = [ [inicio, fin] ]
           nume=0
           for i in lista1:
               for m in i:
                   nume += m
               
               print('resultado',nume)    

def ej6():
    # Ejercicio de secuencias numéricas
    # Pedir por consola dos números que representen el principio y fin de una
    # secuencia numérica.
    # Realizar un bucle "for" que recorra esa secuencia armada con "range"
    # y cuante cuantes números son negativos y cuantos números son mayor o igual a cero
    # Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    # sino que va hasta el anterior

    inicio = int(input('Ingrese el primero número de la secuencia\n'))
    fin = int(input('ingrese numero mayor o igual al anterior\n'))
    n = list(range(inicio,fin))
    list(range(len(n)))
    cantidad = list(range(len(n)))
    total = len(cantidad)
    if total > 0:
        positivos = 0
        negativos = 0
        nulos = 0
        for numero in n: # <-- Ojo que acá estás haciendo un for sobre el contenido de "n" y "n" es una lista que contiene un rango! (linea 179)
            if numero > 0:
                positivos = numero
                print(positivos)
            elif numero < 0:
                negativos = numero
                print(negativos)
            else:
                nulos = numero
                print(nulos)
    print(numero)
    
    # Revisa la lógica de este punto :D
    
        
    


    

    

        
    

    cantidad_numeros_positivos = 0  # Inicializo el contador en 0
    #cantidad_numeros_negativos

    # for ... in range(....)

    # Imprimir el valor de la cantidad de números positivos y negativos


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
    #ej6()
