# 29 - Crie um programa que lê um valor de início e um valor de fim, exibindo em tela a contagem dos números dentro desse intervalo.

valor_inicial = int(input("Digite o valor inicial: "))
valor_final = int(input("Digite o valor final: "))

for i in range(1, valor_final - 1):
    print(i + 1)