'''
Projeto 3 - Nivel Iniciante
Conversor de Tempo

autor: Caio Lima
formato: arquivo python

link: https://github.com/caiolflima/projetos_python_iniciante/'''

print('-='*30)
print(f'{"Conversor de segundos":^60}')
segundos_entrada = int(input('Quantos segundos deseja converter? '))

anos = segundos_entrada // 31536000
segundos_entrada -= (31536000 * anos)
meses = segundos_entrada // 2628000
segundos_entrada -= (2628000 * meses)
semanas = segundos_entrada // 604800
segundos_entrada -= (604800 * semanas)
dias = segundos_entrada // 86400
segundos_entrada -= (86400 * dias)
horas = segundos_entrada // 3600
segundos_entrada -= (3600 * horas)
minutos = segundos_entrada // 60
segundos_entrada -= (60 * minutos)

if anos > 0:
    print(f'{anos} anos, ',end='')
if meses > 0:
    print(f'{meses} meses, ',end='')
if semanas > 0:
    print(f'{semanas} semanas, ',end='')
if dias > 0:
    print(f'{dias} dias, ',end='')
if horas > 0:
    print(f'{horas} horas, ',end='')
if minutos > 0:
    print(f'{minutos} minutos, ',end='')
if segundos_entrada > 0:
    print(f'{segundos_entrada} segundos.')