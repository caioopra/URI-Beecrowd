participantes = int(input())

opinioes = [int(x) for x in input().split()]

satisfatorio = 0
nao_satisfatorio = 0

for i in range(participantes):
    if opinioes[i] == 1:
        nao_satisfatorio += 1
    else:
        satisfatorio += 1

if nao_satisfatorio >= satisfatorio:
    print("N")
else:
    print("Y")