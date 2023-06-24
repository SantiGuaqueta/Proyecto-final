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
