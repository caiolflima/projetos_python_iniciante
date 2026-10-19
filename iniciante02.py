'''
Projeto 2 - Nivel Iniciante
Geometria de Poligonos e Poliedros

autor: Caio Lima
formato: arquivo python

link: https://github.com/caiolflima/projetos_python_iniciante/

-=-=-=-=-=-=--=-=-=-=-=
Funções criadas no Projeto:
def recolher_valores(): - Verifica a forma escolhida, recolhe e informa os atributos necessários

Formas 2d:
def apresentar_2d(): - Oferece menu de opções de cálculos de formas 2d
def erro_calculo(c): - Tratamento de erros para a escolha de cálculo do menu
def mostrar_resultado2d(caracter, forma, area, perimetro): - Apresenta os resultados das opções escolhidas no menu
def perimetro_tri(l1, l2): - Calcula o perimetro dos triangulos
def area_retangulo(l1, l2): - Calcula a area do quadrado, retangulo e paralelogramo
def perimetro_quad(l1, l2): - Calculo o perimetro do quadrado e retangulo
def checar_tri(l1,l2): - Checa se os lados do triângulo isósceles forma triângulo

'''
from math import pi, sqrt
escolha = 0
caracter = forma = ' '
formas_2d = ['Círculo', 'Triângulo Equilatero', 'Triângulo Isosceles','Quadrado', 'Retangulo', 'Losango', 'Paralelogramo' ]
atributos2d = ['- Raio: ', '- Lado: ', '- 1:Lado / 2:Lado que se repete: ', '- Lado: ', '- 1:Lado a / 2:Lado b: ', '- 1:Diagonal Maior / 2:Diagonal Menor: ', '- 1:Base / 2:Altura / 3:Lado lateral: ']

def recolher_valores():
    forma = formas_2d[escolha-1]
    print(forma, atributos2d[escolha-1])
    atributo1 = float(input('Escreva o primeiro valor [cm]: '))
    while atributo1 <= 0:
        atributo1 = float(input('Escreva o primeiro valor [cm]: '))
    if escolha in (3,5,6,7):
        atributo2 = float(input('Escreva o segundo valor [cm]: '))
        while atributo2 <= 0:
            atributo2 = float(input('Escreva o segundo valor [cm]: '))
        if escolha ==3:
            atributo1 = checar_tri(atributo1, atributo2)
        if escolha == 7:
            atributo3 = float(input('Escreva o terceiro valor [cm]: '))
            while atributo3 <= 0:
                atributo3 = float(input('Escreva o terceiro valor [cm]: '))
            return forma, atributo1, atributo2, atributo3
        return forma, atributo1, atributo2
    else:
        return forma, atributo1

def apresentar_2d():
    print('Qual caracteristica deseja calcular?\n P - Perimetro\n A - Area\n T - Todas as informacoes')
    return '>'

def erro_calculo(c):
    while c not in 'PAT':
        print('Escolha invalida.')
        c = str(input(apresentar_2d())).upper().strip()[0]
    return c

def mostrar_resultado2d(caracter, forma, area, perimetro):
    if caracter == 'A':
        return(f'A área do {forma} é de: {area:.2f}cm2')
    elif caracter == 'P':
        return(f'O Perimetro do {forma} é de: {perimetro:.2f}cm')
    elif caracter == 'T':
        return(f'A área do {forma} é de: {area:.2f}cm2\n' +
        f'O Perimetro do {forma} é de: {perimetro:.2f}cm')

def perimetro_tri(l1, l2):
    perimetro = (l1*2) + l2
    return perimetro

def area_retangulo(l1, l2):
    area = l1 * l2
    return area

def perimetro_quad(l1, l2):
    perimetro = (l1*2) + (l2*2)
    return perimetro

def checar_tri(l1,l2):
    while l1 >= (l2*2):
        l1 = float(input('O primeiro lado é maior do que a soma dos outros lados.\n Não forma triângulo.\n Inserir novo primeiro lado [cm]: '))
    return l1

print('-='*12)
dimensoes = int(input('Dimensões do objeto [2 ou 3]: '))
while dimensoes not in (2,3):
    print('Impossível calcular.')
    dimensoes = int(input('Dimensões do objeto [2 ou 3]: '))
if dimensoes == 2:
    print('Escolha sua forma:\n 1-> Círculo\n 2-> Triângulo Equilatero\n 3-> Triângulo Isosceles\n 4-> Quadrado\n 5-> Retangulo\n 6-> Losango\n 7-> Paralelogramo')
    escolha = int(input('>'))
    while escolha not in (1,2,3,4,5,6,7):
        print('Escolha inválida.')
        escolha = int(input('>'))
    if escolha ==1:
        forma, raio = recolher_valores()
        caracter = erro_calculo(str(input(apresentar_2d())).upper().strip()[0])
        area = pi * (raio ** 2)
        perimetro = 2 * pi * raio
        print(mostrar_resultado2d(caracter, forma, area, perimetro))
    elif escolha ==2:
        forma, lado = recolher_valores()
        caracter = erro_calculo(str(input(apresentar_2d())).upper().strip()[0])
        area = ((lado**2)/4)*sqrt(3)
        print(mostrar_resultado2d(caracter, forma, area, perimetro_tri(lado,lado)))
    elif escolha ==3:
        forma, lado, ladoRepetido = recolher_valores()
        caracter = erro_calculo(str(input(apresentar_2d())).upper().strip()[0])
        area = lado/2 * sqrt(ladoRepetido**2 - (lado**2)/4)
        print(mostrar_resultado2d(caracter, forma, area, perimetro_tri(ladoRepetido, lado)))
    elif escolha ==4:
        forma, lado = recolher_valores()
        caracter = erro_calculo(str(input(apresentar_2d())).upper().strip()[0])
        print(mostrar_resultado2d(caracter, forma, area_retangulo(lado,lado), perimetro_quad(lado,lado)))
    elif escolha ==5:
        forma, lado_a, lado_b = recolher_valores()
        caracter = erro_calculo(str(input(apresentar_2d())).upper().strip()[0])
        print(mostrar_resultado2d(caracter, forma, area_retangulo(lado_a, lado_b), perimetro_quad(lado_a, lado_b)))
    elif escolha ==6:
        forma, diag_maior, diag_menor = recolher_valores()
        caracter = erro_calculo(str(input(apresentar_2d())).upper().strip()[0])
        area = (diag_maior * diag_menor)/2
        perimetro = 2*sqrt((diag_maior**2)+(diag_menor**2))
        print(mostrar_resultado2d(caracter, forma, area, perimetro))
    elif escolha ==7:
        forma, base, altura, lado_lateral = recolher_valores()
        caracter = erro_calculo(str(input(apresentar_2d())).upper().strip()[0])
        perimetro = (base*2)+ (lado_lateral*2)
        print(mostrar_resultado2d(caracter, forma, area_retangulo(base, altura), perimetro))
elif dimensoes == 3:
    pass
