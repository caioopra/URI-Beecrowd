# https://www.urionlinejudge.com.br/judge/pt/problems/view/1150 
def comparar():
    x = int(input())
    z = x -1
    
    termos = 2
    soma = x
    somador = 1

    while z <= x:
        z = int(input())

    while soma <= z:
        soma = soma + x + somador
        if soma <= z:
            termos = termos + 1
            somador = somador + 1

    print(termos)

comparar()