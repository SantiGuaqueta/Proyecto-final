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

## Codigo y diagrama de flujo

