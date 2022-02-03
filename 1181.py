# https://www.urionlinejudge.com.br/judge/pt/problems/view/1181
linha_escolha = int(input())
operacao = input().upper()

matriz = []

for i in range(12):
    linha = []
    for j in range(12):
        entrada = float(input())
        linha.append(entrada)
    matriz.append(linha)

soma = 0

for coluna in range(len(matriz[linha_escolha])):
    soma += matriz[linha_escolha][coluna]

soma = round(soma, 1)

if operacao == "S":
    print(soma)
else:
    print(round(soma / len(matriz[linha_escolha]), 1))
