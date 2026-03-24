"""
Módulo de operações matemáticas básicas.
"""

from typing import Union

Number = Union[int, float]


def soma(a: Number, b: Number) -> Number:
    """
    Retorna a soma de dois números.

    :param a: Primeiro número
    :param b: Segundo número
    :return: Soma de a + b
    """
    return a + b


def subtracao(a: Number, b: Number) -> Number:
    """
    Retorna a subtração de dois números.

    :param a: Primeiro número
    :param b: Segundo número
    :return: Resultado de a - b
    """
    return a - b


def multiplicacao(a: Number, b: Number) -> Number:
    """
    Retorna a multiplicação de dois números.

    :param a: Primeiro número
    :param b: Segundo número
    :return: Produto de a * b
    """
    return a * b


def divisao(a: Number, b: Number) -> float:
    """
    Retorna a divisão de dois números.

    :param a: Numerador
    :param b: Denominador
    :raises ValueError: Se b for zero
    :return: Resultado da divisão
    """
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b


def potencia(a: Number, b: Number) -> Number:
    """
    Retorna a potência de um número.

    :param a: Base
    :param b: Expoente
    :return: Resultado de a elevado a b
    """
    return a ** b
