# Crie um programa que exibe em tela a tabuada de um determinado número fornecido pelo usuário:

numero = int(input("Digite um número: "))

for i in range(1, 11):
    print(f"{numero} * {i} = {numero * i}")
    
