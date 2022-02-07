# https://www.urionlinejudge.com.br/judge/pt/problems/view/1281
N = int(input())  # qtd de casos

for caso in range(N):
    M = int(input())  # M produtos com preco

    produtos = {}
    for i in range(M):
        produto, valor = input().split()
        produtos[produto] = float(valor)
    
    P = int(input())  # quantos tipos de produto serao comprados

    custo = 0
    for j in range(P):
        produto_escolhido, quantidade = input().split()
        custo += produtos[produto_escolhido] * int(quantidade)
    
    print(f"R$ {custo:.2f}")
