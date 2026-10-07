# Crie um programa que realiza a contagem de 1 até 100, usando apenas de números ímpares, ao final do processo exiba em tela quantos números ímpares foram encontrados nesse intervalo, assim como a soma dos mesmos:

qtd_impares = 0
soma_impares = 0

for i in range(1, 101):
    if i % 3 == 0:
        qtd_impares += 1
        soma_impares += i
    
print(f"Foram encontrados {qtd_impares} de números ímpares!")
print(f"A soma deste números é {soma_impares}!")
