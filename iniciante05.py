'''
Projeto 4 - Nivel Iniciante
Classificador de IMC com Histórico

autor: Caio Lima
formato: arquivo python

link: https://github.com/caiolflima/projetos_python_iniciante/'''

print('-='*31)
print(f'{"Classificador de IMC com Histórico":^62}')

pessoas_nome = []
classificacao = ['Abaixo do Peso', 'Normal', 'Sobrepeso', 'Obesidade']
pessoa_imc = {}
pessoa_class = {}

while True:
    nome = str(input('Escreva o nome (ou fim): '))
    if nome == 'fim':
        break
    peso = float(input('Peso [kg]: '))
    altura = float(input('Altura [m]: '))
    imc = round((peso/(altura**2)),2)
    pessoas_nome.append(nome)
    if imc < 18.5:
        pessoa_class[nome] = str(classificacao[0])
    elif 18.5 <= imc < 25:
        pessoa_class[nome] = str(classificacao[1])
    elif 25 <= imc < 30:
        pessoa_class[nome] = str(classificacao[2])
    elif imc >= 30:
        pessoa_class[nome] = str(classificacao[3])
    pessoa_imc[nome] = str(imc)
print('Nome'.ljust(15),'|', 'IMC'.ljust(15),'|', 'Classificação')
for registro in pessoas_nome:
    print(registro.ljust(15),'|', pessoa_imc[registro].ljust(15),'|', pessoa_class[registro] )