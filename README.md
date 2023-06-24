# Proyecto-final 
Bienvenidos a este repositorio donde presentaremos el desarrollo del proyecto de programación propuesto por nuestro profesor Felipe González Roldán. Antes de comenzar, es importante recalcar que el proyecto que presentaremos a continuación consiste en una sopa de letras programada en Python, donde aplicamos la mayoría de los temas que hemos visto en clase el día de hoy. Sin más preámbulos, ¡comencemos!
## ¿Como se abordo?

En este proyecto, abordamos la creación de una sopa de letras siguiendo los siguientes pasos. En primer lugar, planteamos la necesidad de crear una matriz que almacenara todas las letras. Esta matriz debía cumplir ciertas características, como tener un tamaño mínimo de 10x10 y un máximo de 30x30. Tras analizar esta consideración, tomamos la decisión de crear una matriz cuadrada, donde el número de filas sea igual al número de columnas.
El segundo aspecto que abordamos en este proyecto fue cómo introducir las letras en la sopa de letras. Para resolver este problema, planteamos el uso de dos punteros, uno para la fila y otro para la columna, como se muestra en la imagen 1. 

[![Captura-de-pantalla-2023-06-23-211020.png](https://i.postimg.cc/m2vthRvZ/Captura-de-pantalla-2023-06-23-211020.png)](https://postimg.cc/kBynprML) [![Captura-de-pantalla-2023-06-23-211446.png](https://i.postimg.cc/2j4zTvMY/Captura-de-pantalla-2023-06-23-211446.png)](https://postimg.cc/pyLbL9Pc)

Inicialmente, nos enfocamos en introducir las palabras en posición horizontal. Para lograr esto, recorrimos la palabra y aumentamos el puntero de la columna, agregando letra por letra a la ubicación señalada en la matriz. Una vez resuelta la posición horizontal, repetimos el proceso para las demás posiciones. Si la palabra se introducía en posición vertical, el puntero de la fila debía aumentar. Para las palabras en posición diagonal, los punteros se sumaban simultáneamente. Si deseábamos invertir la palabra, los punteros debían disminuir, dependiendo de la posición deseada. Gráficamente, se puede representar de la siguiente manera.
### Normal
[![Captura-de-pantalla-2023-06-23-211823.png](https://i.postimg.cc/JnYj2vGy/Captura-de-pantalla-2023-06-23-211823.png)](https://postimg.cc/hzxJJC8g) 
### Invertido
[![Captura-de-pantalla-2023-06-23-213942.png](https://i.postimg.cc/Nf2P1q0P/Captura-de-pantalla-2023-06-23-213942.png)](https://postimg.cc/crZmSzwQ)

El tercer aspecto abordado en este proyecto fue la cantidad de palabras a agregar a la sopa de letras. Con el fin de facilitar y hacerlo más práctico, decidimos establecer un límite máximo de palabras, que sería la mitad de las filas elegidas. El mínimo de palabras permitidas sería 1. En caso de que se eligiera un valor distinto, se mostraría un error y se ofrecería la opción de volver a elegir la cantidad de palabras. Si se seleccionaba la cantidad máxima de palabras, se implementó un contador y un bucle para agregar las palabras a la sopa de letras y a una lista que vería el segundo jugador para completar la sopa de letras.
De esta manera, se estableció un límite adecuado para el número de palabras a agregar, asegurando una experiencia óptima en la resolución de la sopa de letras.

### continuen uds como abordaron lo demas no metan code sino expliquen como vieron el problema y lo solucionaron

## Codigo y diagramas de flujo
### Primera parte
``` python
import random
titulo="SOPA DE LETRAS PROGRASAURIA" # Declaro titulo
print(titulo.center(150)) # Con un metodo de center dejo lo mas centrado el titulo 
# Protocolo
print("¡Bienvenidos a la emocionante aventura de la sopa de letras!")
print("Adelante, atrévete a sumergirte en esta emocionante sopa de letras. Deja que tu pasión por las palabras te guíe a través de este desafío y que tu espíritu de aventura") 
print("te lleve a descubrir todos los tesoros que se esconden entre las letras. Que disfrutes de esta experiencia llena de palabras y diversión! Bienvenido(a) a la maravillosa aventura de la sopa de letras prograsauria.")
# Pido nombres
jugador1=input("\nEscribe el nombre del primer jugador: ")
jugador2=input("Escribe el nombre del segundo jugador: ")
# Utilizo metodo capitalize para que solo la primera letra de los nombres quede en mayuscula y el resto en minuscula como es un sopa de letras prehistorica nosotros respetamos que los nombres inicien en mayuscula y el resto en minuscula
jugador1=jugador1.capitalize() 
jugador2=jugador2.capitalize()
print(f"\nHola {jugador1}  tu seras el que creara la sopa de letras para que {jugador2} pueda resolverla")
def Crear_Matriz(filas_A,columnas_A): # Declaro mi primera funcion la cual se utilizara para crear la sopa de letras.
    matriz=[] # Dejare esta lista de nombre matriz vacia.
    for i in range (0,filas_A): # Declaro que para i en el rango de 0 hasta las filas que halla puesto el lector realice lo siguiente.
        fila= [] # Ingreso otra variable vacia
        for j in range(0, columnas_A): # Ahora declaro que para j en el rango de 0, hasta columnas realice lo siguiente.
            valor= chr(random.randint(100,120)) # relleno con valores aleatorios esto gracias al metodo random que importamos
            fila. append(valor) # el anterior entero se adiciona a la lista vacia llamada fila que declaramos antes. 
        matriz.append(fila) # Ahora pido que la fila se adicione a la matriz vacia antes declarada.
    return(matriz) # Pido que retorne matriz

if __name__ == "__main__":
    print(f"\n{jugador1} Introduce los valores por filas para la matriz. Recuerde que la cantidad de filas es igual a la cantidad de columnas.") # Recalco que la cantidad de filas es igual a la de columnas por lo cual no podra seleccionar la cantidad de columnas solo de filas
    # Creo la  matriz
    print("El valor minimo de las filas es 10 y el valor maximo 30") # Recalco la aclaracion y condicion que tiene el programa
    filas_A = int(input("Especifique el numero de filas de la primera matriz: ")) # Pido cantidad de filas
    while filas_A < 10 or filas_A >= 30: # Un ciclo donde el programa analiza si el usuario realizo caso a la cantidad de filas min y max
        print("Error como te comentamos antes el valor de filas debe ser minimo 10 y maximo 30") # Como no hizo caso le recalca su error
        filas_A=int(input("Especifique el numero de filas de la primera matriz: ")) # Y pide de nuevo la cantidad de filas. El bucle se repite hasta que las filas no cumplan la condicion del while
    columnas_A = filas_A # No doy opcion a elegir columnas en este momento digo que columnas igual a filas
    matrizA = Crear_Matriz(filas_A,columnas_A) # Llamo a la funcion crear matriz
    #for i in range (0,filas_A): 
        # print(matrizA[i])  imprimo la matriz
```
En esta sección inicial del código, se establece el protocolo del juego y se define la primera función. En el protocolo, se crea una variable llamada "titulo" que almacena el título del juego, "SOPA DE LETRAS PROGRASAURIA". Luego, se imprime el título centrado utilizando el método center(150) para asegurar su presentación estética. A continuación, se utilizan varios comandos print para dar una breve introducción al juego, explicando que se trata de encontrar palabras ocultas en una sopa de letras y solicitando los nombres de los dos jugadores. Para garantizar la falta de errores de portografia de los nombres, se utiliza el método capitalize() en los nombres ingresados mediante la función input(). Este método convierte la primera letra de cada nombre en mayúscula y el resto en minúscula.Con esto, se completa el protocolo del juego y se procede a la definición de la primera función.

Antes de hablar de la matriz, es importante mencionar la importancia del comando import random. Este comando permite utilizar la funcionalidad de la biblioteca o módulo "random" en Python. La biblioteca random proporciona una serie de funciones para generar números o letras aleatorias, lo cual es útil en diversos escenarios, incluyendo la generación de valores aleatorios para juegos, selección aleatoria de elementos de una lista, entre otros.

En esta función, se comienza solicitando al usuario que ingrese la cantidad de filas para la matriz utilizando la función input(). Se verifica que la cantidad de filas esté en el rango válido de 10 a 30 mediante un ciclo while. Si la condición no se cumple, se muestra un mensaje de error y se solicita nuevamente al usuario que ingrese la cantidad de filas. Una vez validada la cantidad de filas, se establece que la cantidad de columnas sea igual a la cantidad de filas. Luego, se crea una lista vacía llamada matriz, que se utilizará para almacenar las letras. A continuación, se utiliza un bucle for para recorrer las filas de la matriz. Dentro de este bucle, se declara una lista vacía llamada fila. Luego, se utiliza otro bucle for para recorrer las columnas de la matriz. Dentro de este segundo bucle, se genera una letra aleatoria utilizando la función chr(random.randint(100,120)). La letra generada se agrega a la lista fila, y luego esta lista se agrega a la lista matriz. De esta forma, se completa la creación de la matriz de letras. Es importante tener en cuenta que, hasta este punto, la matriz no se ha impreso.
## Diagramas

## Segunda parte 
``` python
def palabras(apt1,apt2,k,posiciones,matrizA,apt,lista): # Declaro mi segunda funcion la cual se utilizara para rellenar la sopa de letras.
   
    while posiciones < k: # Realizo un bucle el cual sirve para contabilizar la cantidad de calabras que quiero agregar
        posiciones +=1 # Contador que sirve para que el bucle llegue a su fin
        apt+=1 # Contador que me servira para declarar el numero de la palabra osea cual palabra estamos agrgando ejemplo la 1 2 o 3
        palabra=input("Escribe la palabra numero "+ str(apt)+ " a agregar: ") # Le pido al usuario la primera palabra
        palabra=palabra.lower() # Aplicamos metodo lower por si nos dan la palabra en mayuscula
        palabra=palabra.strip()  # Aplicamos metodo strip por si el usuario ingresa espacios al final o al inicio de la palabra
        lista.append(palabra) # Añadimos la palabra ingresada a una lista que se usara mas adelante
        eleccion=int(input("Dirección de la palabra (1: horizontal, 2: vertical, 3: diagonal): ")) # Declaramos la primera eleccion la cual nos sirve para que el usuario nos indique la posicion de la palabra
        while eleccion > 3:
                print("La opcion que elegiste en la direccion de palabra no se encuentra por favor no cometer este mismo error de nuevo")
                eleccion=int(input("Dirección de la palabra (1: horizontal, 2: vertical, 3: diagonal): "))
        
        eleccion2=int(input("Dirección 2 de la palabra (1: De izquierda a derecha o de arriba hacia abajo, 2: De derecha a izquirda o de abajo hacia arriba):"))# Declaramos segunda eleccion que nos dira como quiere que se posicione la palabra
        while eleccion2 > 2:
                print("La opcion que elegiste en la direccion 2 de palabra no se encuentra por favor no cometer este mismo error de nuevo")
                eleccion2=int(input("Dirección 2 de la palabra (1: De izquierda a derecha o de arriba hacia abajo, 2: De derecha a izquirda o de abajo hacia arriba):"))
        
        apt1=int(input("Escriba en que fila quiere que se encuentre la palabra: ")) # Preguntamos al usuario en que fila quiere la palabra esta fila es fila inicial
        while apt1 > filas_A:
            print("Esta fila no se encuentra disponible en el tamaño que pusiste")
            apt1=int(input("Escriba en que fila quiere que se encuentre la palabra: "))
        apt1-= 1
        apt2=int(input("Escriba en que columna quiere que se encuentre la palabra: ")) # Preguntamos al usuario en que columna quiere la palabra esta columna es columna inicial 
        while apt2 > columnas_A:
            print("Esta columna no se encuentra disponible en el tamaño que pusiste")
            apt2=int(input("Escriba en que columna quiere que se encuentre la palabra: "))
        apt2-= 1
        if eleccion == 1: # realizo una sentencia o condicional if el cual evalua cual fue la eleccion 1 elegida por el usiario 
            if eleccion2==1: # Realizo otra sentencia o condicional if el cual evalua cual fue la eleccion 2 elegida por el usuario
                if apt2 + len(palabra) <= columnas_A: # Esta condicion evalua si la palabra escrita tiene el tamaño requerido para ser ingresada a la sopa de letras en este caso como la palabra va a estar horizontalmente se evalua en realcion a las columnas
                    for i in range(len(palabra)): # Realizo un bucle for donde recorrere el rango de la palabra osea desde 0 hasta la cantidad de caracteres que tenga la palabra
                        matrizA[apt1][apt2 + i] = palabra[i] # Como la palabra se va a introducir horizontalmente aumentare las columnas unicamente la fila sera la misma y alfinal imprimo la letra que ira en esa pocicion
                else:
                    print("Lo sentimos pero la palabra que quieres ingresar es demasiado grande y no es posible ingresarla")
                    lista=lista.remove(palabra)
            else: # Este else es relacionado a la eleccion 2
                if apt2 - len(palabra) <= columnas_A and apt2 - len(palabra) >= 0 : # De nuevo evaluo si la palabra se puede ingresar   
                    for i in range(len(palabra)): # Recorro desde 0 hasta la cantidad de letras o caracteres que tiene la palabra
                        matrizA[apt1][apt2 - i] = palabra[i] # En este caso como la palabra queremos que vaya de derecha a izquierda vamos a restar i a la cantidad de columnas dada
        elif eleccion ==2: # Elif relazionado a la elleccion 1
            if eleccion2 == 1: # Realizo otra sentencia o condicional if el cual evalua cual fue la eleccion 2 elegida por el usuario
                if apt1 +len(palabra) <= filas_A: # Esta condicion evalua si la palabra escrita tiene el tamaño requerido para ser ingresada a la sopa de letras en este caso como la palabra va a estar verticalmente evaluamos es en filas
                    for i in range(len(palabra)): # Realizo un bucle for donde recorrere el rango de la palabra osea desde 0 hasta la cantidad de caracteres que tenga la palabra
                        matrizA[apt1 + i][apt2] = palabra[i] # Como la palabra se va a introducir verticalmente aumentare las filas unicamente la columna sera la misma y al final imprimo la letra que ira en esa pocicion
            else: # Este else es relacionado a la eleccion 2
                if apt1 - len(palabra) <= filas_A and apt1 - len(palabra) >= 0: # De nuevo evaluo si la palabra se puede ingresar
                    for i in range(len(palabra)): # Realizo un bucle for donde recorrere el rango de la palabra osea desde 0 hasta la cantidad de caracteres que tenga la palabra
                        matrizA[apt1 - i][apt2] = palabra[i] # En este caso como la palabra queremos que vaya de abajo hacia ariiba vamos a restar i a la cantidad de filas dada

        else: # Este else es porque ya solo queda la opcion 3
            if eleccion2 ==1: # Condicional que evalua la eleccion 2 que eligio el usuario
                if apt2 + len(palabra) <= columnas_A:  # Evalua si la palabra se puede ingresar en la sopa de letras en el lugar escogido
                    if apt1 +len(palabra) <= filas_A: # evalua por segunda vez si la palabra se puede agregar
                        for i in range(len(palabra)): # Recorremos la cantidad de caracteres que tiene la palabra con ayuda de un for
                            matrizA[apt1 + i][apt2+ i] = palabra[i] # Como la palabra se va a introducir en diagonal vamos a ir sumando la cantidad de filas y columnas con el valor que tenga i
            else:
                if apt2 - len(palabra) <= columnas_A: # Evalua si la palabra se puede ingresar en la sopa de letras en el lugar escogido
                    if apt1 -len(palabra) <= filas_A: # Evalua por segunda vez si la palabra se puede agregar
                        for i in range(len(palabra)): # Recorremos la cantidad de caracteres que tiene la palabra con ayuda de un for
                            matrizA[apt1 - i][apt2- i] = palabra[i]  # Como la palabra se va a introducir en diagonal pero invertida vamos a ir restando la cantidad de filas y columnas con el valor que tenga i
if __name__ == "__main__":
    print(f"\n{jugador1} Introduce los valores por filas para la matriz. Recuerde que la cantidad de filas es igual a la cantidad de columnas.") # Recalco que la cantidad de filas es igual a la de columnas por lo cual no podra seleccionar la cantidad de columnas solo de filas
    # Creo la  matriz
    print("El valor minimo de las filas es 10 y el valor maximo 30") # Recalco la aclaracion y condicion que tiene el programa
    filas_A = int(input("Especifique el numero de filas de la primera matriz: ")) # Pido cantidad de filas
    while filas_A < 10 or filas_A >= 30: # Un ciclo donde el programa analiza si el usuario realizo caso a la cantidad de filas min y max
        print("Error como te comentamos antes el valor de filas debe ser minimo 10 y maximo 30") # Como no hizo caso le recalca su error
        filas_A=int(input("Especifique el numero de filas de la primera matriz: ")) # Y pide de nuevo la cantidad de filas. El bucle se repite hasta que las filas no cumplan la condicion del while
    columnas_A = filas_A # No doy opcion a elegir columnas en este momento digo que columnas igual a filas
    matrizA = Crear_Matriz(filas_A,columnas_A) # Llamo a la funcion crear matriz
    #for i in range (0,filas_A): 
        # print(matrizA[i]) # imprimo la matriz
    
    # Recalco variables que utilizare
    apt = 0 
    apt1=0
    apt2=0
    
    print("\nAclaracion\nLa cantidad de palabras que se podra agregar maximo sera la mitad de la cantidad de filas")# Realizo una segunda condicion donde explico que la cantidad maxima de palabras es la mitad de filas que se ingresaron
    k=int(input("Cuantas palabras desea agregar: ")) # Pregunto cuantas palabras quiere
    while k > filas_A//2 or k <= 0: # bucle con condicion que la cantidad de palabras no sea mayor a la mitad de filas ni sea 0
        print("Error pusiste mas letras de las permitidas o no pusiste ninguna palabra") # Recalcamos su error
        k=int(input("Cuantas palabras desea agregar: ")) # Le pedimos de nuevo la cantidad de palabras que quiere agregar hasta que no cumpla las condiciones del bucle
    posiciones= 0 # Variable contador que se utiliza en la funcion de pedir palabras
    lista=[] # Lista vacia donde guardaremos las palabras que van a estar en la sopa de letras 
    palabra= palabras(apt1,apt2,k,posiciones,matrizA,apt,lista) # Llamamos a la funcion 
    
    for fila in matrizA: # Creamos un for que recorrera la matriz
        print(' '.join(fila)) # Y la imprimimos en este caso utilizamos join que nos sirve para dejar espacio entre columna y columna 

    print(f"{jugador2}, {jugador1} ya realizo su sopa de letra ahora es tu turno de resolverla, las palabras que tendras que buscar son las siguientes: ") 
    print("Lista de palabras: \n"+str(lista)) # Imprimo la lista con las palabras a buscar utilizo un salto de linea entre el titulo y las palabras
```
