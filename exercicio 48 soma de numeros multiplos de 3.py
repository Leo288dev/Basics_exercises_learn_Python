#Exercício Python 48: Faça um programa que calcule a soma entre
# todos os números que são múltiplos de três e que se encontram
# no intervalo de 1 até 500.
soma  = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
       cont  += 1
       soma  += c
print(f'A soma dos valores é : {soma}')
print(f'O total de valores múltiplos de 3 é: {cont} '
      f'dentro do intervalo informado')