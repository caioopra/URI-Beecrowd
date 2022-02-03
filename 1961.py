# https://www.beecrowd.com.br/judge/pt/problems/view/1961?origem=1
pulo, qtd_canos = [int(x) for x in input().split()]
canos = [int(x) for x in input().split()]

falhou = 0

for i in range(1, qtd_canos):  # precisa começar com 1 para não comparar o primeiro com o ultimo na primeira vez
    if abs(canos[i] - canos[i - 1]) > pulo:
        falhou = 1
        break

if falhou:
    print("GAME OVER")
else:
    print("YOU WIN")
