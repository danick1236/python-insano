valor = float(input('Qual o valor que você recebe por hora? '))
horas = int(input('Quantas horas você trabalha por mês? '))

salario = valor * horas
desconto = salario * 0.11

salarioliq = salario - desconto

print()
print(f'Este é o seu salário!\n R${salarioliq:.2f}')