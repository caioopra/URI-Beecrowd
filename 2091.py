# https://www.urionlinejudge.com.br/judge/pt/problems/view/2091
while True:
    N = int(input())
    if N == 0:
        break

    lista = [int(x) for x in input().split()]
    conjunto = set(lista)
    dicionario = {}

    for elemento in conjunto:
        dicionario[elemento] = 0

    for i in lista:
        dicionario[i] += 1

    for j in dicionario:
        if (dicionario[j] % 2) != 0:
            print(j)
