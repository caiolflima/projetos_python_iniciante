'''
Projeto 1 - Nivel Iniciante
Sorteio de Dados de RPG

autor: Caio Lima
formato: arquivo python

link: https://github.com/caiolflima/projetos_python_iniciante/
'''

from random import randint, seed
from time import sleep

faces_dado = int(input('Quantas faces tem o dado? '))
soma = 0
media = 0.0
seed(42)
print('Rolando dados...')
print('-='*12)
sleep(2)
for c in range(1,4):
    resultado = randint(1,faces_dado)
    print(f'{resultado}, ', end='')
    soma += resultado
media = soma/3
print(f'Soma: {soma} | Média: {media:.2f}')