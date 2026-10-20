'''
Projeto 4 - Nivel Iniciante
Classificador de IMC com Histórico

autor: Caio Lima
formato: arquivo python

link: https://github.com/caiolflima/projetos_python_iniciante/'''

print('-='*31)
print(f'{"Classificador de IMC com Histórico":^62}')

classificacao = ['Abaixo do Peso', 'Normal', 'Sobrepeso', 'Obesidade']

while True:
    nome = str(input('Escreva o nome (ou fim): '))
    if nome == 'fim':
        break
    peso = float(input('Peso [kg]: '))
    altura = float(input('Altura [m]: '))
    imc = (peso/(altura**2))
    pessoa_imc = {nome: f'{imc:.2f}'}
    if imc < 18.5:
        pessoa_class = {nome: classificacao[0]}
    elif 18.5 <= imc < 25:
        pessoa_class = {nome: classificacao[1]}
    elif 25 <= imc < 30:
        pessoa_class = {nome: classificacao[2]}
    elif imc >= 30:
        pessoa_class = {nome: classificacao[3]}
print('Nome'.ljust(25),'|', 'IMC'.ljust(25),'|', 'Classificação')
for pessoa in pessoa_imc:
    print(pessoa_imc[nome].ljust(25),'|', pessoa_imc[imc].just(25),'|', pessoa_class[nome] )

