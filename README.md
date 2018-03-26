# Python #

* ¿Cual es la diferencia entre un metodo de clase y un metodo de instancia?
    * En un metodo de instancia, el primer parametro que recibe es "self", el cual hace referencia a la instancia. Para poder llamar al metodo primero hay que instanciar la clase:
    ```python
    class Instancia(object):
        def __init__(self):
            pass
        def metodo(self):
            pass

    inst = Instancia()
    inst.metodo()
    ```
    * Los metodos de clase reciben como primer parametro a la clase. La diferencia con estos metodos es que no hay que instanciar a la clase para poder invocarlos. Se usa cuando se va a heredar de esta clase
    ```python
    class MiClase(object):
    def __init__(self):
        pass
    @classmethod
    def metodo(cls):
        pass

    MiClase.metodo()

    class Subclase(MiClase):
        pass

    Subclase.metodo()
    ```

* ¿Para que utilizamos super en la POO?
    * Se usa para ganar acceso a metodos heredados

* ¿Que son los args y kwargs?
    * ```args*``` sirve para pasarle un numero variable de argumentos a una funcion
    * ```kwargs**``` es para pasarle un numero variable de parametros en forma de {key: value}

* ¿Que es la multiherencia y como es trabajada por Python?
    * Es el manejo de herencia jerarquica desde una superclase hacia barias subclases y sub-sub clases.
    * Python maneja la herencia de metodos con un algoritmo de linearizacion de superclases, por medio del cual resuelve el orden de resolucion de metodos heredados.

* ¿Como inviertes el orden de una lista?
    * Usando el metodo reverse del objeto lista o usando 
    ```python
    L = list(1,2,3,4,5,6)
    print(L.reverse())
    print(L[::-1])
    ```

* ¿Que es un decorador o para que es utilizado?
    * Sirve para expandir la funcionalidad de una funcion. Yo uso decoradores para anadir manejo de excepciones a mis funciones.

# Django #

* ¿Que problema sucede cuando tenemos 2 migraciones con el mismo numero de secuencia y como solucionamos este problema?
    * no se pueden realizar los migrations, se debe reenumerar dentro del app/migrations/000#_initial.py

* Teniendo el modelo Persona con los atributos nombre, estatura, peso. Realizar un queryset de todos los objetos con peso mayor a 50, ordenados por estatura
```python
Persona.objects.filter(peso__gte=50).order_by('estatura')
```
* ¿Para que utilizamos un signal?
    * Para disparar un evento cuando se realiza un cambio en los modelos de la base de datos, como enviar un email cuando se cree un nuevo usuario

* ¿Como muestras la sentencia SQL ejecutada por un queryset?
    * Aqui se guarda la lista de queries
    ```python
    from django.db import connection
    print(connection.queries)
    ```
    * Tambien con:
    ```python
    MyModel.objects.filter(field='string').query
    ```

# Ejercicio

* Teniendo la URL como cadena, obtener el nombre de la imagen, URL: http://inkuvi.com/folder_images/enero/caratula.jpeg, la salida para este ejemplo debe ser: caratula.jpeg
```python
url = "http://inkuvi.com/folder_images/enero/caratula.jpeg"
filename = url.split("/")[-1] 
print(filename)
```

* Teniendo una lista con N elementos numericos en una lista, retornar todas las posiciones impares del mismo: ej. [3,4,5,9,7,8,1] salida: [4,9,8], ej: [9,7,5,1,3,2,4,8,6,5,0] salida: [7,1,2,8,5]
```python
items = list([9,7,5,1,3,2,4,8,6,5,0])

new_list = list(map(lambda x: x[1], filter(lambda x: x[0] % 2 != 0, list(enumerate(items)))))
print(new_list)
```
