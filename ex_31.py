# 31 - Crie um programa que realiza a Progressão Aritmética de 20 elementos, com primeiro termo e razão definidos pelo usuário:

primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

# for i in range(20):
#     primeiro_termo += razao
#     print(primeiro_termo)

# formula
# pa = primeiro_elemento + (qtd_elementos - 1) * razao

pa = primeiro_termo + (20 - 1) * razao

print(pa)