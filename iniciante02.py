'''
Projeto 2 - Nivel Iniciante
Geometria de Poligonos e Poliedros

autor: Caio Lima
formato: arquivo python

link: https://github.com/caiolflima/projetos_python_iniciante/
'''

from math import pi
def apresentar_2d():
    print('''Qual caracteristica deseja calcular?
     P - Perimetro
     A - Area
     T - Todas as informacoes
     ''')
    return '>'

escolha = 0
caracter = ''

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
    7-> Paralelogramo
    ''')
    escolha = int(input('>'))
    while escolha not in (1,2,3,4,5,6,7):
        print('Escolha inválida.')
        escolha = int(input('>'))
    if escolha ==1:
        raio = float(input('Qual o raio do circulo? [cm]'))
        caracter = str(input(apresentar_2d())).upper().strip()[0]
        while caracter not in 'PAT':
            caracter = str(input(apresentar_2d())).upper().strip()[0]
        area = pi * (raio ** 2)
        perimetro = 2 * pi * raio
        if caracter == 'A':
            print(f'A área do Círculo é de: {area:.2f}cm2')
        elif caracter == 'P':
            print(f'O Perimetro do Círculo é de: {perimetro:.2f}cm')
        elif caracter == 'T':
            print(f'A área do Círculo é de: {area:.2f}cm2')
            print(f'O Perimetro do Círculo é de: {perimetro:.2f}cm')

elif dimensoes == 3:
    pass
