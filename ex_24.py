# 24 - Crie duas variáveis com dois valores numéricos inteiros digitados pelo usuário, caso o valor do primeiro número for maior que o do segundo, exiba em tela uma mensagem de acordo, caso contrário, exiba em tela uma mensagem dizendo que o primeiro valor digitado é menor que o segundo:

primeiro_valor = int(input("Digite o primeiro valor: "))
segundo_valor = int(input("Digite o segundo valor: "))

if primeiro_valor > segundo_valor:
    print("O primeiro número digitado é maior que o segundo")
else:
    print("O primeiro número digitado é menor que o segundo")