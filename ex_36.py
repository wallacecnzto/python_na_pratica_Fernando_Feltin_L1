# Crie um programa que pede que o usuário digite um nome ou uma frase, verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em tela esse resultado.

texto = str(input("Digite o nome ou uma frase: ")).strip().lower()
palavras = texto.split()
caracteres = "".join(palavras)
frase_invertida = ""

for i in range(len(caracteres)-1, -1, -1):
    frase_invertida += caracteres[i]
    
print(caracteres, frase_invertida)

if frase_invertida == caracteres:
    print(f"É palíndromo!")
else:
    print(f"Não é palíndromo!")

