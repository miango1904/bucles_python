#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

# Variable global utilizada para el ejercicio de nota
notas = [70, 82, -1, 65, 55, 67, 87, 92, -1]


# Variable global utilizada para el ejercicio de temperaturas
temp_dataloger = [12.8, 18.6, 14.5, 20.8, 12.1, 21.2, 13.5, 18.6,
                  14.7, 19.6, 11.2, 18.4]


def ej1():
    print('Comenzamos a ponernos serios!')

    '''
    Realice un programa que pida por consola dos números que representen
    el principio y fin de una secuencia numérica.
    Realizar un bucle "for" que recorra esa secuencia armada con "range"
    y cuente cuantos números ingresados hay, y la sumatoria de todos los números
    Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    sino que va hasta el anterior
    '''

    # inicio = ....
    # fin = ....
    # cantidad_numeros ....
    # sumatoria ....
    # bucle.....
    # Al terminar el bucle calcular el promedio como:
    # promedio = sumatoria / cantidad_numeros
    # Imprimir resultado en pantalla
    inicio = int(input('Ingrese el primer número de la secuencia\n'))
    fin = int(input('ingrese numero mayor o igual al anterior\n'))
    lista_1 = list(range(inicio,fin))
    list(range(len(lista_1)))
    cantidad = list(range(len(lista_1)))
    tot_elem = 0
    for n in lista_1:
        tot_elem += 1
    print ('numeros ingresados :', tot_elem)

    for numbers in range(inicio, fin):
        lista1 = [ [inicio, fin] ]
        cantidad = list(range(len(lista_1)))
        total = len(cantidad)
        nume=0
        for i in lista1:
            for m in i:
                nume += m
    print('suma de numeros :',nume)
    promedio = nume/tot_elem
    print('el promedio es :',promedio)
               
            




def ej2():
    print("Mi Calculadora (^_^)")

    '''
    Realice una calculadora:
    Dentro de un bucle se debe ingresar por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar:
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)
    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    El programa se debe repetir dentro del bucle hasta que como operador
    se ingrese la palabra "FIN", en ese momento debe terminar el programa
    Se debe debe imprimir un cartel de error si el operador ingresado no es
     '''
    s = int(input('ingrese primer valor\n'))
    e = int(input('ingrese segundo valor\n'))
    print('ingrese el numero equivalente al simbolo de operacion deseada')
    
    

    Suma = (s + e)
    Resta = (s - e)
    Multiplicación = (s * e)
    División = (s/e)
    Potencia = (s**e)
    

    
    
    while True: 
        
            op = input('1-suma\n 2-Resta\n 3-multiplicar\n 4-dividir\n 5-potencia\n FIN\n')
        
            if op == '1':
                print(Suma)
                break
            elif op == '2':
                print(Resta)
                break
            elif op == '3':
                print(Multiplicación)
                break
            elif op == '4':   
                print(División)
                break
            elif op== 'FIN':
                break
            else:
                print('numero erroneo')
            
        
            




def ej3():
    print("Mi organizador académico (#_#)")

    '''
    Tome el ejercicio de "calificaciones":
    <condicionales_python / ejercicios_practica / ej3>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Las notas del estudinte se encuentran almacenadas en una
    lista llamada "notas" que ya hemos definido al comienzo del archivo

    Debe caluclar el promedio de todas las notas y luego transformar
    la califiación en una letra según la escala establecida en el ejercicio
    "calificaciones" <condicionales_python / ejercicios_practica / ej3>

    A medida que recorre las notas, no debe considerar como válidas aquellas
    que son negativas, en ese caso el alumno estuvo ausente

    Debe contar la cantidad de notas válidas y la cantidad de ausentes
    '''
    # Si el puntaje es mayor igual a 90 --> imprimir A
    # Si el puntaje es mayor igual a 80 --> imprimir B
    # Si el puntaje es mayor igual a 70 --> imprimir C
    # Si el puntaje es mayor igual a 60 --> imprimir D
    # Si el puntaje es manor a  60      --> imprimir F
    # Para calcular el promedio primero debe obtener la suma
    # de todas las notas, que irá almacenando en esta variable
    sumatoria = 0                # Ya le hemos inicializado en 0

    cantidad_notas = 0            # Aquí debe contar cuantas notas válidas encontró
    cantidad_ausentes = 0         # Aquí debe contar cuantos ausentes hubo
    x = (len(notas))

    for numero in notas:
        if numero > 0:
            sumatoria = sumatoria + numero
        
        elif numero < 0:
            cantidad_ausentes= cantidad_ausentes + numero
    print('los dias no asisitidos fueron :',cantidad_ausentes)
        
    cantidad_notas= x + cantidad_ausentes
    promedio= sumatoria/cantidad_notas
    if promedio >= 90:
        print ('a'.upper())
    elif promedio>=80:
        print('b'.upper())
    elif promedio>=70:
        print('la calificacion es c'.upper())
    elif promedio <=60:
        print('f'.upper())


    # Realice aquí el bucle para recorrer todas las notas
    # y cacular la sumatoria
    # Terminado el bucle calcule el promedio como
    # promedio = sumatoria / cantidad_notas
    # Utilice la nota promedio calculada y transformela
    # a calificación con letras, imprima en pantalla el resultado
    # Imprima en pantalla al cantidad de ausentes
    
    
   
            
            





   
    
     



def ej4():
    print("Mi primer pasito en data analytics")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_profundizacion /ej5>,
    copielo a este ejercicio y modifíquelo para cumplir el
    siguiente requerimiento

    En este ejercicio se lo provee de una lista de temperatuas,
    esa lista de temperatuas corresponde a los valores de temperaturas
    tomados durante una temperorada del año en Buenos Aires.
    Ustede deberá analizar dicha lista para deducir
    en que temporada del año se realizó el muestreo de temperatura.
    La variable con la lista de temperaturas se llama "temp_dataloger"
    definida al comienzo del archivo

    Debe recorrer la lista "temp_dataloger" y obtener los siguientes
    resultados

    1 - Obtener la máxima temperatura
    2 - Obtener la mínima temperatura
    3 - Obtener el promedio de las temperatuas

    Los resultados se deberán almacenar en las siguientes variables
    que ya hemos preparado para usted.
    
    NOTA: No se debe ordenar la lista de temperaturas, se debe obtener
    el máximo y el mínimo utilizando los mismos métodos vistos
    durante la clase (ejemplos_clase)
    '''

    temperatura_max = None      # Aquí debe ir almacenando la temp máxima
    temperatura_min = None      # Aquí debe ir almacenando la temp mínima
    temperatura_sumatoria = 0   # Aquí debe ir almacenando la suma de todas las temp
    temperatura_promedio = 0    # Al finalizar el loop deberá aquí alamcenar el promedio
    temperatura_len = (len(temp_dataloger))  # Aquí debe almacenar cuantas temperatuas hay en la lista
    
    
    

    # Colocar el bucle aqui......
    for num in temp_dataloger:
        if (temperatura_max is None or num > temperatura_max):
            temperatura_max = num
        elif (temperatura_min is None or num < temperatura_min):
            temperatura_min = num
    for numero in temp_dataloger:
        if numero > 0:
            temperatura_sumatoria = temperatura_sumatoria + numero
        
    temperatura_promedio = temperatura_sumatoria/temperatura_len
    
    for numero in temp_dataloger:
        if numero > 8  < 14:
            print('La epoca del año es \n invierno')
        elif numero > 11 < 20:
            print('La epoca del año es \n otoño')
        elif numero > 10 < 24:
            print('La epoca del año es \n primavera')
        elif numero > 19 < 28:
            print('la epoca del año es \n verano')
    
    
    

    # Al finalizar el bucle compare si el valor que usted calculó para
    # temperatura_max y temperatura_min coincide con el que podría calcular
    # usando la función "max" y la función "min" de python
    # función "max" --> https://www.w3schools.com/python/ref_func_max.asp
    # función "min" --> https://www.w3schools.com/python/ref_func_min.asp

    # Al finalizar el bucle debe calcular el promedio como:
    # temperatura_promedio = temperatura_sumatoria / cantidad_temperatuas

    # Corroboren los resultados de temperatura_sumatoria
    # usando la función "sum"
    # función "sum" --> https://www.w3schools.com/python/ref_func_sum.asp

    '''
    Una vez que tengamos nuestros valores correctamente calculados debemos
    determinar en que epoca del año nos encontramos en Buenos Aires utilizando
    la estadística de años anteriores. Basados en el siguiente link realizamos
    las siguientes aproximaciones:

    verano -->      min = 19, max = 28
    otoño -->       min = 11, max = 20
    invierno -->    min = 8, max = 14
    primavera -->   min = 10, max = 24

    Referencia:
    https://es.weatherspark.com/y/28981/Clima-promedio-en-Buenos-Aires-Argentina-durante-todo-el-a%C3%B1o
    '''

    # En base a los rangos de temperatura de cada estación,
    # ¿En qué época del año nos encontramos?
    # Imprima el resultado en pantalla
    # Debe utilizar temperatura_max y temperatura_min para definirlo


def ej5():
    print("Ahora sí! buena suerte :)")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_profundizacion / ej4>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Realize un programa que corra indefinidamente en un bucle, al comienzo de la
    iteración del bucle el programa consultará al usuario con el siguiente menú:
    1 - Obtener la palabra más grande por orden alfabético (usando el operador ">")
    2 - Obtener la palabra más grande por cantidad de letras (longitud de la palabra)
    3 - Salir del programa

    En caso de presionar "3" el programa debe terminar e informar por
    pantalla de que ha acabado,
    en caso contrario si se presionar "1" o "2" debe continuar con la siguiente tarea

    NOTA: Si se ingresa otro valor que no sea 1, 2 o 3 se debe enviar
    un mensaje de error y volver a comenzar el bucle
    (vea en el apunte "Bucles - Sentencias" para encontrar
    la sentencia que lo ayude a cumplir esa tarea)

    Si el bucle continua (se presionó "1" o "2") se debe ingresar a otro bucle
    en donde en cada iteración se pedirá una palabra. La cantidad de iteración
    (cantidad de palabras a solicitar) lo dejamos a gusto del alumno, intente que esa
    condición esté dada por una variable (ej: palabras_deseadas = 4)
    Cada palabra ingresada se debe ir almacenando en una lista de palabras, dicha
    lista la debe inicializar vacia y agregar cada nuevo valor con el método "append".
    Luego de tener las palabras deseadas almacenadas en una lista de palabras
    se debe proceder a realizar las siguientes tareas:

    Si se ingresa "1" por consola se debe obtener la palabra
    más grande por orden alfabético
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra
    más grande alfabeticamente.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?

    Si se ingresa "2" por consola se debe obtener la palabra
    con mayor cantidad de letras
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra con
    mayor cantidad de letras.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?
    
    NOTA: No se debe ordenar la lista de palabras, se debe obtener
    el máximo utilizando el mismos métodos vistos durante la clase
    (ejemplos_clase), tal como el ejercicio anterior. Ordenar una
    lista representa un problema mucho más complejo que solo
    buscar el máximo.

    NOTA: Es recomendable que se organice con lápiz y papel para
    hacer un bosquejo del sistema ya que deberá utilizar 3 bucles en total,
    1 - El bucle principal que hace que el programa corra hasta ingresar un "3"
    2 - Un bucle interno que corre hasta socilitar todas las palabras deseadas
        que se deben ir guardando en una lista
    3- Otro bucle interno que corre luego de que termine el bucle "2" que
       recorre la lista de palabras y busca la mayor según el motivo ingresado ("1" o "2")

  '''
    pa_1 = (input('Ingrese primer palabra:\n'))
    pa_2 = (input('Ingrese segunda palara:\n'))
    pa_3 = (input('Ingrese tercer palabra:\n'))
    lista = [pa_1,pa_2,pa_3]
    alf = sorted(lista)
    long = sorted(lista,key=len, reverse=True)
    
    








    
    
        
        
    

if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
