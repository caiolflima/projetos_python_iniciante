'''
Projeto 2 - Nivel Iniciante
Geometria de Poligonos e Poliedros

autor: Caio Lima
formato: arquivo python

link: https://github.com/caiolflima/projetos_python_iniciante/
'''
from math import pi, sqrt
escolha = 0
caracter = forma = ' '

def apresentar_2d():
    print('''Qual caracteristica deseja calcular?
     P - Perimetro
     A - Area
     T - Todas as informacoes
     ''')
    return '>'

def erro_calculo(c):
    if c not in 'PAT':
        while c not in 'PAT':
            print('Escolha invalida.')
            c = str(input(apresentar_2d())).upper().strip()[0]
        return c
    else:
        return c

def mostrar_resultado2d(caracter, forma, area, perimetro):
    if caracter == 'A':
        return(f'A área do {forma} é de: {area:.2f}cm2')
    elif caracter == 'P':
        return(f'O Perimetro do {forma} é de: {perimetro:.2f}cm')
    elif caracter == 'T':
        return(f'A área do {forma} é de: {area:.2f}cm2\n' +
        f'O Perimetro do {forma} é de: {perimetro:.2f}cm')

print('-='*12)
dimensoes = int(input('Dimensões do objeto [2 ou 3]: '))
while dimensoes not in (2,3):
    print('Impossível calcular.')
    dimensoes = int(input('Dimensões do objeto [2 ou 3]: '))
if dimensoes == 2:
    print('Escolha sua forma: ')
    print('''    1-> Círculo
    2-> Triângulo Equilatero
    3-> Triângulo Isosceles
    4-> Quadrado
    5-> Retangulo
    6-> Losango
    7-> Paralelogramo''')
    escolha = int(input('>'))
    while escolha not in (1,2,3,4,5,6,7):
        print('Escolha inválida.')
        escolha = int(input('>'))
    if escolha ==1:
        forma = 'Círculo'
        raio = float(input('Qual o raio do circulo? [cm]'))
        caracter = erro_calculo(str(input(apresentar_2d())).upper().strip()[0])
        area = pi * (raio ** 2)
        perimetro = 2 * pi * raio
        print(mostrar_resultado2d(caracter, forma, area, perimetro))
    elif escolha ==2:
        forma = 'Triângulo Equilátero'
        lado = float(input('Qual o valor do lado do triângulo? [cm] '))
        caracter = erro_calculo(str(input(apresentar_2d())).upper().strip()[0])
        area = ((lado**2)/4)*sqrt(3)
        perimetro = lado * 3
        print(mostrar_resultado2d(caracter, forma, area, perimetro))
    elif escolha ==3:
        forma = 'Triângulo Isosceles'
        lado = float(input('Qual o valor do lado que não se repete? [cm] '))
        ladoRepetido = float(input('Qual o valor do lado que se repete? [cm] '))
        caracter = erro_calculo(str(input(apresentar_2d())).upper().strip()[0])
        area = lado/2 * sqrt(ladoRepetido**2 - (lado**2)/4)
        perimetro = (ladoRepetido * 2) + lado
        print(mostrar_resultado2d(caracter, forma, area, perimetro))
    elif escolha ==4:
        forma = 'Quadrado'
    elif escolha ==5:
        forma = 'Retângulo'
    elif escolha ==6:
        forma = 'Losango'
    elif escolha ==7:
        forma = 'Paralelogramo'

elif dimensoes == 3:
    pass
