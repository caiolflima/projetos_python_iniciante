'''
Projeto 4 - Nivel Iniciante
Decodificador de Cores do Resistor

autor: Caio Lima
formato: arquivo python

link: https://github.com/caiolflima/projetos_python_iniciante/'''

resistores = {'preto':0, 'marrom':1, 'vermelho': 2, 'laranja':3, 'amarelo':4, 'verde':5, 'azul':6, 'violeta':7, 'cinza':8, 'branco':9}
calc_resistencia = []
print('Cores do Resistor:')
escolha_cores = str(input('Cores das três faixas (separadas por espaço): ')).split()

for cor in escolha_cores:
    if cor not in resistores:
        print(f'Cor {cor} inválida. Escreva novas cores:')
        escolha_cores = str(input('Cores das três faixas (separadas por espaço): ')).split()
    elif cor in resistores:
        calc_resistencia.append(resistores[cor])
resistencia = ((calc_resistencia[0]*10)+calc_resistencia[1])*10**calc_resistencia[2]

if resistencia < 1000:
    print(f'Resistência: {resistencia}Ω.')
elif resistencia > 1000:
    print(f'Resistência: {resistencia/1000}kΩ.')
elif resistencia > 1000000:
    print(f'Resistência: {resistencia/1000000}MΩ')
print('Fim do Programa')