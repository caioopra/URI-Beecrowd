# https://www.beecrowd.com.br/judge/pt/problems/view/1471?origem=1
while True:
    try:
        # N = numero de voluntarios, R = numero de voluntarios que retornaram
        N, R = [int(x) for x in input().split()]

        identificadores = [voluntario for voluntario in range(1, N + 1)]  # valor das placas de 1 até N
        id_retornaram = [int(x) for x in input().split()]

        id_nao_retornaram = []

        for valor in identificadores:
            if valor not in id_retornaram:
                id_nao_retornaram.append(valor)
        
        if id_nao_retornaram == []:
            print('*')
        else:
            for x in range(len(id_nao_retornaram)):
                print(id_nao_retornaram[x], end=" ")
            print('')


    except EOFError:  # tratamento para exceção com o fim de entradas
        break