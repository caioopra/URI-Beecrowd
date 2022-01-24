# https://www.urionlinejudge.com.br/judge/pt/problems/view/1154
def calcular_media():
    entrada = 1
    soma = 0
    quantidade = 0

    while entrada > 0: 
        entrada = int(input())
        
        if entrada < 0:
            break

        soma += entrada
        quantidade += 1
    
    media = soma / quantidade

    print(f"{media:.2f}")


calcular_media()