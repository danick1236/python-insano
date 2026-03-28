nome = input('Qual seu nome? ')
cidade = input('Qual sua cidade natal? ')
ano = int(input('Em que ano você nasceu? '))
nota1 = float(input('Agora, sobre suas últimas 3 provas, qual foi a nota da primeira? '))
nota2 = float(input('A nota da segunda? '))
nota3 = float(input('E por último, qual a terceira nota? '))
temp = int(input('Qual a temperatura no seu bairro agora? '))

media = (nota1 + nota2 + nota3) / 3
idade = 2026 - ano
tempf = temp * 1.8 + 32

print()
print(f'Olá, {nome}! Você é de {cidade}.')
print(f'Você tem {idade} anos de idade!')
print(f'Sua média de notas é {media:.2f}!')
print(f'E em Fahrenheit a temperatura no seu bairro seria {tempf}!')