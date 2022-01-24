def analisar_jogos(qtd_jogos, lista):
    max_atual = 0
    posicao_max = []
    
    for i in range(qtd_jogos):
        if lista[i] >= max_atual and lista[i] > 0:
            max_atual = lista[i]
            posicao_max.append(i + 1)

    if len(posicao_max) == 0:
        return "nenhum"
    elif len(posicao_max) == 1:
        posicao_max.append(posicao_max[0])
        return (posicao_max)
    else:
        return posicao_max[0], posicao_max[len(posicao_max) - 1]


n = 1

while True:
    qtd_jogos = int(input())
    lista = []

    if qtd_jogos == 0:
        break
    else:
        print("Teste", n)
        for i in range(qtd_jogos):
            x, y = [int(x) for x in input().split()]
            lista.append(x - y)

        periodo = analisar_jogos(qtd_jogos, lista)
        tamanho_lista = len(periodo)
        
        print(tamanho_lista)

        if tamanho_lista == 6:
            print("nenhum")
        else:
            for j in range(tamanho_lista):
                print(periodo[j], end = " ")
                print()
        print()

        n += 1