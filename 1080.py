maior = 0
posicao = 0

for i in range(100):
    entrada = int(input())
    if entrada > maior:
        maior = entrada
        posicao = i + 1

print(maior)
print(posicao)