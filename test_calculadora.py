from calculadora import *

def test_soma():
    assert soma(1,1) == 2

def test_subtrair():
    assert subtrair(4,2) == 2

def test_multiplicar():
    assert multiplicar(2,2) == 4

def test_dividir():
    assert dividir(4,2) == 2

def test_raiz_quadrada():
    assert raiz_quadrada(25) == 5

def test_divisao_inteira():
    assert divisao_inteiro(7,2) == 3