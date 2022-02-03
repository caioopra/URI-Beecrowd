# https://www.beecrowd.com.br/judge/pt/problems/view/1184?origem=1
# matriz 12x12

operacao = input().upper()

matriz = []
for i_linha in range(12):
    linha = []
    for j_linha in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)

soma = 0
numero_somas = 0
# loop descendo as linhas (não soma na linha 0)
for i in range(1, 13):
    for j in range(i - 1):
        soma += matriz[i - 1][j]
        numero_somas += 1

soma = round(soma)

if operacao == "S":
    print(soma)
else:
    print(round((soma / numero_somas), 1))
