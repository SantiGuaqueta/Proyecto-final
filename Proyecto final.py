import random
import getpass
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
def palabras(apt1,apt2,k,posiciones,matrizA,apt,lista): # Declaro mi segunda funcion la cual se utilizara para rellenar la sopa de letras.
   
    while posiciones < k: # Realizo un bucle el cual sirve para contabilizar la cantidad de calabras que quiero agregar
        posiciones +=1 # Contador que sirve para que el bucle llegue a su fin
        apt+=1 # Contador que me servira para declarar el numero de la palabra osea cual palabra estamos agrgando ejemplo la 1 2 o 3
        palabra=getpass.getpass("Escribe la palabra numero "+ str(apt)+ " a agregar: ") # Le pido al usuario la primera palabra
        palabra=palabra.lower() # Aplicamos metodo lower por si nos dan la palabra en mayuscula
        palabra=palabra.strip()  # Aplicamos metodo strip por si el usuario ingresa espacios al final o al inicio de la palabra
        lista.append(palabra) # Añadimos la palabra ingresada a una lista que se usara mas adelante
        eleccion=int(getpass.getpass("Dirección de la palabra (1: horizontal, 2: vertical, 3: diagonal): ")) # Declaramos la primera eleccion la cual nos sirve para que el usuario nos indique la posicion de la palabra
        while eleccion > 3: # Ciclos que agregamos por si no se cumple la condicion
                print("La opcion que elegiste en la direccion de palabra no se encuentra por favor no cometer este mismo error de nuevo")
                eleccion=int(getpass.getpass("Dirección de la palabra (1: horizontal, 2: vertical, 3: diagonal): ")) # Volvemos a pedir la eleccion
        
        eleccion2=int(getpass.getpass("Dirección 2 de la palabra (1: De izquierda a derecha o de arriba hacia abajo, 2: De derecha a izquierda o de abajo hacia arriba):"))# Declaramos segunda eleccion que nos dira como quiere que se posicione la palabra
        while eleccion2 > 2: # Ciclos que agregamos por si no se cumple la condicion
                print("La opcion que elegiste en la direccion 2 de palabra no se encuentra por favor no cometer este mismo error de nuevo")
                eleccion2=int(getpass.getpass("Dirección 2 de la palabra (1: De izquierda a derecha o de arriba hacia abajo, 2: De derecha a izquierda o de abajo hacia arriba):"))# Volvemos a pedir la eleccion
        
        apt1=int(getpass.getpass("Escriba en que fila quiere que se encuentre la palabra: ")) # Preguntamos al usuario en que fila quiere la palabra esta fila es fila inicial
        while apt1 > filas_A: # Ciclos que agregamos por si no se cumple la condicion
            print("Esta fila no se encuentra disponible en el tamaño que pusiste")
            apt1=int(getpass.getpass("Escriba en que fila quiere que se encuentre la palabra: "))# Volvemos a pedir la eleccion
        apt1-= 1
        apt2=int(getpass.getpass("Escriba en que columna quiere que se encuentre la palabra: ")) # Preguntamos al usuario en que columna quiere la palabra esta columna es columna inicial 
        while apt2 > columnas_A: # Ciclos que agregamos por si no se cumple la condicion
            print("Esta columna no se encuentra disponible en el tamaño que pusiste")
            apt2=int(getpass.getpass("Escriba en que columna quiere que se encuentre la palabra: "))# Volvemos a pedir la eleccion
        apt2-= 1
        if eleccion == 1: # realizo una sentencia o condicional if el cual evalua cual fue la eleccion 1 elegida por el usiario 
            if eleccion2==1: # Realizo otra sentencia o condicional if el cual evalua cual fue la eleccion 2 elegida por el usuario
                if apt2 + len(palabra) <= columnas_A: # Esta condicion evalua si la palabra escrita tiene el tamaño requerido para ser ingresada a la sopa de letras en este caso como la palabra va a estar horizontalmente se evalua en realcion a las columnas
                    for i in range(len(palabra)): # Realizo un bucle for donde recorrere el rango de la palabra osea desde 0 hasta la cantidad de caracteres que tenga la palabra
                        matrizA[apt1][apt2 + i] = palabra[i] # Como la palabra se va a introducir horizontalmente aumentare las columnas unicamente la fila sera la misma y alfinal imprimo la letra que ira en esa pocicion
                else:
                    print(f"\nLo sentimos pero la palabra {palabra} demasiado grande para la ubicacion que elegiste y no es posible ingresarla\n") # Escribo esto si la palabra no se puede agregar
                    lista=lista.remove(palabra) # Y la remuevo de la lista que contendra las palabras que estan DENTRO de la sopa de letras
            else: # Este else es relacionado a la eleccion 2
                if apt2 - len(palabra) <= columnas_A and apt2 - len(palabra) >= 0 : # De nuevo evaluo si la palabra se puede ingresar   
                    for i in range(len(palabra)): # Recorro desde 0 hasta la cantidad de letras o caracteres que tiene la palabra
                        matrizA[apt1][apt2 - i] = palabra[i] # En este caso como la palabra queremos que vaya de derecha a izquierda vamos a restar i a la cantidad de columnas dada
                else:
                    print(f"\nLo sentimos pero la palabra {palabra} demasiado grande para la ubicacion que elegiste y no es posible ingresarla\n") # Escribo esto si la palabra no se puede agregar
                    lista=lista.remove(palabra) # Y la remuevo de la lista que contendra las palabras que estan DENTRO de la sopa de letras
        elif eleccion ==2: # Elif relazionado a la elleccion 1
            if eleccion2 == 1: # Realizo otra sentencia o condicional if el cual evalua cual fue la eleccion 2 elegida por el usuario
                if apt1 +len(palabra) <= filas_A: # Esta condicion evalua si la palabra escrita tiene el tamaño requerido para ser ingresada a la sopa de letras en este caso como la palabra va a estar verticalmente evaluamos es en filas
                    for i in range(len(palabra)): # Realizo un bucle for donde recorrere el rango de la palabra osea desde 0 hasta la cantidad de caracteres que tenga la palabra
                       matrizA[apt1 + i][apt2] = palabra[i] # Como la palabra se va a introducir verticalmente aumentare las filas unicamente la columna sera la misma y al final imprimo la letra que ira en esa pocicion
                else:
                    print(f"\nLo sentimos pero la palabra {palabra} demasiado grande para la ubicacion que elegiste y no es posible ingresarla\n") # Escribo esto si la palabra no se puede agregar
                    lista=lista.remove(palabra) # Y la remuevo de la lista que contendra las palabras que estan DENTRO de la sopa de letras
            else: # Este else es relacionado a la eleccion 2
                if apt1 - len(palabra) <= filas_A and apt1 - len(palabra) >= 0: # De nuevo evaluo si la palabra se puede ingresar
                    for i in range(len(palabra)): # Realizo un bucle for donde recorrere el rango de la palabra osea desde 0 hasta la cantidad de caracteres que tenga la palabra
                        matrizA[apt1 - i][apt2] = palabra[i] # En este caso como la palabra queremos que vaya de abajo hacia ariiba vamos a restar i a la cantidad de filas dada
                else:
                    print(f"\nLo sentimos pero la palabra {palabra} demasiado grande para la ubicacion que elegiste y no es posible ingresarla\n") # Escribo esto si la palabra no se puede agregar
                    lista=lista.remove(palabra) # Y la remuevo de la lista que contendra las palabras que estan DENTRO de la sopa de letras

        else: # Este else es porque ya solo queda la opcion 3
            if eleccion2 ==1: # Condicional que evalua la eleccion 2 que eligio el usuario
                if apt2 + len(palabra) <= columnas_A:  # Evalua si la palabra se puede ingresar en la sopa de letras en el lugar escogido
                    if apt1 +len(palabra) <= filas_A: # evalua por segunda vez si la palabra se puede agregar
                        for i in range(len(palabra)): # Recorremos la cantidad de caracteres que tiene la palabra con ayuda de un for
                            matrizA[apt1 + i][apt2+ i] = palabra[i] # Como la palabra se va a introducir en diagonal vamos a ir sumando la cantidad de filas y columnas con el valor que tenga i
                else:
                    print(f"\nLo sentimos pero la palabra {palabra} demasiado grande para la ubicacion que elegiste y no es posible ingresarla\n") # Escribo esto si la palabra no se puede agregar
                    lista=lista.remove(palabra) # Y la remuevo de la lista que contendra las palabras que estan DENTRO de la sopa de letras
            else:
                if apt2 - len(palabra) <= columnas_A: # Evalua si la palabra se puede ingresar en la sopa de letras en el lugar escogido
                    if apt1 -len(palabra) <= filas_A: # Evalua por segunda vez si la palabra se puede agregar
                        for i in range(len(palabra)): # Recorremos la cantidad de caracteres que tiene la palabra con ayuda de un for
                            matrizA[apt1 - i][apt2- i] = palabra[i]  # Como la palabra se va a introducir en diagonal pero invertida vamos a ir restando la cantidad de filas y columnas con el valor que tenga i
                else:
                    print(f"\nLo sentimos pero la palabra {palabra} demasiado grande para la ubicacion que elegiste y no es posible ingresarla\n") # Escribo esto si la palabra no se puede agregar
                    lista=lista.remove(palabra) # Y la remuevo de la lista que contendra las palabras que estan DENTRO de la sopa de letras

def buscar_palabra(matriz, palabra):
    # Obtener el número de filas y columnas de la matriz
    filas = len(matriz)
    columnas = len(matriz[0])
    longitud = len(palabra)

    # Convertir la palabra a minúsculas para una búsqueda insensible a mayúsculas
    palabra = palabra.lower()

    # Direcciones posibles: horizontal, vertical, diagonal superior y diagonal inferior
    direcciones = [(1, 0), (0, 1), (1, 1), (1, -1)]

    # Iterar sobre todas las filas de la matriz
    for fila in range(filas):
        # Iterar sobre todas las columnas de la matriz
        for columna in range(columnas):
            # Iterar sobre todas las direcciones posibles
            for direccion in direcciones:
                dx, dy = direccion
                # Calcular la posición de la última letra de la palabra en la dirección actual
                ultimo_fila = fila + (longitud - 1) * dx
                ultimo_columna = columna + (longitud - 1) * dy

                # Verificar si las coordenadas están dentro de la matriz
                if (
                    ultimo_fila >= 0
                    and ultimo_fila < filas
                    and ultimo_columna >= 0
                    and ultimo_columna < columnas
                ):
                    encontrado = True
                    # Verificar si la palabra se encuentra en la dirección actual
                    for i in range(longitud):
                        fila_actual = fila + i * dx
                        columna_actual = columna + i * dy

                        # Convertir la letra actual a minúsculas para una búsqueda insensible a mayúsculas
                        letra_actual = matriz[fila_actual][columna_actual].lower()

                        # Verificar si la letra actual coincide con la letra de la palabra en la misma posición
                        if letra_actual != palabra[i]:
                            encontrado = False
                            break

                    # Si se encontró la palabra, devolver True
                    if encontrado:
                        return True

    # Si la palabra no se encontró en ninguna dirección, devolver False
    return False

if __name__ == "__main__":
    print(f"\n{jugador1} Introduce los valores por filas para la matriz. Recuerde que la cantidad de filas es igual a la cantidad de columnas.") # Recalco que la cantidad de filas es igual a la de columnas por lo cual no podra seleccionar la cantidad de columnas solo de filas
    # Creo la  matriz
    print("El valor minimo de las filas es 10 y el valor maximo 30") # Recalco la aclaracion y condicion que tiene el programa
    filas_A = int(input("Especifique el numero de filas de la primera matriz: ")) # Pido cantidad de filas
    while filas_A < 10 or filas_A > 30: # Un ciclo donde el programa analiza si el usuario realizo caso a la cantidad de filas min y max
        print("Error como te comentamos antes el valor de filas debe ser minimo 10 y maximo 30") # Como no hizo caso le recalca su error
        filas_A=int(input("Especifique el numero de filas de la primera matriz: ")) # Y pide de nuevo la cantidad de filas. El bucle se repite hasta que las filas no cumplan la condicion del while
    columnas_A = filas_A # No doy opcion a elegir columnas en este momento digo que columnas igual a filas
    matrizA = Crear_Matriz(filas_A,columnas_A) # Llamo a la funcion crear matriz
    #for i in range (0,filas_A): 
        #print(matrizA[i]) # imprimo la matriz
    
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
    letras_encontradas = {}  # Inicializar como un diccionario vacío
    
    for fila in matrizA: # Creamos un for que recorrera la matriz
        print(' '.join(fila)) # Y la imprimimos en este caso utilizamos join que nos sirve para dejar espacio entre columna y columna 
        a=fila
    print(f"{jugador2}, {jugador1} ya realizo su sopa de letra ahora es tu turno de resolverla") 

# Obtener la palabra a buscar del usuario
    puntos=1 # Variable que servira para el puntaje
    for q in range(1,k+1):
     print("\nSi la palabra se encuentra invertida escriba la palabra invertida ej: si la palabra es 'hola' y esta invertida al ingresar la palabra ingresela como 'aloh'") # Aclaracion importante
     palabra_usuario = input("Ingresa la palabra a buscar: ")

     matriz=[] #se crea matriz vacia 
     for fila in matrizA: #Creamos un for que recorrera la matriz inicial(matrizA)
      matriz.append(fila) #agregamos cada fila de la matrizA a la nueva matriz
     encontrada = buscar_palabra(matriz, palabra_usuario) #llamamos la funcion para buscar la palabra
     if encontrada: #creamos condicional para que imprima texto segun si encontro la palabra en la sopa
      print("La palabra se encontró en la sopa de letras.")
      puntos +=1 # Les sumamos 1 punto si acerto
     else:
      print("La palabra no se encontró en la sopa de letras.")
      puntos -=1 # Les restamos 1 punto si no acerto
    # Agrego con condicionales todos los casos posibles y dependiendo del numero que tenga la variable numeros la evaluo con la variable k y depende de la condicion que se cumpla el puntaje obtenido sera diferente
    if puntos >= k:
        print("\nGenial "+str(jugador2)+" haz completado la sopa de letras")
        print(f"{jugador2} tu  puntuacion es = 100")
    elif puntos > k/2 and puntos < k:
        print("\nSuerte a la proxima "+str(jugador2)+" no lograste compeltar la sopa de letras en su totalidad")
        print(f"{jugador2} tu puntuacion es = 70")
    elif puntos == k//2:
        print("\nSuerte a la proxima "+str(jugador2)+" no lograste compeltar la sopa de letras en su totalidad")
        print(f"{jugador2} tu puntuacion es = 50")
    elif puntos < k/2 and puntos >= 0 :
        print("\nSuerte a la proxima "+str(jugador2)+" no lograste compeltar la sopa de letras en su totalidad")
        print(f"{jugador2} tu puntuacion es = 30")
    elif puntos < 0:
        print("\nQue mal "+str(jugador2)+" no encontraste ni una palabra de la sopa de letras")
        print(f"{jugador2} tu puntuacion es = 0")
