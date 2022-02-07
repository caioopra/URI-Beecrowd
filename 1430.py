# https://www.urionlinejudge.com.br/judge/pt/problems/view/1430
duracao = {
    "W": 1,
    "H": 1 / 2,
    "Q": 1 / 4,
    "E": 1 / 8,
    "S": 1 / 16,
    "T": 1 / 32,
    "X": 1 / 64
}

while True:
    composicao = input().split("/")
    if composicao == ["*"]:
        break

    del composicao[0]

    acertos = 0

    for compasso in composicao:
        soma = 0

        for letra in compasso:
            soma += duracao[letra]

        if soma == 1:
            acertos += 1

    print(acertos)
