'''
Projeto 2 - Nivel Iniciante
Geometria de Poligonos e Poliedros

autor: Caio Lima
formato: arquivo python

link: https://github.com/caiolflima/projetos_python_iniciante/

-=-=-=-=-=-=--=-=-=-=-=\n
Funções criadas no Projeto:\n
def apresentar_caracter(): - Oferece menu de opções de cálculos de formas 2d ou 3d\n
def verificar_escolha(c): - Recolhe escolha do menu e tratamento de erros\n
def mostrar_resultado(caracter, forma, area, perimetro_vol): - Apresenta os resultados das opções escolhidas no menu\n

Formas 2d:\n
def recolher_valores2d(): - Verifica a forma escolhida, recolhe e informa os atributos necessários de formas 2d\n
def perimetro_tri(l1, l2): - Calcula o perimetro dos triangulos\n
def area_retangulo(l1, l2): - Calcula a area do quadrado, retangulo e paralelogramo\n
def perimetro_quad(l1, l2): - Calculo o perimetro do quadrado e retangulo\n
def checar_tri(l1,l2): - Checa se os lados do triângulo isósceles formam triângulo\n

Formas 3d:\n
def recolher_valores3d(): - Verifica a forma escolhida, recolhe e informa os atributos necessários de formas 2d\n

'''
from math import pi, sqrt
escolha = 0
caracter = forma = ' '
formas_2d = ['Círculo', 'Triângulo Equilatero', 'Triângulo Isosceles','Quadrado', 'Retangulo', 'Losango', 'Paralelogramo' ]
formas_3d = ['Esfera', 'Cubo', 'Paralelepípeto', 'Piramide (Base Triangular)', 'Piramide (Base Quadrada)']
atributos2d = ['- Raio: ', '- Lado: ', '- 1:Lado / 2:Lado que se repete: ', '- Lado: ', '- 1:Lado a / 2:Lado b: ', '- 1:Diagonal Maior / 2:Diagonal Menor: ', '- 1:Base / 2:Altura / 3:Lado lateral: ']
atributos3d = ['- Raio: ', '- Lado: ', '- 1:Lado a / 2:Lado b / 3:Lado c: ', '- 1: Lado Base / 2: Altura: ']

def recolher_valores2d():
    forma = formas_2d[escolha-1]
    print(forma, atributos2d[escolha - 1])
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

def recolher_valores3d():
    forma = formas_3d[escolha-1]
    if escolha==5:
        print(forma, atributos3d[4])
    else:
        print(forma, atributos3d[escolha-1])
    atributo1 = float(input('Escreva o primeiro valor [cm]: '))
    while atributo1 <= 0:
        atributo1 = float(input('Escreva o primeiro valor [cm]: '))
    if escolha in (3, 4, 5):
        atributo2 = float(input('Escreva o segundo valor [cm]: '))
        while atributo2 <= 0:
            atributo2 = float(input('Escreva o terceiro valor [cm]: '))
        if escolha==3:
            atributo3 = float(input('Escreva o terceiro valor [cm]: '))
            while atributo3 <= 0:
                atributo3 = float(input('Escreva o terceiro valor [cm]: '))
        return forma, atributo1, atributo2
    return forma, atributo1

def apresentar_caracter():
    if dimensoes ==2:
        print('Qual caracteristica deseja calcular?\n P - Perimetro\n A - Area\n T - Todas as informacoes')
    else:
        print('Qual caracteristica deseja calcular?\n V - Volume\n A - Area\n T - Todas as informacoes')
    return '>'

def verificar_escolha(c):
    opcoes_menu = ' '
    if dimensoes ==2:
        opcoes_menu = 'PAT'
    elif dimensoes ==3:
        opcoes_menu = 'VAT'
    while c not in opcoes_menu:
        print('Escolha invalida.')
        c = str(input(apresentar_caracter())).upper().strip()[0]
    return c

def mostrar_resultado(caracter, forma, area, perimetro_vol):
    if dimensoes ==2:
        if caracter == 'A':
            return(f'A área do {forma} é de: {area:.2f}cm2')
        elif caracter == 'P':
            return(f'O Perimetro do {forma} é de: {perimetro_vol:.2f}cm')
        elif caracter == 'T':
            return(f'A área do {forma} é de: {area:.2f}cm2\n' +
            f'O Perimetro do {forma} é de: {perimetro_vol:.2f}cm')
    elif dimensoes ==3:
        if caracter == 'A':
            return(f'A área do {forma} é de: {area:.2f}cm2')
        elif caracter == 'P':
            return(f'O Volume do {forma} é de: {perimetro_vol:.2f}cm3')
        elif caracter == 'T':
            return(f'A área do {forma} é de: {area:.2f}cm2\n' +
            f'O Volume do {forma} é de: {perimetro_vol:.2f}cm3')

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
        forma, raio = recolher_valores2d()
        caracter = verificar_escolha(str(input(apresentar_caracter())).upper().strip()[0])
        area = pi * (raio ** 2)
        perimetro = 2 * pi * raio
        print(mostrar_resultado(caracter, forma, area, perimetro))
    elif escolha ==2:
        forma, lado = recolher_valores2d()
        caracter = verificar_escolha(str(input(apresentar_caracter())).upper().strip()[0])
        area = ((lado**2)/4)*sqrt(3)
        print(mostrar_resultado(caracter, forma, area, perimetro_tri(lado, lado)))
    elif escolha ==3:
        forma, lado, ladoRepetido = recolher_valores2d()
        caracter = verificar_escolha(str(input(apresentar_caracter())).upper().strip()[0])
        area = lado/2 * sqrt(ladoRepetido**2 - (lado**2)/4)
        print(mostrar_resultado(caracter, forma, area, perimetro_tri(ladoRepetido, lado)))
    elif escolha ==4:
        forma, lado = recolher_valores2d()
        caracter = verificar_escolha(str(input(apresentar_caracter())).upper().strip()[0])
        print(mostrar_resultado(caracter, forma, area_retangulo(lado, lado), perimetro_quad(lado, lado)))
    elif escolha ==5:
        forma, lado_a, lado_b = recolher_valores2d()
        caracter = verificar_escolha(str(input(apresentar_caracter())).upper().strip()[0])
        print(mostrar_resultado(caracter, forma, area_retangulo(lado_a, lado_b), perimetro_quad(lado_a, lado_b)))
    elif escolha ==6:
        forma, diag_maior, diag_menor = recolher_valores2d()
        caracter = verificar_escolha(str(input(apresentar_caracter())).upper().strip()[0])
        area = (diag_maior * diag_menor)/2
        perimetro = 2*sqrt((diag_maior**2)+(diag_menor**2))
        print(mostrar_resultado(caracter, forma, area, perimetro))
    elif escolha ==7:
        forma, base, altura, lado_lateral = recolher_valores2d()
        caracter = verificar_escolha(str(input(apresentar_caracter())).upper().strip()[0])
        perimetro = (base*2)+ (lado_lateral*2)
        print(mostrar_resultado(caracter, forma, area_retangulo(base, altura), perimetro))
elif dimensoes == 3:
    print('Escolha sua forma:\n 1 - Esfera\n 2 - Cubo\n 3 - Paralelepípeto\n 4 - Piramide (Base Triangular)\n 5 - Piramide (Base Quadrada)')
    escolha = int(input('>'))
    while escolha not in (1,2,3,4,5):
        escolha = int(input('Escolha invalida!\n Escolha sua forma: \n>'))
    if escolha == 1:
        forma, raio = recolher_valores3d()
        caracter = verificar_escolha(str(input(apresentar_caracter())).upper().strip()[0])
        area = 4*(pi * (raio**2))
        volume = (4*(pi * (raio**3)))/3
        print(mostrar_resultado(caracter, forma, area, volume))
    elif escolha ==2:
        forma, lado = recolher_valores3d()
        caracter = verificar_escolha(str(input(apresentar_caracter())).upper().strip()[0])
        area = 6*area_retangulo(lado,lado)
        volume = lado**3
        print(mostrar_resultado(caracter, forma, area, volume))
    elif escolha ==3:
        forma, altura, largura, profund = recolher_valores3d()
        caracter = verificar_escolha(str(input(apresentar_caracter())).upper().strip()[0])
        area = (2*(altura*largura)) + (2*(altura*profund)) + (2*(profund*largura))
        volume = altura*largura*profund
        print(mostrar_resultado(caracter, forma, area, volume))
    elif escolha ==4:
        pass
    elif escolha ==5:
        pass
print('Fim do Programa.')
