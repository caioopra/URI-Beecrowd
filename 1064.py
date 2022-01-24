# https://www.urionlinejudge.com.br/judge/pt/problems/view/1064
def media_positivos():
    soma_positivos = 0
    qtd_positivos = 0 
    
    for i in range(6):
        entrada = float(input())

        if entrada > 0:
            soma_positivos += entrada
            qtd_positivos += 1
    
    print(f"{qtd_positivos} valores positivos\n{soma_positivos/qtd_positivos:.1f}")


media_positivos()