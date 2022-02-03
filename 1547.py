# https://www.beecrowd.com.br/judge/pt/problems/view/1547?origem=1
casos = int(input())  # numero de casos de teste

for caso in range(casos):
    QT, S = [int(x) for x in input().split()]  # QT = qtd de alunos do grupo, S = numero secreto

    valores = [int(x) for x in input().split()]  # lista de entradas do valore de cada aluno 
    acertou = -1
    
    posi_prox = 0
    dif_proximidade = 101
 
    for i in range(QT):
        if valores[i] == S:
            acertou = i
            break
        else:  # caso nao acerte, verifica a proximidade com o valor secreto
            diferenca = abs(S - valores[i])

            if diferenca < dif_proximidade:  # se for mais proximo, atualiza qual o valor e sua posicao
                dif_proximidade = diferenca
                posi_prox = i
                
    if acertou == -1:
        print(posi_prox + 1)
    else:
        print(acertou + 1)
