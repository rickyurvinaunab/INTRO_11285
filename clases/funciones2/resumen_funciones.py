# ============================================================
# Clase: Funciones en Python
# Contenidos:
# - Definición de funciones propias
# - Parámetros
# - Salida con return (1 valor)
# - Scope (ámbito) local
# - Definición vs. llamada
# - Uso de funciones definidas por otros (módulos / import)
# ============================================================

# -----------------------------
# 1) FUNCIONES PROPIAS
# -----------------------------

def saludar():
    # Ejemplo mínimo: función SIN parámetros y SIN return (solo imprime).
    print("Hola a todos 👋")


def saludar_a(nombre):
    # Ejemplo con PARÁMETRO: hace que la función sea flexible.
    print(f"Hola, {nombre}")


def cuadrado(numero):
    # Ejemplo con SALIDA (return de 1 valor).
    return numero * numero


def imprimir_vs_return():
    # Diferencia entre print y return:
    # - print: muestra algo en pantalla (efecto colateral).
    # - return: entrega un valor a quien llama (se puede guardar/usar).
    # A) Solo imprime (no devuelve nada, retorna None implícitamente)
    def solo_imprime(n):
        print(f"[solo_imprime] El doble de {n} es {2*n}")

    # B) Devuelve un valor (retorna un resultado)
    def devuelve_valor(n):
        return 2 * n

    solo_imprime(5)
    resultado = devuelve_valor(5)
    print(f"[devuelve_valor] El doble de 5 es {resultado} (lo guardé en una variable)")


def ejemplo_scope_local():
    # Demuestra que las variables definidas DENTRO de la función son LOCALES.
    x = 10  # <- variable local a la función
    print(f"[ejemplo_scope_local] Dentro de la función, x = {x}")


# (Opcional) Demostración de sombreado (shadowing) entre variable global y local
x = "soy_global"  # variable en el módulo (ámbito global)


def ejemplo_shadowing():
    x = "soy_local"  # <- esta x es distinta y "sombrea" a la global
    print(f"[ejemplo_shadowing] Dentro de la función, x = {x}")


# -------------------------------------------------------
# 2) FUNCIONES DEFINIDAS POR OTROS: IMPORTAR
# -------------------------------------------------------
# Python trae MUCHOS módulos en la biblioteca estándar (math, random, statistics, datetime, etc.)
# También podemos instalar o usar módulos creados por otras personas.
# Formas comunes de importación:

import math  # importar TODO el módulo
import random as rnd  # importar módulo con alias
from math import factorial  # importar solo una función específica

def ejemplos_imports():
    # Ejemplos básicos usando funciones de módulos externos (biblioteca estándar).
    # 1) Usando 'math'
    raiz_25 = math.sqrt(25)  # función sqrt del módulo math
    print(f"[imports] math.sqrt(25) = {raiz_25}")
    print(f"[imports] math.pi = {math.pi}")

    # 2) Usando 'random' con alias 'rnd'
    dado = rnd.randint(1, 6)  # entero aleatorio entre 1 y 6
    print(f"[imports] rnd.randint(1, 6) = {dado}")

    # 3) Usando 'from math import factorial'
    print(f"[imports] factorial(5) = {factorial(5)}")


# -----------------------------------------
# 3) MINI-EJERCICIOS
# -----------------------------------------

def promedio(a, b):
    # Retorna el promedio de dos números.
    return (a + b) / 2


def promedio_aleatorio():
    # Genera dos números aleatorios y calcula su promedio usando la función 'promedio'.
    a = rnd.randint(1, 50)
    b = rnd.randint(1, 50)
    p = promedio(a, b)
    print(f"[ejercicio] a={a}, b={b} -> promedio(a,b) = {p}")


# -----------------------------------------
# 4) USO DE LAS FUNCIONES DEFINIDAS ANTERIORMENTE
# -----------------------------------------

print("=== 1) Definición y llamada de funciones propias ===")
saludar()  # llamada
saludar_a("Ricardo")
saludar_a("Ingrid")

print("\n=== 2) Parámetros y retorno (1 valor) ===")
n = 5
print(f"cuadrado({n}) = {cuadrado(n)}")

print("\n=== 3) Diferencia print vs return ===")
imprimir_vs_return()

print("\n=== 4) Scope (ámbito) local ===")
ejemplo_scope_local()

print("\n=== 4.1) Shadowing (sombreado de nombres) ===")
print(f"[global] Antes de llamar, x global = {x}")
ejemplo_shadowing()
print(f"[global] Después de llamar, x global sigue siendo = {x}")

print("\n=== 5) Importar y usar funciones definidas por otros (módulos) ===")
ejemplos_imports()

print("\n=== 6) Mini-ejercicio con funciones propias + módulos ===")
promedio_aleatorio()

print("\n=== FIN DEMO ===")