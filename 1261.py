# https://www.urionlinejudge.com.br/judge/pt/problems/view/1261
M, N = [int(x) for x in input().split()]

dicionario = {}
for i in range(M):
    cargo, valor = input().split()
    valor = int(valor)

    dicionario[cargo] = valor

for i in range(N):
    descricao = []
    entrada = 0

    while entrada != ".":
        entrada = input()
        descricao.append(entrada.split())

    soma = 0

    # TODO: debug com valores (tá somando errado)
    for j in range(len(descricao) - 1):
        for k in range(len(descricao[j])):
            if descricao[j][k] in dicionario:
                soma += dicionario[descricao[j][k]]

    print(soma)
