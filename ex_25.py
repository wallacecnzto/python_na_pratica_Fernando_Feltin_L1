# 25 - Peça para que o usuário digite um número, em seguida exiba em tela uma mensagem dizendo se tal número é PAR ou se é ÍMPAR:

num = int(input("Digite um número: "))

print(f"{num} é PAR" if num % 2 == 0 else f"{num} é IMPAR")
