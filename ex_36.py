# Crie um programa que pede que o usuário digite um nome ou uma frase, verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em tela esse resultado.

texto = input("Digite o nome ou uma frase: ")
novo_texto = texto.strip().lower()
print(novo_texto)
if texto == novo_texto[::-1].title():
    print(f"{texto} é palíndromo!")
else:
    print(f"{texto} não é palíndromo!")

