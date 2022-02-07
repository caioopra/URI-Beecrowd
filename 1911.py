# https://www.beecrowd.com.br/judge/pt/problems/view/1911?origem=1
N = -1
falsas = []

while True:
    N = int(input())

    if N == 0:
        break

    while not (1 <= N <= 50):
        N = int(input())

    alunos = {}
    for i in range(N):
        nome, assinatura_original = input().split()
        alunos[nome] = assinatura_original

    M = int(input())
    while not (0 <= M <= N):
        M = int(input())

    qtd_assinaturas_falsas = 0

    for i in range(M):
        nome, assinatura_aula = input().split()
        
        erros = 0

        for j in range(len(assinatura_aula)):
            if assinatura_aula[j] != alunos[nome][j]:
                erros += 1
        if erros > 1:
            qtd_assinaturas_falsas += 1
                    
            
    print(qtd_assinaturas_falsas)      
    