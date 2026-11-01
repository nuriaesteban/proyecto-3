# %%
#1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
#de cada letra en la cadena. Los espacios no deben ser considerados.

def frecuencia_letras(texto):
    """
    Cuenta la frecuencia de cada letra en una cadena,
    ignorando los espacios.

    Args:
        texto (str): Cadena de texto que se desea analizar.

    Returns:
        dict: Diccionario con cada letra y su frecuencia.

    """
    frecuencias = {}

    for letra in texto:
        if letra != " ":
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1

    return frecuencias


resultado = frecuencia_letras("Que buen dia hace hoy")
print(resultado)



# %%
#2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
numeros = [2,8,5,3,11]

def multiplicar (x):
    return x * 2
    """Funcion para devolver en formato lista , el resultado de una lista de numeros multiplicado por 2
    """
resultado = map (multiplicar, numeros)

print(f'El resultado de la funcion es: {list(resultado)}')


# %%
#3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
#devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo

def filtrar_palabras(palabras, objetivo):
    """
    Filtra una lista de palabras y devuelve aquellas que contienen
    la palabra objetivo.

    Args:
        palabras (list): Lista de palabras que se quieren comprobar.
        objetivo (str): Palabra o texto que deben contener las palabras.

    Returns:
        list: Lista con las palabras que contienen el objetivo.

    """
    return list(filter(lambda palabra: objetivo in palabra, palabras))


palabras = ["gato", "gatito", "perro", "gatera", "conejo"]
objetivo = "gat"

resultado = filtrar_palabras(palabras, objetivo)
print(resultado)

# %%
#4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
def restar(x, y):
    return x - y


def calcular_diferencias(lista1, lista2):
    """
    Calcula la diferencia entre los elementos de dos listas.

    Args:
        lista1 (list): Primera lista de números.
        lista2 (list): Segunda lista de números.

    Returns:
        list: Lista con las diferencias correspondientes.
    """
    return list(map(restar, lista1, lista2))


lista1 = [10, 20, 30, 40]
lista2 = [1, 2, 3, 4]

print(calcular_diferencias(lista1, lista2))

# %%
#5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
#defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
#que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
#una tupla que contenga la media y el estado.

def media_notas(x, nota_aprobado=5):
    """
    Calcula la media de una lista de notas y determina
    si el resultado es aprobado o suspenso.

    Parámetros:
        x (list): Lista de notas numéricas.
        nota_aprobado (float): Nota mínima para aprobar. Por defecto, 5.

    Devuelve:
        tuple: Una tupla con la media y el estado (aprobado o suspenso).
    """
    resultado = sum(x) / len(x)

    if resultado >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"

    return (resultado, estado)


lista_notas = [2.1, 5.2, 4.9, 8.7, 9.1]

resultado = media_notas(lista_notas)

print(resultado)



# %%
#6. Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial(n):
    """
    Calcula el factorial de un número de forma recursiva.

    Args:
        n (int): Número entero no negativo.

    Returns:
        int: Resultado del factorial de n.
    """
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


numero = 5
resultado = factorial(numero)

print(resultado)

# %%
#7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def tuplas_a_strings(lista):
    return list(map(str, lista))
    """
    Convierte una lista de tuplas en una lista de strings.

    Args:
        lista (list): Lista de tuplas que se desea convertir.

    Returns:
        list: Lista de strings, donde cada string representa una tupla.

    """

tuplas = [(1, 2), (3, 4), (5, 6)]
resultado = tuplas_a_strings(tuplas)

print(resultado)

# %%
#8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
#o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
#indicando si la división fue exitosa o no

def dividir_numeros():
    """
    Solicita dos números al usuario e intenta dividirlos.

    Controla los errores de valores no numéricos y
    división entre cero mediante una única excepción.
    """
    try:
        num1 = int(input("Introduce un número dividendo: "))
        num2 = int(input("Introduce el divisor: "))

        resultado = num1 / num2

        print(f"División exitosa. Resultado: {resultado}")

    except (ValueError, ZeroDivisionError):
        print("Error: Introduce números válidos y no dividas entre cero.")


dividir_numeros()

# %%
#9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
#excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
#"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

def filtrar_mascotas(mascotas):
    """
    Filtra una lista de mascotas excluyendo las que están prohibidas.

    Args:
        mascotas (list): Lista con los nombres de las mascotas.

    Returns:
        list: Nueva lista sin las mascotas prohibidas.

    """
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

    return list(filter(lambda mascota: mascota not in prohibidas, mascotas))


mascotas = ["Perro", "Mapache", "Gato", "Tigre", "Conejo", "Oso"]

resultado = filtrar_mascotas(mascotas)
print(resultado)

# %%
#10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
#excepción personalizada y maneja el error adecuadamente.

def promedio (lista):
    if len(lista) == 0:
        print(promedio)
    else:
        print('No hay numeros para hacer media ')

def calcular_promedio(lista):
    """
    Calcula el promedio de una lista de números.

    Args:
        lista (list): Lista de números.

    Returns:
        float: Promedio de los números o un mensaje de error.
    """
    if len(lista) == 0:
        print("Error: La lista está vacía")
    else:
        print(sum(lista) / len(lista))


numeros = [10, 7, 15, 4, 50]
numeros2 = []

resultado = calcular_promedio(numeros)


resultado = calcular_promedio(numeros2)



# %%
#·11.Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un 
#valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120, maneja las excepciones 
#adecuadamente.

"""
Solicita la edad al usuario y comprueba que esté entre 0 y 120.
"""

preguntar_edad = input("Introduce tu edad actual: ")

if preguntar_edad == "":
    print("Debes introducir una edad")

elif preguntar_edad.replace("-", "").replace(" ", "").isdecimal():
    preguntar_edad = int(preguntar_edad)

    if preguntar_edad < 0:
        print("La edad no puede ser negativa")
    elif preguntar_edad > 120:
        print("Deberías estar muerto")
    else:
        print("Edad correcta")

else:
    print("Debes introducir un número")


# %%
#12.Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()


frase = "Hola como estas hoy"


resultado = list(map(len, frase.split()))
    """funcion map() para devolver la longitud de las palabras de una frase
    """
print(resultado)

# %%
#13.Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en 
#mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()
letra ="AbGhuT"

convertir_tupla = list(map(lambda x: (x.upper(), x.lower()), set(letra)))

print(convertir_tupla)

# %%
#14.Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico.
# Usa la funcion filter()

def filtrar_palabras(lista, letra):
    """
    Filtra las palabras que comienzan por una letra determinada.

    Args:
        lista (list): Lista de palabras.
        letra (str): Letra que queremos buscar.

    Returns:
        list: Palabras que empiezan por esa letra.
    """
    return list(filter(lambda x: x[0] == letra, lista))

palabras = ["casa", "coche", "perro", "camino", "gato"]

resultado = filtrar_palabras(palabras, "c")

print(resultado)

# %%
#15.Crea una función lambda que  sume 3 a cada número de una lista dada.
    
sumar_tres = lambda lista: [x + 3 for x in lista]
numeros = [1, 9, 3, 7, 12]

print(sumar_tres(numeros))

# %%
#16.Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de 
#todas las palabras que sean más largas que n. Usa la función filter()

def filtrar_palabras(frase, n):
    """
    Devuelve las palabras que tienen más de n caracteres.

    Args:
        frase (str): Cadena de texto.
        n (int): Longitud mínima de las palabras.

    Returns:
        list: Lista de palabras que superan la longitud n.
    """
    palabras = frase.split()
    return list(filter(lambda x: len(x) > n, palabras))

frase = "Hola hace muy buen dia para pasear"
n = 3

resultado = filtrar_palabras(frase, n)

print(resultado)

# %%
#17.Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, 5,7,2 
#corresponde al número quinientos setenta y dos 572. Usa la función reduce()

from functools import reduce

def convertir_numero(digitos):
    """
    Convierte una lista de dígitos en un número entero.

    Args:
        digitos (list): Lista de números individuales.

    Returns:
        int: Número correspondiente a los dígitos.
    """
    return reduce(lambda x, y: x * 10 + y, digitos)

numeros = [5, 7, 2]

resultado = convertir_numero(numeros)

print(resultado)

# %%
#18.Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes 
#(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 
#90. Usa la función filter()

def filtrar_estudiantes(estudiantes):
    """
    Filtra los estudiantes que tienen una calificación
    mayor o igual a 90.

    Parámetros:
        estudiantes (list): Lista de diccionarios con los datos
        de los estudiantes.

    Devuelve:
        list: Lista de estudiantes que cumplen la condición.
    """
    resultado = filter(lambda x: x["calificacion"] >= 90, estudiantes)

    return list(resultado)


# Creamos la lista de estudiantes
estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 22, "calificacion": 85},
    {"nombre": "Marta", "edad": 21, "calificacion": 92},
    {"nombre": "Pedro", "edad": 19, "calificacion": 78},
    {"nombre": "Laura", "edad": 23, "calificacion": 90}
]

# Aplicamos la función
aprobados = filtrar_estudiantes(estudiantes)

print("Estudiantes con calificación igual o superior a 90:")

for estudiante in aprobados:
    print(estudiante)

# %%
#19.Crea una función lambda que filtre los números impares de una lista dada.

"""
Filtra los números impares de una lista.
"""

numeros = [11, 32, 13, 14, 45, 76, 97, 18, 9]

impares = list(filter(lambda x: x % 2 != 0, numeros))

print(impares)


# %%
#20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()
lista_mixta = [12, "caracol", 27, "arbol", 13, 18, "pasto"]

extraccion_int = list(filter(lambda x :type(x)== int ,lista_mixta))

print(extraccion_int)

# %%
#21.Crea una función que calcule el cubo de un número dado mediante una función lambda
numero_cubo =lambda x: x**3


numero = 7
resultado= numero_cubo(numero)

print(f'El cubo de numero {numero} es : {resultado}')

# %%
#22.Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .

from functools import reduce
def producto_lista(lista):
    """
    Calcula el producto total de los valores de una lista numérica.

    Parámetros:
        lista (list): Lista de números.

    Devuelve:
        int o float: Producto de todos los elementos de la lista.
    """
    return reduce(lambda x, y: x * y, lista)

numeros = [2, 9, 7, 5]

resultado = producto_lista(numeros)

print("El producto total es:", resultado)


# %%
#23.Concatena una lista de palabras.Usa la función reduce() 

from functools import reduce

def concatenar_palabras(lista):
    """
    Concatena todas las palabras de una lista en una única cadena.

    Parámetros:
        lista (list): Lista de palabras que se quieren concatenar.

    Devuelve:
        str: Cadena de texto con todas las palabras concatenadas.
    """
    return reduce(lambda x, y: x + y, lista)

palabras =["Hoy", " ","no", " ","me", " ","puedo", " ","levantar"]

resultado= concatenar_palabras(palabras)

print(resultado)

# %%
#24.Calcula la diferencia total en los valores de una lista. Usa la función reduce() .
from functools import reduce

def resta_lista (lista):
    return reduce(lambda x , y : x - y , lista)

    """
    Calcula el resultado total de  restar los valores de una lista numérica.

    Parámetros:
        lista (list): Lista de números.

    Devuelve:
        int o float: Producto de todos los elementos de la lista.
    """

valores = [25,2,11,1]

resultado = resta_lista(valores)

print(resultado)

# %%
#25.Crea una función que cuente el número de caracteres en una cadena de texto dada
def contar_caracteres(texto):
    """
    Cuenta el número de caracteres de una cadena de texto.

    Parámetros:
        texto (str): Cadena de texto que queremos analizar.

    Devuelve:
        int: Número total de caracteres de la cadena.
    """
    return len(texto)

cadena = "Hola equipo"

resultado = contar_caracteres(cadena)

print("El número de caracteres es:", resultado)

# %%
#26.Crea una función lambda que calcule el resto de la división entre dos números dados.

def calcular_resto(a, b):
    """
    Calcula el resto de la división entre dos números
    mediante una función lambda.

    Parámetros:
        a (int o float): Dividendo.
        b (int o float): Divisor.

    Devuelve:
        int o float: Resto de la división.
    """
    resto = lambda x, y: x % y
    return resto(a, b)


resultado = calcular_resto(17, 3)

print("El resto de la división es:", resultado)


# %%
#27.Crea una función que calcule el promedio de una lista de números.

def promedio_lista(lista):
    """
    Calcula el promedio de una lista de números
    utilizando una función lambda.

    Parámetros:
        lista (list): Lista de números.

    Devuelve:
        float: Promedio de los números de la lista.
    """
    resultado = lambda x: sum(x) / len(x)
    return resultado(lista)


numeros = [5, 12.2, 1, 7.1, 10]

resultado = promedio_lista (numeros)

print("El promedio es:", resultado)

# %%
#28.Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def primer_duplicado(lista):
    """
    Busca y devuelve el primer elemento duplicado de una lista.

    Parámetros:
        lista (list): Lista de elementos que queremos analizar.

    Devuelve:
        El primer elemento que aparece repetido.
        None si no existen elementos duplicados.
    """
    elementos_vistos = set()

    for elemento in lista:
        if elemento in elementos_vistos:
            return elemento
        elementos_vistos.add(elemento)

    return None

numeros = [2, 5, 8, 4, 5, 8, 2]

resultado = primer_duplicado(numeros)

print("El primer elemento duplicado es:", resultado)

# %%
#29.Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres  con el 
#carácter '#', excepto los últimos cuatro.

def enmascarar_datos(dato):
    """
    Convierte una variable en texto y enmascara todos sus caracteres,
    excepto los últimos cuatro.

    Args:
        dato: Variable que queremos enmascarar.

    Returns:
        Una cadena de texto con los caracteres enmascarados.
    """
    dato = str(dato)

    resultado = "#" * max(0, len(dato) - 4) + dato[-4:]

    return resultado


print(enmascarar_datos("123456789123"))
print(enmascarar_datos(987654321))
print(enmascarar_datos("Hola"))

# %%
#30.Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras 
#pero en diferente orden.
def comprobar_anagrama(palabra1, palabra2):
    """
    Comprueba si dos palabras son anagramas.

    Args:
        palabra1: Primera palabra.
        palabra2: Segunda palabra.

    Returns:
        True si las palabras son anagramas, False en caso contrario.
    """
    palabra1 = palabra1.lower().replace(" ", "")
    palabra2 = palabra2.lower().replace(" ", "")

    if sorted(palabra1) == sorted(palabra2):
        return True
    else:
        return False


palabra1 = input("Introduce la primera palabra: ")
palabra2 = input("Introduce la segunda palabra: ")

if comprobar_anagrama(palabra1, palabra2):
    print("Las palabras son anagramas")
else:
    print("Las palabras no son anagramas")

# %%
#31.Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en 
#esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se 
#lanza una excepción.

def buscador_persona():
    """
    Busca un nombre introducido por el usuario en una lista de personas.

    Returns:
        Imprime un mensaje indicando si la persona ha sido encontrada.
    """
    lista = ["Ana", "Juan", "Pedro", "María", "Luis", "Carmen"]

    print("Lista de personas:", lista)

    nombre = input("Nombre a comprobar: ")

    if nombre in lista:
        print("La persona fue encontrada en la base de datos")
    else:
        print("La persona no se encuentra en la base de datos")


buscador_persona()

# %%
#32.Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y 
#devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona 
#no trabaja aquí.

def buscador_empleado(nombre_completo, empleados):
    """
    Busca un empleado por su nombre completo en una lista de empleados.

    Args:
        nombre_completo: Nombre y apellidos del empleado.
        empleados: Lista de diccionarios con los datos de los empleados.

    Returns:
        El puesto del empleado si existe, o un mensaje indicando
        que la persona no trabaja aquí.
    """
    buscador = lambda empleado: empleado["nombre"] == nombre_completo

    for empleado in empleados:
        if buscador(empleado):
            return empleado["puesto"]

    return "Esta persona no trabaja aquí."


empleados = [
    {"nombre": "Juan Pérez", "puesto": "Programador"},
    {"nombre": "Ana García", "puesto": "Administrativa"},
    {"nombre": "Luis Martín", "puesto": "Diseñador"}
]

print(buscador_empleado("Juan Pérez", empleados))
print(buscador_empleado("Pedro López", empleados))



# %%
#33.Crea una función lambda que sume elementos correspondientes de dos listas dadas.
def suma_listas(lista1, lista2):
    """
    Suma los elementos correspondientes de dos listas.

    Args:
        lista1: Primera lista de números.
        lista2: Segunda lista de números.

    Returns:
        Una lista con la suma de los elementos correspondientes.
    """
    resultado = map(lambda x, y: x + y, lista1, lista2)
    return list(resultado)


print(suma_listas([1, 2, 3], [4, 5, 6]))

# %%
#34.Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: 
#crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para 
#manipular la estructura del árbol.
#Código a seguir:
#1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
#2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
#3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
#4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
#5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
#6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las 
#mismas.
#Caso de uso:
#1. Crear un árbol.
#2. Hacer crecer el tronco del árbol una unidad.
#3. Añadir una nueva rama al árbol.
#4. Hacer crecer todas las ramas del árbol una unidad.
#5. Añadir dos nuevas ramas al árbol.
#6. Retirar la rama situada en la posición 2.
#7. Obtener información sobre el árbol.

"""
Clase Arbol que representa un árbol con un tronco y varias ramas.

Permite:
- Hacer crecer el tronco.
- Añadir nuevas ramas.
- Hacer crecer todas las ramas.
- Eliminar una rama.
- Consultar la información del árbol.
"""


class Arbol:
    """
    Representa un árbol con un tronco y una lista de ramas.
    """

    def __init__(self):
        """
        Inicializa el árbol con un tronco de longitud 1
        y una lista vacía de ramas.
        """
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        """
        Aumenta la longitud del tronco en una unidad.
        """
        self.tronco += 1

    def nueva_rama(self):
        """
        Añade una nueva rama de longitud 1.
        """
        self.ramas.append(1)

    def crecer_ramas(self):
        """
        Aumenta la longitud de todas las ramas en una unidad.
        """
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        """
        Elimina una rama de una posición determinada.

        Args:
            posicion (int): Posición de la rama que queremos eliminar.
        """
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            raise IndexError("La posición de la rama no existe.")

    def info_arbol(self):
        """
        Devuelve información sobre el árbol.

        Returns:
            dict: Longitud del tronco, número de ramas
            y longitud de cada rama.
        """
        return {
            "Longitud del tronco": self.tronco,
            "Número de ramas": len(self.ramas),
            "Longitud de las ramas": self.ramas
        }


# CASO DE USO

# 1. Crear un árbol
arbol = Arbol()

# 2. Hacer crecer el tronco una unidad
arbol.crecer_tronco()

# 3. Añadir una nueva rama
arbol.nueva_rama()

# 4. Hacer crecer todas las ramas una unidad
arbol.crecer_ramas()

# 5. Añadir dos nuevas ramas
arbol.nueva_rama()
arbol.nueva_rama()

# 6. Retirar la rama situada en la posición 2
arbol.quitar_rama(2)

# 7. Obtener información del árbol
print("--- INFORMACIÓN DEL ÁRBOL ---")

informacion = arbol.info_arbol()

for clave, valor in informacion.items():
    print(f"{clave}: {valor}")


# %%
#36.Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta 
#corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y 
#agregar dinero al saldo.
#Código a seguir:
#Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante 
#Implementar el método True y False .
#retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
#Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. 
#Lanzará un error en caso de no poder hacerse.
#Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
#Caso de uso: Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
#2
# PROYECTO LÓGICA Katas de Python
#Agregar 20 unidades de saldo de "Bob".
#Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
#Retirar 50 unidades de saldo a "Alicia".


"""
Clase UsuarioBanco para gestionar cuentas bancarias.
Permite retirar, transferir y agregar dinero.
"""


class UsuarioBanco:
    """
    Representa a un usuario de un banco.
    """

    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        """Retira dinero del saldo del usuario."""

        if not self.cuenta_corriente:
            raise ValueError("No tiene cuenta corriente.")

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva.")

        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente.")

        self.saldo -= cantidad
        print(f"{self.nombre} ha retirado {cantidad} euros.")

    def transferir_dinero(self, otro_usuario, cantidad):
        """Transfiere dinero desde otro usuario al usuario actual."""

        if not self.cuenta_corriente or not otro_usuario.cuenta_corriente:
            raise ValueError("Ambos usuarios deben tener cuenta corriente.")

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva.")

        if cantidad > otro_usuario.saldo:
            raise ValueError("Saldo insuficiente para transferir.")

        otro_usuario.saldo -= cantidad
        self.saldo += cantidad

        print(f"Transferencia de {cantidad} euros realizada "
              f"de {otro_usuario.nombre} a {self.nombre}.")

    def agregar_dinero(self, cantidad):
        """Agrega dinero al saldo del usuario."""

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva.")

        self.saldo += cantidad
        print(f"Se han agregado {cantidad} euros a {self.nombre}.")


# CASO DE USO

try:
    # Crear usuarios
    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)

    # Agregar 20 euros a Bob
    bob.agregar_dinero(20)

    # Transferir 80 euros de Bob a Alicia
    alicia.transferir_dinero(bob, 80)

    # Retirar 50 euros de Alicia
    alicia.retirar_dinero(50)

except ValueError as error:
    print("Error:", error)

finally:
    # Mostrar los saldos finales
    print("\n--- SALDOS FINALES ---")
    print(f"Alicia: {alicia.saldo} euros")
    print(f"Bob: {bob.saldo} euros")




# %%
#37.Crea una función llamada procesar_texto que procesa un texto según la opción especificada: reemplazar_palabras , 
#procesar_texto .contar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro 
#de la función Código a seguir:
#Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
#Crear una función reemplazar_palabras para remplazar una que devolver el texto con el remplazo de palabras.
#Crear una función palabra_original del texto por una palabra_nueva . Tiene eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra 
#eliminada.
#Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.
#Caso de uso:Comprueba el funcionamiento completo de la función procesar_texto

"""
Programa para procesar un texto mediante diferentes opciones:
- Contar las palabras.
- Reemplazar una palabra por otra.
- Eliminar una palabra del texto.
"""


def contar_palabras(texto):
    """
    Cuenta cuántas veces aparece cada palabra en el texto.

    Args:
        texto (str): Texto que queremos analizar.

    Returns:
        dict: Diccionario con las palabras y sus frecuencias.
    """
    palabras = texto.split()
    contador = {}

    for palabra in palabras:
        palabra = palabra.lower()
        contador[palabra] = contador.get(palabra, 0) + 1

    return contador


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """
    Reemplaza una palabra original por una palabra nueva.

    Args:
        texto (str): Texto que queremos modificar.
        palabra_original (str): Palabra que queremos reemplazar.
        palabra_nueva (str): Nueva palabra.

    Returns:
        str: Texto con las palabras reemplazadas.
    """
    return texto.replace(palabra_original, palabra_nueva)


def eliminar_palabra(texto, palabra_eliminar):
    """
    Elimina una palabra del texto.

    Args:
        texto (str): Texto que queremos modificar.
        palabra_eliminar (str): Palabra que queremos eliminar.

    Returns:
        str: Texto sin la palabra indicada.
    """
    palabras = texto.split()
    palabras = [palabra for palabra in palabras
                if palabra != palabra_eliminar]

    return " ".join(palabras)


def procesar_texto(texto, opcion, *args):
    """
    Procesa un texto según la opción seleccionada.

    Args:
        texto (str): Texto que queremos procesar.
        opcion (str): Opción: contar, reemplazar o eliminar.
        *args: Argumentos adicionales según la opción.

    Returns:
        dict o str: Resultado del procesamiento.
    """
    if opcion == "contar":
        return contar_palabras(texto)

    elif opcion == "reemplazar":
        if len(args) != 2:
            return "Error: debes indicar la palabra original y la nueva."
        return reemplazar_palabras(texto, args[0], args[1])

    elif opcion == "eliminar":
        if len(args) != 1:
            return "Error: debes indicar la palabra que quieres eliminar."
        return eliminar_palabra(texto, args[0])

    else:
        return "Opción no válida."



texto = "Python es un lenguaje. Python es muy útil."

print("Texto original:")
print(texto)

# 1. Contar palabras
print("\nContar palabras:")
print(procesar_texto(texto, "contar"))

# 2. Reemplazar palabras
print("\nReemplazar palabras:")
print(procesar_texto(texto, "reemplazar", "Python", "Java"))

# 3. Eliminar palabra
print("\nEliminar palabra:")
print(procesar_texto(texto, "eliminar", "Python"))


# %%
#38.Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
"""
Programa que determina si es de día, de tarde o de noche
utilizando el módulo datetime.
"""

from datetime import datetime

def determinar_momento_dia():
    """
    Obtiene la hora actual y determina el momento del día.

    Returns:
        str: Indica si es de día, de tarde o de noche.
    """
    hora = datetime.now().hour

    if 6 <= hora < 12:
        return "Es de día"
    elif 12 <= hora < 20:
        return "Es de tarde"
    else:
        return "Es de noche"

print("La hora actual es:", datetime.now().strftime("%H:%M"))
print(determinar_momento_dia())


# %%
#39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. 


"""
Programa que determina la calificación en texto de un alumno
a partir de su calificación numérica.

Escala de calificaciones:
    0 - 69: Insuficiente
    70 - 79: Bien
    80 - 89: Muy bien
    90 - 100: Excelente
"""

def calcular_calificacion(nota):
    """
    Recibe una calificación numérica y devuelve su equivalente en texto.

    Args:
        nota (float): Calificación numérica del alumno.

    Returns:
        str: Calificación en texto o mensaje de error.
    """
    if 0 <= nota <= 69:
        return "Insuficiente"
    elif 70 <= nota <= 79:
        return "Bien"
    elif 80 <= nota <= 89:
        return "Muy bien"
    elif 90 <= nota <= 100:
        return "Excelente"
    else:
        return "Calificación no válida"

nota = float(input("Introduce la calificación del alumno: "))

print(calcular_calificacion(nota))



# %%
#40. Escribe una función que tome dos parámetros: "triangulo" ) y figura (una cadena que puede ser "rectangulo" , 
#"circulo" o datos (una tupla con los datos necesarios para calcular el área de la figura).
"""
Programa que calcula el área de diferentes figuras geométricas:
rectángulo, círculo y triángulo.
"""

import math


def calcular_area(figura, datos):
    """
    Calcula el área de una figura geométrica.

    Args:
        figura (str): Tipo de figura (rectangulo, circulo o triangulo).
        datos (tuple): Datos necesarios para calcular el área.

    Returns:
        float: Área de la figura geométrica.
    """

    if figura == "rectangulo":
        base, altura = datos
        return base * altura

    elif figura == "circulo":
        (radio,) = datos
        return math.pi * radio ** 2

    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2

    else:
        return "Figura no válida"


print("Área del rectángulo:", calcular_area("rectangulo", (5, 3)))

print("Área del círculo:", calcular_area("circulo", (4,)))

print("Área del triángulo:", calcular_area("triangulo", (6, 4)))


# %%
#41.En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el 
#monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo 
#siguiente:
#1. Solicita al usuario que ingrese el precio original de un artículo.
#2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
#3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
#4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor 
#a cero). Por ejemplo, descuento de 15€. 
#5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
#6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.

"""
Programa para calcular el precio final de una compra
aplicando un cupón de descuento si el usuario dispone de él.
"""

# 1. Solicitar el precio original del artículo
precio = float(input("Introduce el precio del artículo (€): "))

# Comprobar que el precio sea válido
if precio <= 0:
    print("El precio debe ser mayor que cero.")

else:
    # 2. Preguntar si tiene un cupón de descuento
    cupon = input("¿Tienes un cupón de descuento? (si/no): ").lower()

    # 3. Comprobar si tiene cupón
    if cupon == "si":
        descuento = float(input("Introduce el valor del descuento (€): "))

        # 4. Aplicar el descuento si es válido
        if descuento > 0:
            if descuento <= precio:
                precio_final = precio - descuento
                print(f"Descuento aplicado: {descuento} €")
                print(f"Precio final: {precio_final:.2f} €")
            else:
                print("El descuento no puede ser mayor que el precio.")
                print(f"Precio final: {precio:.2f} €")

        elif descuento <= 0:
            print("El descuento debe ser mayor que cero.")
            print(f"Precio final: {precio:.2f} €")

    elif cupon == "no":
        print("No se ha aplicado ningún descuento.")
        print(f"Precio final: {precio:.2f} €")

    else:
        print("Respuesta no válida. Debes escribir si o no.")



